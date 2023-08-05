import torch
import torch.nn as nn
from einops import rearrange
from tqdm import tqdm
from sklearn.cluster import KMeans
import torch.nn.functional as F
from torchvision.models.feature_extraction import create_feature_extractor


class CFA(nn.Module):
    def __init__(self, autoencoder):
        super().__init__()
        self.feature_extractor = create_feature_extractor(
            autoencoder, return_nodes={'encoder.layer1': 'feat1',
                                       'encoder.layer2': 'feat2',
                                       'encoder.layer3': 'feat3'}
        )


    def forward(self, x):
        pass


class DSVDD(nn.Module):

    def __init__(self, cnn, gamma_c, gamma_d, device, feature_act=False):
        super(DSVDD, self).__init__()
        self.export = False
        self.device = device

        self.C   = 0
        self.nu = 1e-3
        self.scale = [1, 1]

        self.gamma_c = gamma_c
        self.gamma_d = gamma_d
        self.alpha = 1e-1
        self.K = 3
        self.J = 3

        self.r   = nn.Parameter(1e-5*torch.ones(1), requires_grad=True)
        self.Descriptor = Descriptor(self.gamma_d, cnn).to(device)
        self.leaky = feature_act

    def forward(self, feats):
        if self.leaky:
            p = []
            for v in feats.values():
                p.append(F.leaky_relu(v))
        else:
            p = feats

        if self.export:
            return self.forward_export(p)
        phi_p = self.Descriptor(p)
        phi_p = rearrange(phi_p, 'b c h w -> b (h w) c')

        features = torch.sum(torch.pow(phi_p, 2), 2, keepdim=True)
        centers  = torch.sum(torch.pow(self.C, 2), 0, keepdim=True)
        f_c      = 2 * torch.matmul(phi_p, (self.C))
        dist     = features + centers
        dist     = dist - f_c
        dist     = torch.sqrt(dist)

        n_neighbors = self.K
        dist     = dist.topk(n_neighbors, largest=False).values

        dist = (F.softmin(dist, dim=-1)[:, :, 0]) * dist[:, :, 0]
        dist = dist.unsqueeze(-1)

        score = rearrange(dist, 'b (h w) c -> b c h w', h=self.scale[0], w=self.scale[1])

        loss = 0
        if self.training:
            loss = self._soft_boundary(phi_p)

        return loss, score

    def forward_export(self, p):
        phi_p = self.Descriptor(p)

        phi_p = rearrange(phi_p, 'b c h w -> b (h w) c')

        features = torch.sum(torch.pow(phi_p, 2), 2, keepdim=True)
        centers  = torch.sum(torch.pow(self.C, 2), 0, keepdim=True)
        f_c      = 2 * torch.matmul(phi_p, (self.C))
        # print(features.shape)
        # features = torch.repeat_interleave(features, 3136, 2)
        # centers = torch.repeat_interleave(centers.unsqueeze(1), 3136, 1)
        dist     = features + centers
        dist     = dist - f_c
        dist     = torch.sqrt(dist)

        n_neighbors = self.K
        dist     = dist.topk(n_neighbors, largest=False).values

        dist = (F.softmin(dist, dim=-1)[:, :, 0]) * dist[:, :, 0]
        dist = dist.unsqueeze(-1)

        score = rearrange(dist, 'b (h w) c -> b c h w', h=self.scale[0], w=self.scale[1])

        # return dist, f_c
        return score

    def _soft_boundary(self, phi_p):
        features = torch.sum(torch.pow(phi_p, 2), 2, keepdim=True)
        centers  = torch.sum(torch.pow(self.C, 2), 0, keepdim=True)
        f_c      = 2 * torch.matmul(phi_p, (self.C))
        dist     = features + centers - f_c
        n_neighbors = self.K + self.J
        dist     = dist.topk(n_neighbors, largest=False).values

        score = (dist[:, : , :self.K] - self.r**2) 
        L_att = (1/self.nu) * torch.mean(torch.max(torch.zeros_like(score), score))
        
        score = (self.r**2 - dist[:, : , self.J:]) 
        L_rep  = (1/self.nu) * torch.mean(torch.max(torch.zeros_like(score), score - self.alpha))
        
        loss = L_att + L_rep

        return loss 

    def init_centroid(self, model, data_loader):
        for i, (x, _, _) in enumerate(tqdm(data_loader)):
            x = x.to(self.device)
            feats = model(x)
            if self.leaky:
                p = []
                for v in feats.values():
                    p.append(F.leaky_relu(v))
            else:
                p = feats

            self.scale = [p[0].size(2), p[0].size(3)]
            phi_p = self.Descriptor(p)
            self.C = ((self.C * i) + torch.mean(phi_p, dim=0, keepdim=True).detach()) / (i+1)

        self.C = rearrange(self.C, 'b c h w -> (b h w) c').detach()

        if self.gamma_c > 1:
            self.C = self.C.cpu().detach().numpy()
            self.C = KMeans(n_clusters=(self.scale[0] * self.scale[1])//self.gamma_c, max_iter=3000). \
                fit(self.C).cluster_centers_
            self.C = torch.Tensor(self.C).to(self.device)

        self.C = self.C.transpose(-1, -2).detach()
        self.C = nn.Parameter(self.C, requires_grad=False)


class Descriptor(nn.Module):
    def __init__(self, gamma_d, cnn):
        super(Descriptor, self).__init__()
        self.cnn = cnn
        if cnn == 'wrn50_2':
            dim = 1792 
            self.layer = CoordConv2d(dim, dim//gamma_d, 1)
        elif cnn == 'res18':
            dim = 448
            self.layer = CoordConv2d(dim, dim//gamma_d, 1)
        elif cnn == 'effnet-b5':
            dim = 568
            self.layer = CoordConv2d(dim, 2*dim//gamma_d, 1)
        elif cnn == 'vgg19':
            dim = 1280 
            self.layer = CoordConv2d(dim, dim//gamma_d, 1)
        else:
            raise RuntimeError(f'dont match cnn: {cnn}')
        

    def forward(self, p):
        sample = None
        for o in p:
            o = F.avg_pool2d(o, 3, 1, 1) / o.size(1) if self.cnn == 'effnet-b5' else F.avg_pool2d(o, 3, 1, 1)
            sample = o if sample is None else torch.cat(
                (sample, F.interpolate(o, [sample.size(2), sample.size(3)], mode='bilinear', align_corners=False)),
                dim=1
            )
        
        phi_p = self.layer(sample)
        return phi_p


class CoordConv2d(nn.Conv2d):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1,
                 padding=0, dilation=1, groups=1, bias=True, with_r=False, use_cuda=True):
        super(CoordConv2d, self).__init__(in_channels, out_channels, kernel_size,
                                          stride, padding, dilation, groups, bias)
        self.rank = 2
        self.addcoords = AddCoords(self.rank, with_r, use_cuda=use_cuda)
        self.conv = nn.Conv2d(in_channels + self.rank + int(with_r), out_channels,
                              kernel_size, stride, padding, dilation, groups, bias)

    def forward(self, input_tensor):
        out = self.addcoords(input_tensor)
        out = self.conv(out)

        return out


class AddCoords(nn.Module):
    def __init__(self, rank, with_r=False, use_cuda=True):
        super(AddCoords, self).__init__()
        self.rank = rank
        self.with_r = with_r
        self.use_cuda = use_cuda

    def forward(self, input_tensor):
        batch_size_shape, _, dim_y, dim_x = input_tensor.shape
        xx_ones = torch.ones([1, 1, 1, dim_x], dtype=torch.int32)
        yy_ones = torch.ones([1, 1, 1, dim_y], dtype=torch.int32)

        xx_range = torch.arange(dim_y, dtype=torch.int32)
        yy_range = torch.arange(dim_x, dtype=torch.int32)
        xx_range = xx_range[None, None, :, None]
        yy_range = yy_range[None, None, :, None]

        xx_channel = torch.matmul(xx_range, xx_ones)
        yy_channel = torch.matmul(yy_range, yy_ones)

        yy_channel = yy_channel.permute(0, 1, 3, 2)

        xx_channel = xx_channel.float() / (dim_y - 1)
        yy_channel = yy_channel.float() / (dim_x - 1)

        xx_channel = xx_channel * 2 - 1
        yy_channel = yy_channel * 2 - 1

        xx_channel = xx_channel.repeat(batch_size_shape, 1, 1, 1)
        yy_channel = yy_channel.repeat(batch_size_shape, 1, 1, 1)

        if torch.cuda.is_available and self.use_cuda:
            input_tensor = input_tensor.cuda()
            xx_channel = xx_channel.cuda()
            yy_channel = yy_channel.cuda()
        out = torch.cat([input_tensor, xx_channel, yy_channel], dim=1)

        if self.with_r:
            rr = torch.sqrt(torch.pow(xx_channel - 0.5, 2) + torch.pow(yy_channel - 0.5, 2))
            out = torch.cat([out, rr], dim=1)

        return out