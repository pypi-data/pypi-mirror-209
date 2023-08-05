import os
import torch
import torch.nn as nn


__all__ = ['ShuffleNetv2Keypoint']


def channel_shuffle(x, groups):
    # type: (torch.Tensor, int) -> torch.Tensor
    batchsize, num_channels, height, width = x.data.size()
    channels_per_group = num_channels // groups

    # reshape
    x = x.view(batchsize, groups,
               channels_per_group, height, width)

    x = torch.transpose(x, 1, 2).contiguous()

    # flatten
    x = x.view(batchsize, -1, height, width)

    return x


class InvertedResidual(nn.Module):
    def __init__(self, inp, oup, stride):
        super(InvertedResidual, self).__init__()

        if not (1 <= stride <= 3):
            raise ValueError('illegal stride value')
        self.stride = stride

        branch_features = oup // 2
        assert (self.stride != 1) or (inp == branch_features << 1)

        if self.stride > 1:
            self.branch1 = nn.Sequential(
                self.depthwise_conv(inp, inp, kernel_size=3, stride=self.stride, padding=1),
                nn.BatchNorm2d(inp),
                nn.Conv2d(inp, branch_features, kernel_size=1, stride=1, padding=0, bias=False),
                nn.BatchNorm2d(branch_features),
                nn.ReLU(inplace=True),
            )
        else:
            self.branch1 = nn.Sequential()

        self.branch2 = nn.Sequential(
            nn.Conv2d(inp if (self.stride > 1) else branch_features,
                      branch_features, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(branch_features),
            nn.ReLU(inplace=True),
            self.depthwise_conv(branch_features, branch_features, kernel_size=3, stride=self.stride, padding=1),
            nn.BatchNorm2d(branch_features),
            nn.Conv2d(branch_features, branch_features, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(branch_features),
            nn.ReLU(inplace=True),
        )

    @staticmethod
    def depthwise_conv(i, o, kernel_size, stride=1, padding=0, bias=False):
        return nn.Conv2d(i, o, kernel_size, stride, padding, bias=bias, groups=i)

    def forward(self, x):
        if self.stride == 1:
            x1, x2 = x.chunk(2, dim=1)
            out = torch.cat((x1, self.branch2(x2)), dim=1)
        else:
            out = torch.cat((self.branch1(x), self.branch2(x)), dim=1)

        out = channel_shuffle(out, 2)

        return out


class ComputeLoss(nn.Module):
    def __init__(self, class_weights=None):
        super(ComputeLoss, self).__init__()
        self.loss_func = torch.nn.MSELoss(size_average=None, reduce=None, reduction='sum')
        self.class_weights = class_weights

    def __call__(self, preds, data):
        labels = data['target']
        kp_num = int(preds.shape[1])
        if self.class_weights:
            assert kp_num == len(self.class_weights), "class_weights's length == num_keypoints"
        else:
            self.class_weights = [1] * kp_num

        losses = []
        loss_total = 0
        for i in range(kp_num):
            pred = preds[:, i, :, :]
            label = labels[:, i, :, :]
            pos_mask = label > 0
            neg_mask = label == 0

            loss_pos = self.loss_func(pred[pos_mask], label[pos_mask]) / labels.shape[0]
            loss_neg = self.loss_func(pred[neg_mask], label[neg_mask]) / labels.shape[0]
            loss = loss_pos + 0.05 * loss_neg
            loss *= self.class_weights[i]
            loss_total += loss

            losses.append(loss)

        loss_dict = {'loss': loss_total}
        loss_dict.update({f'loss_{i}': v for i, v in enumerate(losses)})
        # loss_dict.update({f'loss_neg_{i}': v for i, v in enumerate(neg_losses)})

        return loss_dict


class FocalLoss(nn.Module):
    def __init__(self, weight=None, reduction='mean', gamma=0, eps=1e-7):
        super(FocalLoss, self).__init__()
        self.gamma = gamma
        self.eps = eps
        self.ce = torch.nn.CrossEntropyLoss(weight=weight, reduction=reduction)

    def forward(self, input, target):
        logp = self.ce(input, target)
        p = torch.exp(-logp)
        loss = (1 - p) ** self.gamma * logp
        return loss.mean()


class DUC(nn.Module):
    '''
    Initialize: inplanes, planes, upscale_factor
    OUTPUT: (planes // upscale_factor^2) * ht * wd
    '''

    def __init__(self, inplanes, planes, upscale_factor=2):
        super(DUC, self).__init__()
        self.conv = nn.Conv2d(
            inplanes, planes, kernel_size=3, padding=1, bias=False)
        self.bn = nn.BatchNorm2d(planes, momentum=0.1)
        self.relu = nn.ReLU(inplace=True)
        self.pixel_shuffle = nn.PixelShuffle(upscale_factor)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        x = self.pixel_shuffle(x)
        return x

class ShuffleNetv2Keypoint(nn.Module):
    def __init__(self, num_keypoint, channel_ratio):
        super(ShuffleNetv2Keypoint, self).__init__()

        self.kp_num = num_keypoint
        width_mult = channel_ratio
        inverted_residual=InvertedResidual

        if width_mult == 0.5:
            stages_repeats = [4, 8, 4]
            stages_out_channels = [24, 48, 96, 192, 1024]
        elif width_mult == 1.0:
            stages_repeats = [4, 8, 4]
            stages_out_channels = [24, 116, 232, 464, 1024]
        elif width_mult == 1.5:
            stages_repeats = [4, 8, 4]
            stages_out_channels = [24, 176, 352, 704, 1024]
        elif width_mult == 2.0:
            stages_repeats = [4, 8, 4]
            stages_out_channels = [24, 244, 488, 976, 2048]
        elif width_mult == 0.25:
            stages_repeats = [4, 8, 4]
            stages_out_channels = [24, 28, 48, 96, 512]
        else:
            assert(False)


        if len(stages_repeats) != 3:
            raise ValueError('expected stages_repeats as list of 3 positive ints')
        if len(stages_out_channels) != 5:
            raise ValueError('expected stages_out_channels as list of 5 positive ints')
        self._stage_out_channels = stages_out_channels

        input_channels = 3
        output_channels = self._stage_out_channels[0]
        self.conv1 = nn.Sequential(
            nn.Conv2d(input_channels, output_channels, 3, 2, 1, bias=False),
            nn.BatchNorm2d(output_channels),
            nn.ReLU(inplace=True),
        )
        input_channels = output_channels

        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        stage_names = ['stage{}'.format(i) for i in [2, 3, 4]]
        for name, repeats, output_channels in zip(
                stage_names, stages_repeats, self._stage_out_channels[1:]):
            seq = [inverted_residual(input_channels, output_channels, 2)]
            for i in range(repeats - 1):
                seq.append(inverted_residual(output_channels, output_channels, 1))
            setattr(self, name, nn.Sequential(*seq))
            input_channels = output_channels

        output_channels = self._stage_out_channels[-1]

        self.conv5 = nn.Sequential(
            nn.Conv2d(input_channels, output_channels, 1, 1, 0, bias=False),
            nn.BatchNorm2d(output_channels),
            nn.ReLU(inplace=True),
        )

        self.conv_compress = nn.Conv2d(1024, 256, 1, 1, 0, bias=False)
        self.duc1 = DUC(256, 512, upscale_factor=2)
        self.duc2 = DUC(128, 256, upscale_factor=2)
        #self.duc3 = DUC(64, 128, upscale_factor=2)
        self.conv_result = nn.Conv2d(64, self.kp_num , 1, 1, 0, bias=False)


    def _forward_impl(self, x):
        # See note [TorchScript super()]
        x = self.conv1(x)  # [B, 24, 112, 112]
        x = self.maxpool(x)  # [B, 24, 56, 56]
        x = self.stage2(x)  # [B, 116, 28, 28]
        x = self.stage3(x)  # [B, 232, 14, 14]
        x = self.stage4(x)  # [B, 464, 7, 7]
        x = self.conv5(x)  # [B, 1024, 7, 7]
        x = self.conv_compress(x)  # [B, 256, 7, 7]
        x = self.duc1(x)  # [B, 128, 14, 14]
        x = self.duc2(x)  # [b, 64, 28, 28]
        #x = self.duc3(x)
        x = self.conv_result(x)  # [b, num_kp, 28, 28]
        return x

    def forward(self, x):
        x = self._forward_impl(x)
        # x = nn.functional.sigmoid(x)
        return x.sigmoid()
        # if self.training:
        #     return x
        # else:
        #     heatmaps = nn.functional.sigmoid(x)
        #     return heatmaps


if __name__ == '__main__':
    model = ShuffleNetv2Keypoint(2, 1.0)
    
    inp = torch.rand(8, 3, 224, 224)
    out = model(inp)
    