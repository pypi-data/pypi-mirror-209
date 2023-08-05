"""
Ref doc: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html#convnet-as-fixed-feature-extractor
         https://paddleclas.readthedocs.io/zh_CN/latest/models/Tricks.html
"""
from tepe.modules.backbone import resnet
from tepe.core import BaseTask, register_config


MODEL_DICT = {
    'resnet18': resnet.resnet18,
    'resnet34': resnet.resnet34,
    'resnet50': resnet.resnet50,
    'resnet101': resnet.resnet101,
    'resnet152': resnet.resnet152,
    'resnext50': resnet.resnext50_32x4d,
    'resnext101': resnet.resnext101_32x8d,
    'resnet_wide50': resnet.wide_resnet50_2,
    'resnet_wide101': resnet.wide_resnet101_2,
}


@register_config('resnet')
class ResNetConfig(BaseTask):
    def __init__(self):
        super().__init__()
        self.task_name = 'resnet'
        self.model_type = 'resnet18'

        self.data_root = None
        self.CLASS = ('', )
        self.num_classes = 1000
        self.input_size = (224, 224)

        self.batch_size = 128  # 每次迭代时，输入进网络中图像的数量
        self.basic_lr_per_img = 0.001 / 256  # 每张图像对应的学习率，此值为pretrained=True, 或者数据量<1000时的默认值
                                             # 如果是从头开始训练，需要增大此值，参考ImageNet的值：0.1/256
                                             # 最终的学习率learning_rate = self.batch_size * self.basic_lr_per_img
        self.max_epoch = 100  # 数据集被训练的最多轮数
        self.optimizer_type = 'sgd'
        self.momentum = 0.9  # 优化器中的动量因子，一般不修改
        self.weight_decay = 1e-4  # 数据集复杂、数据增广多的话，适当减少该值

        self.resume = False  # 是否接着上次checkpoint继续训练，为True时需要指定self.ckpt的路径
        self.pretrained = True  # 是否载入预训练模型
        self.freeze_feature_extractor = False  # 是否固定住backbone中的参数，为True时backbone中的参数在训练时不再被更新

        self.label_smoothing = False  # 一种正则化方法，resnet50以上的模型有一定的提升效果

        # lr scheduler args
        self.scheduler_type = 'step'  # LR scheduler
        self.lr_noise = None  # learning rate noise on/off epoch percentages
        self.lr_noise_pct = 0.67  # learning rate noise limit percent (default: 0.67)
        self.lr_noise_std = 1.  # learning rate noise std-dev (default: 1.0)
        self.lr_cycle_mul = 1.  # learning rate cycle len multiplier (default: 1.0)
        self.lr_cycle_decay = 0.1  # amount to decay each learning rate cycle (default: 0.5)
        self.lr_cycle_limit = 1  # learning rate cycle limit, cycles enabled if > 1
        self.lr_k_decay = 1.0
        self.min_lr = 1e-6
        self.decay_epochs = 100  # epoch interval to decay LR
        self.decay_milestones = []
        self.decay_rate = 0.1  # LR decay rate (default: 0.1)
        self.warmup_lr = 0.0001
        self.warmup_epochs = 3  # epochs to warmup LR, if scheduler supports
        self.cooldown_epochs = 10  # epochs to cooldown LR at min_lr, after cyclic schedule ends
        self.patience_epochs = 10  # patience epochs for Plateau LR scheduler (default: 10)
        self.step_on_epochs = True
        
    def get_model(self, train=True):
        from torch.nn import Linear

        model = MODEL_DICT[self.model_type](pretrained=self.pretrained)
        num_ftrs = model.fc.in_features
        # Here the size of each output sample is set to 2.
        # Alternatively, it can be generalized to nn.Linear(num_ftrs, len(class_names)).
        model.fc = Linear(num_ftrs, self.num_classes)

        if train:
            if self.freeze_feature_extractor:
                for param in model.parameters():
                    param.requires_grad = False
                # update params
                self.params = model.classifier.parameters()
            else:
                # update params
                self.params = model.parameters()
        else:
            self.load_ckpt(model, self.weights, self.device, load_keys='model')

        self.model = model

        return self.model

    def get_train_loader(self):
        from torch.utils.data import DataLoader
        from torchvision.transforms import transforms
        from ...data.datasets.cls_datasets import CustomClsDataset
        from ...data.utils import IMAGENET_DEFAULT_STD, IMAGENET_DEFAULT_MEAN

        transform = transforms.Compose([
            transforms.RandomResizedCrop(self.input_size),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_DEFAULT_MEAN,
                                 std=IMAGENET_DEFAULT_STD)
        ])

        train_dataset = CustomClsDataset(
            self.data_root,
            self.CLASS,
            image_sets=['train'],
            transform=transform,
            is_train=True
        )
        workers = 4
        self.train_loader = DataLoader(
            train_dataset, batch_size=self.batch_size, shuffle=True,
            num_workers=workers, worker_init_fn=None, pin_memory=True,
            sampler=None, collate_fn=None)

        return self.train_loader

    def get_eval_loader(self):
        from torch.utils.data import DataLoader
        from torchvision.transforms import transforms
        from ...data.datasets.cls_datasets import CustomClsDataset
        from ...data.utils import IMAGENET_DEFAULT_STD, IMAGENET_DEFAULT_MEAN

        transform = transforms.Compose([
            transforms.Resize(int(self.input_size[0] / 0.875)),
            transforms.CenterCrop(self.input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_DEFAULT_MEAN,
                                 std=IMAGENET_DEFAULT_STD)
        ])

        val_dataset = CustomClsDataset(
            self.data_root,
            self.CLASS,
            image_sets=['val'],
            transform=transform,
            is_train=False
        )
        workers = 4
        val_loader = DataLoader(
            val_dataset, batch_size=self.batch_size, shuffle=False,
            num_workers=workers, worker_init_fn=None, pin_memory=True,
            sampler=None, collate_fn=None)

        return val_loader

    def get_transform(self, mode='train'):
        import albumentations as A
        from albumentations.pytorch import ToTensorV2
        from tepe.data.utils import IMAGENET_DEFAULT_STD, IMAGENET_DEFAULT_MEAN

        if mode == 'train':
            transform_list = [
                A.Resize(self.input_size[0], self.input_size[1], p=1),
                A.RandomCrop(self.input_size[0], self.input_size[1], p=1),
                A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.4),
                A.GridDistortion(p=0.3),
                A.OneOf([
                    A.HueSaturationValue(p=0.4),
                    A.ChannelShuffle(p=0.5)
                ], p=1),
                A.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD),
                ToTensorV2()
            ]
            transform = A.Compose(transform_list)
        elif mode == 'eval':
            transform_list = [
                A.Resize(self.input_size[0], self.input_size[1], p=1),
                A.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD),
                ToTensorV2()
            ]
            transform = A.Compose(transform_list)
        elif mode == 'predict':
            from torchvision import transforms
            import cv2

            transform = transforms.Compose([
                lambda img : cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
                lambda img : cv2.resize(img, self.input_size, interpolation=cv2.INTER_LINEAR),
                transforms.ToTensor(),
                # transforms.Resize(self.input_size[0]),
                transforms.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD)
            ])
        else:
            raise Exception("mode should be 'train', 'eval' or 'predict'")

        return transform

    def get_loss(self):
        from torch.nn import CrossEntropyLoss

        return CrossEntropyLoss()

    def get_optimizer(self):
        from tepe.modules.optim import create_optimizer_v2

        kwargs = {}
        opt_eps = None  # (float) Optimizer Epsilon
        opt_betas = None  # (float) Optimizer Betas
        if opt_eps is not None:
            kwargs['eps'] = self.opt_eps
        if opt_betas is not None:
            kwargs['betas'] = self.opt_betas

        params = getattr(self, 'params', self.model.parameters())
        self.optimizer = create_optimizer_v2(
            self.model, opt=self.optimizer_type,
            lr=self.learning_rate, weight_decay=self.weight_decay,
            momentum=self.momentum, filter_bias_and_bn=True, **kwargs
        )

        return self.optimizer

    def get_lr_scheduler(self, **kwargs):
        from tepe.modules.scheduler import create_scheduler

        optimizer = getattr(self, 'optimizer', self.get_optimizer())
        lr_scheduler, self.max_epoch = create_scheduler(
            self, sched=self.scheduler_type, optimizer=optimizer)

        return lr_scheduler

    def get_trainer(self):
        return Trainer(self)

    def get_evaluator(self, train=None):
        from tepe.core.evaluator import ClsEvaluator

        model = None if train else self.get_model(train=False)
        val_loader = self.get_eval_loader()
        evaluator = ClsEvaluator(
            model=model,
            dataloader=val_loader,
            img_size=self.input_size,
            num_classes=self.num_classes,
            training=train,
            save_dir=self.output_dir
        )
        return evaluator

    def get_predictor(self):
        from pathlib import Path
        from tepe.core.predictor import ClsPredictor

        model = self.get_model(train=False) if Path(self.weights).suffix == '.pth' else None
        predictor = ClsPredictor(self.input_size, self.CLASS,
                                 model=model, weights=self.weights,
                                 preprocess=self.get_transform(mode='predict'),
                                 save_dir=self.output_dir)
        return predictor


import torch
from tepe.core.base_trainer import Trainer as BaseTrainer


class Trainer(BaseTrainer):
    def __init__(self, task):
        super(Trainer, self).__init__(task)

    def train_one_iter(self, data):
        x, y, _, _ = data
        x = x.to(self.data_type).cuda(non_blocking=True)
        y = y.to(torch.long).cuda(non_blocking=True)
        y.requires_grad = False

        self.optimizer.zero_grad()

        y_pred = self.model(x)
        loss = self.loss_fn(y_pred, y)

        self.scaler.scale(loss).backward()
        self.scaler.step(self.optimizer)
        self.scaler.update()

        return {'loss': loss}