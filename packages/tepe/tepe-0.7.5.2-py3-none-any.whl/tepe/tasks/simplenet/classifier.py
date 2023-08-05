from torch import nn


class Classifier(nn.Module):
    def __init__(self,
                 backbone=None):
        super().__init__()
        self.backbone = backbone
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, inputs, targets=None):
        outputs = self.backbone(inputs)
        if self.training:
            loss = self.loss_fn(outputs, targets)
            return {'loss': loss}

        return outputs

    def init_weights(self):
        for n, m in self.named_modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)
