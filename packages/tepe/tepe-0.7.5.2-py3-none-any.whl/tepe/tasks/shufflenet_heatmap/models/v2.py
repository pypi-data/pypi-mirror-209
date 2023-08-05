import torch
import torch.nn as nn
from tepe.modules.backbone import ShuffleNetV2
from tepe.modules.neck import PAN


class ComputeLoss(nn.Module):
    def __init__(self, compute_paf_loss=True, class_weights=None):
        super(ComputeLoss, self).__init__()
        self.kpt_loss_func = nn.MSELoss(size_average=None, reduce=None, reduction='sum')
        self.paf_loss_func = nn.MSELoss(size_average=None, reduce=None, reduction='sum')
        self.class_weights = class_weights
        self.compute_paf_loss = compute_paf_loss
        # self.seg_loss_func = nn.BCEWithLogitsLoss()

    def __call__(self, preds, data):

        if self.compute_paf_loss:
            kpt_labels, paf_labels = data['target'], data['paf_maps']
            device = kpt_labels.device
            paf_labels = paf_labels.to(device)
            lkpt, lpaf = torch.zeros(1, device=device), torch.zeros(1, device=device)
            for i in range(0, len(preds), 2):
                kpt_preds, paf_preds = preds[i], preds[i+1]

                lkpt += self.kpt_loss_func(kpt_preds, kpt_labels) / kpt_labels.shape[0]
                lpaf += self.paf_loss_func(paf_preds, paf_labels) / paf_labels.shape[0]

            loss = lkpt + lpaf
            loss_dict = {'loss': loss, 'kpt_loss': lkpt, 'paf_loss': lpaf}

            return loss_dict
        else:
            kpt_labels = data['target']
            device = kpt_labels.device
            lkpt = torch.zeros(1, device=device)
            for i in range(len(preds)):
                kpt_preds = preds[i]
                lkpt += self.kpt_loss_func(kpt_preds, kpt_labels) / kpt_labels.shape[0]

            loss_dict = {'loss': lkpt}

            return loss_dict


def conv(in_channels, out_channels, kernel_size=3, padding=1, bn=True, dilation=1, stride=1, relu=True, bias=True):
    modules = [nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, bias=bias)]
    if bn:
        modules.append(nn.BatchNorm2d(out_channels))
    if relu:
        modules.append(nn.ReLU(inplace=True))
    return nn.Sequential(*modules)


class InitialStage(nn.Module):
    def __init__(self, num_channels, num_heatmaps, num_pafs):
        super().__init__()
        self.trunk = nn.Sequential(
            conv(num_channels, num_channels, bn=False),
            conv(num_channels, num_channels, bn=False),
            conv(num_channels, num_channels, bn=False)
        )
        self.heatmaps = nn.Sequential(
            conv(num_channels, 512, kernel_size=1, padding=0, bn=False),
            conv(512, num_heatmaps, kernel_size=1, padding=0, bn=False, relu=False)
        )
        self.pafs = nn.Sequential(
            conv(num_channels, 512, kernel_size=1, padding=0, bn=False),
            conv(512, num_pafs, kernel_size=1, padding=0, bn=False, relu=False)
        ) if num_pafs > 0 else None

    def forward(self, x):
        trunk_features = self.trunk(x)
        heatmaps = self.heatmaps(trunk_features)
        if self.pafs is not None:
            pafs = self.pafs(trunk_features)
            return [heatmaps, pafs]
        else:
            return [heatmaps]


class RefinementStageBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.initial = conv(in_channels, out_channels, kernel_size=1, padding=0, bn=False)
        self.trunk = nn.Sequential(
            conv(out_channels, out_channels),
            conv(out_channels, out_channels, dilation=2, padding=2)
        )

    def forward(self, x):
        initial_features = self.initial(x)
        trunk_features = self.trunk(initial_features)
        return initial_features + trunk_features

class RefinementStage(nn.Module):
    def __init__(self, in_channels, out_channels, num_heatmaps, num_pafs):
        super().__init__()
        self.trunk = nn.Sequential(
            RefinementStageBlock(in_channels, out_channels),
            RefinementStageBlock(out_channels, out_channels),
            RefinementStageBlock(out_channels, out_channels),
            RefinementStageBlock(out_channels, out_channels),
            RefinementStageBlock(out_channels, out_channels)
        )
        self.heatmaps = nn.Sequential(
            conv(out_channels, out_channels, kernel_size=1, padding=0, bn=False),
            conv(out_channels, num_heatmaps, kernel_size=1, padding=0, bn=False, relu=False)
        )
        self.pafs = nn.Sequential(
            conv(out_channels, out_channels, kernel_size=1, padding=0, bn=False),
            conv(out_channels, num_pafs, kernel_size=1, padding=0, bn=False, relu=False)
        ) if num_pafs > 0 else None

    def forward(self, x):
        trunk_features = self.trunk(x)
        heatmaps = self.heatmaps(trunk_features)
        if self.pafs is not None:
            pafs = self.pafs(trunk_features)
            return [heatmaps, pafs]
        else:
            return [heatmaps]


class ShuffleNetv2Keypointv2(nn.Module):
    def __init__(self, num_keypoint_classes, num_pafs, num_refinement_stages=1, pretrain=True):
        super(ShuffleNetv2Keypointv2, self).__init__()
        self.backbone = ShuffleNetV2(
            model_size='1.0x',
            out_stages=[2, 3, 4],
            activation='LeakyReLU',
            with_last_conv=False,
            pretrain=pretrain
        )
        self.neck = PAN(
            in_channels=[116, 232, 464],
            out_channels=128,
            num_outs=3,
            activation='lrelu',
        )

        num_heatmaps = num_keypoint_classes
        num_pafs = 2 * num_pafs
        self.initial_stage = InitialStage(num_channels=128, num_heatmaps=num_heatmaps, num_pafs=num_pafs)
        self.refinement_stages = nn.ModuleList()
        for idx in range(num_refinement_stages):
            self.refinement_stages.append(
                RefinementStage(128 + num_heatmaps + num_pafs, 128,  num_heatmaps, num_pafs)
            )
        self.num_pafs = num_pafs

    def forward(self, x):
        x = self.backbone(x)
        x = self.neck(x)

        backbone_features = x[0]
        stages_output = self.initial_stage(backbone_features)
        for refinement_stage in self.refinement_stages:
            if self.num_pafs > 0:
                stages_output.extend(
                    refinement_stage(torch.cat([backbone_features, stages_output[-2], stages_output[-1]], dim=1))
                )
            else:
                stages_output.extend(
                    refinement_stage(torch.cat([backbone_features, stages_output[0]], dim=1))
                )
        if not self.training and self.num_pafs > 0:
            stages_output = [o for i, o in enumerate(stages_output) if i%2==0]
        return stages_output


if __name__ == '__main__':
    model = ShuffleNetv2Keypointv2(num_keypoint_classes=2, num_pafs=2)
    
    inp = torch.rand(8, 3, 640, 640)
    out = model(inp)