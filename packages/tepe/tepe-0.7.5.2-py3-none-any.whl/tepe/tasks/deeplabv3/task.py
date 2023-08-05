from typing import Literal, Union, Callable, Tuple
from tepe.core import BaseTask, register_config
from tepe.data.utils import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
from tepe.tasks.deeplabv3 import create_model


MODEL_DICT = {
    'deeplabv3_mobilenet': create_model.deeplabv3_mobilenet,
    'deeplabv3_resnet50': create_model.deeplabv3_resnet50,
    'deeplabv3_resnet101': create_model.deeplabv3_resnet50,
    'deeplabv3plus_mobilenet': create_model.deeplabv3plus_mobilenet,
    'deeplabv3plus_resnet50': create_model.deeplabv3plus_resnet50,
    'deeplabv3plus_resnet101': create_model.deeplabv3plus_resnet50,
}


@register_config('deeplabv3')
class DeeplabV3Config(BaseTask):
    def __init__(self):
        super(DeeplabV3Config, self).__init__()
        self.task_name = 'deeplabv3'
        self.CLASS = (
            'sky', 'building', 'pole', 'road', 'pavement',
            'tree', 'signsymbol', 'fence', 'car',
            'pedestrian', 'bicyclist', 'unlabelled')
        self.num_classes = 12
        self.input_size = (512, 512)
        self.model_type = 'deeplabv3plus_mobilenetv2'
        self.stride = 8  # 8 or 16

        self.device = 0

        self.data_root = '/home/zepei/DATA/CamVid'

        self.basic_lr_per_img = 0.01 / 16
        self.batch_size = 16
        self.max_epoch = 300

        self.loss_type = 'cross_entropy'  # 'focal_loss'
        self.lr_policy = 'poly'  # 'step'
        self.ema = True

    def get_model(self, train=False):

        model = MODEL_DICT[self.model_type](
            num_classes=self.num_classes,
            output_stride=self.stride,
            pretrained_backbone=True
        )
        if train:
            from .utils import set_bn_momentum
            set_bn_momentum(model.backbone, momentum=0.01)
        else:
            self.load_ckpt(model, self.weights, load_keys='model')

        self.model = model
        return self.model

    def get_train_loader(self):
        from torch.utils.data import DataLoader
        from tepe.data.datasets.seg_voc_custom import VOCSegmentation

        train_transform = self.get_transform(mode='train')
        train_dataset = VOCSegmentation(
            root=self.data_root,  image_set='train',
            download=False, transform=train_transform)
        self.train_loader = DataLoader(
            train_dataset, batch_size=self.batch_size, shuffle=True,
            num_workers=4, drop_last=True
        )
        return self.train_loader

    def get_eval_loader(self):
        from torch.utils.data import DataLoader
        from tepe.data.datasets.seg_voc_custom import VOCSegmentation

        val_transform = self.get_transform(mode='val')
        valid_dataset = VOCSegmentation(
            root=self.data_root, image_set='val',
            download=False, transform=val_transform)
        valid_loader = DataLoader(
            valid_dataset, batch_size=self.batch_size, shuffle=False, num_workers=2)
        return valid_loader

    def get_transform(
            self,
            mode: Literal['train', 'val', 'test'] = 'train'
    ) -> Union[None, Union[Callable, Tuple[Callable, ...]]]:
        # return self._get_albu_transform(mode)
        return self._get_torch_transform(mode)

    def _get_torch_transform(self, mode):
        from tepe.data.augments import seg_augment as sa
        if mode == 'train':

            return sa.ExtCompose([
                sa.ExtResize(size=self.input_size),
                # sa.ExtRandomScale((0.5, 2.0)),
                sa.ExtRandomCrop(size=self.input_size, pad_if_needed=True),
                sa.ExtRandomHorizontalFlip(),
                sa.ExtColorJitter(brightness=0.2,  # 亮度
                                  contrast=0,  # 对比度
                                  saturation=0,  # 饱和度
                                  hue=0.1),   # 色调
                sa.ExtToTensor(),
                sa.ExtNormalize(mean=IMAGENET_DEFAULT_MEAN,
                                std=IMAGENET_DEFAULT_STD),
            ])
        elif mode == 'val':
            return sa.ExtCompose([
                sa.ExtResize(self.input_size),
                # sa.ExtCenterCrop(self.input_size),
                sa.ExtToTensor(),
                sa.ExtNormalize(mean=IMAGENET_DEFAULT_MEAN,
                                std=IMAGENET_DEFAULT_STD),
            ])

    def _get_albu_transform(self, mode='train'):
        import albumentations as albu

        if mode == 'train':
            train_transform = [
                albu.Resize(self.input_size[0], self.input_size[1], p=1),
                albu.RandomCrop(
                    self.input_size[0], self.input_size[1], p=1
                ),
                albu.RandomBrightnessContrast(
                    brightness_limit=0.2, contrast_limit=0.2, p=0.4
                ),
                albu.Rotate(limit=30, p=1),
                # albu.GridDistortion(p=0.3),
                albu.HueSaturationValue(p=0.4),
                albu.HorizontalFlip(p=0.3),
                albu.Normalize(mean=IMAGENET_DEFAULT_MEAN,
                               std=IMAGENET_DEFAULT_STD,
                               max_pixel_value=255.)
            ]
            train_transform = albu.Compose(train_transform)
            return train_transform
        else:
            val_transform = [
                albu.Resize(self.input_size[0], self.input_size[1], p=1),
                albu.Normalize(mean=IMAGENET_DEFAULT_MEAN,
                               std=IMAGENET_DEFAULT_STD,
                               max_pixel_value=255.)
            ]
            val_transform = albu.Compose(val_transform)
            return val_transform

    def get_optimizer(self):
        from torch.optim import SGD

        self.optimizer = SGD(params=[
            {'params': self.model.backbone.parameters(), 'lr': 0.1 *
             self.learning_rate},
            {'params': self.model.classifier.parameters(), 'lr': self.learning_rate},
        ], lr=self.learning_rate, momentum=0.9, weight_decay=1e-4)

        return self.optimizer

    def get_lr_scheduler(self):
        from torch.optim.lr_scheduler import StepLR
        step_size = 1000
        scheduler = StepLR(self.optimizer, step_size=step_size, gamma=0.1)

        return scheduler

    def get_loss(self):
        if self.loss_type == 'focal_loss':
            from tepe.modules.loss import FocalLoss
            criterion = FocalLoss(ignore_index=255, size_average=True)
        elif self.loss_type == 'cross_entropy':
            from torch.nn import CrossEntropyLoss
            criterion = CrossEntropyLoss(ignore_index=255, reduction='mean')
        return criterion

    def get_evaluator(self, train=False):
        from tepe.core.evaluator import SegEvaluator

        val_loader = self.get_eval_loader()
        evaluator = SegEvaluator(
            dataloader=val_loader,
            img_size=self.input_size,
            num_classes=self.num_classes,
            device=self.device,
            training=train,
            save_dir=self.output_dir
        )
        return evaluator

    def train(self):
        from tepe.core.trainer import SegTrainer as Trainer
        from tepe.utils.general import init_seeds

        init_seeds()

        trainer = Trainer(self)
        trainer.train()

    def eval(self):
        evaluator = self.get_evaluator(train=False)
        model = self.get_model(train=False)
        evaluator.evaluate(model=model)

    def get_predictor(self):          
        from pathlib import Path
        import cv2
        from tepe.core.predictor import SegPredictor
        
        assert Path(self.weights).exists()
        model = self.get_model(train=False) if Path(self.weights).suffix == '.pth' \
            else cv2.dnn.readNet(self.weights)
        self.predictor = SegPredictor(
            input_size=self.input_size, classes=self.CLASS,
            model=model, device=0,
            save_dir=self.output_dir
        )
        return self.predictor

    def predict(self, source, view_img=True, save_img=True):
        from tepe.core.predictor import SegPredictor
        if 'predictor' not in self.__dict__:
            self.predictor = self.get_predictor()
        self.predictor.predict(source, view_img, save_img)
