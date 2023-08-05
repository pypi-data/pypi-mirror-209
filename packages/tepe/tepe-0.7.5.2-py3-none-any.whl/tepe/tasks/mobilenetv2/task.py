"""
Ref impl: https://github.com/d-li14/mobilenetv2.pytorch/blob/master/imagenet.py
Ref doc: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html#convnet-as-fixed-feature-extractor
"""

from tepe.core import register_config
from tepe.tasks.resnet import ResNetConfig


@register_config('mobilenetv2')
class MobileNetV2Config(ResNetConfig):
    def __init__(self):
        super().__init__()
        self.data_root = None
        self.task_name = 'mobilenet_v2'
        self.CLASS = ('', )
        self.num_classes = 1000
        self.input_size = (224, 224)
        self.width_mult = 1.  # 1. 0.75 0.5 0.33

        self.batch_size = 64
        self.basic_lr_per_img = 0.1 / 256
        self.max_epoch = 100
        self.optimizer_type = 'rmsprop'
        self.scheduler_type = "multistep"
        self.decay_epochs = [30, 60, 90, 120, 150, 180]
        self.decay_rate = 0.1  # LR decay rate (default: 0.1)
        self.ema = True
        self.weight_decay = 3e-5  # 1e-5~4e-5  值越大，越容易欠拟合，mobilenet相比于resnet等网络需要小点的weight_decay

        self.resume = False
        self.pretrained = True
        self.freeze_feature_extractor = False

    def get_model(self, train=True):
        from torch import nn
        from torchvision.models import mobilenet_v2

        pretrained = self.pretrained if train else False
        model = mobilenet_v2(pretrained=pretrained,
                             width_mult=self.width_mult)

        if train:
            # modify classifier
            linear = nn.Linear(model.last_channel, self.num_classes)
            nn.init.normal_(linear.weight, 0, 0.01)
            nn.init.zeros_(linear.bias)
            model.classifier = nn.Sequential(
                nn.Dropout(0.2),
                linear,
            )

            if self.freeze_feature_extractor:
                for param in model.features.parameters():
                    param.requires_grad = False
        else:
            model.classifier = nn.Sequential(
                nn.Dropout(0.2),
                nn.Linear(model.last_channel, self.num_classes)
            )
            self.load_ckpt(model, self.weights, self.device, load_keys='model')

        self.model = model

        return self.model