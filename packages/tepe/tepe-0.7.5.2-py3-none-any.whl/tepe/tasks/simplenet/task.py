import os
import torch
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from tepe.core import BaseTask, register_config


@register_config('simplenet')
class SimplenetConfig(BaseTask):
    def __init__(self):
        super(SimplenetConfig, self).__init__()
        self.task_name = 'simplenet'
        self.CLASS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.num_classes = 10
        self.input_size = (32, 32)  # (H, W)
        self.device = 0

        self.model_type = 's'

        self.data_root = ''

        # --------------  training config -------------- #
        self.batch_size = 128
        self.max_epoch = 300
        self.basic_lr_per_img = 0.001 / 128
        self.scheduler = "multistep"
        self.milestones = [30, 60, 90, 120, 150, 180]
        self.ema = True

    def get_model(self, train=False, **kwargs):
        from .classifier import Classifier
        from tepe.modules.backbone import SimpleNet, SimpleNetM, SimpleNetL

        if self.model_type == 's':
            backbone = SimpleNet(self.num_classes) 
        elif self.model_type == 'm':
            backbone = SimpleNetM(self.num_classes) 
        elif self.model_type == 'l':
            backbone = SimpleNetL(self.num_classes) 
        else:
            raise Exception("model type should be 's', 'm' or 'l'")
        model = Classifier(backbone=backbone)

        if not train:
            assert self.weights, 'weights path is None'
            if os.path.splitext(self.weights)[-1] in ['.pt', '.pth']:
                self.load_ckpt(model, self.weights, device=self.device, load_keys='model')
                model.eval()

        self.model = model
        return self.model

    def get_train_loader(self):
        from ...data.datasets import CustomClsDataset

        # with wait_for_the_master():
        train_set = CustomClsDataset(
            self.data_root,
            self.CLASS,
            image_sets=['train'],
            transform=self.get_transform(mode='train'),
            is_train=True
        )

        # Create a loder for the training set
        self.train_loader = DataLoader(train_set, batch_size=self.batch_size, shuffle=True, num_workers=4)

        return self.train_loader

    def get_eval_loader(self):

        from ...data.datasets import CustomClsDataset

        test_set = CustomClsDataset(
            self.data_root,
            self.CLASS,
            image_sets=['val'],
            transform=self.get_transform(mode='eval'),
            is_train=False
        )

        # Create a loder for the test set, note that both shuffle is set to false for the test loader
        test_loader = DataLoader(test_set, batch_size=self.batch_size, shuffle=False, num_workers=4)

        return test_loader

    def get_transform(self, mode='train'):
        if mode == 'train':
            transform = transforms.Compose([
                # transforms.RandomHorizontalFlip(),
                transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
                transforms.RandomAffine((-6, 6), (0.08, 0.03)),
                # transforms.RandomCrop(32,padding=4),
                # lambda img: cv2.resize(img, self.input_size, interpolation=cv2.INTER_LINEAR),
                transforms.Resize(self.input_size),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
        elif mode == 'eval':
            transform = transforms.Compose([
                transforms.Resize(self.input_size),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
        else:
            import cv2

            transform = transforms.Compose([
                lambda img: cv2.resize(img, self.input_size, interpolation=cv2.INTER_LINEAR),
                lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
        return transform

    def get_optimizer(self) -> torch.optim.Optimizer:
        from torch.optim import Adam

        optimizer = Adam(self.model.parameters(), lr=self.learning_rate, weight_decay=0.005)
        return optimizer

    def get_lr_scheduler(self):
        from ...modules.utils.scheduler import LRScheduler

        scheduler = LRScheduler(
            name=self.scheduler,
            lr=self.learning_rate,
            iters_per_epoch=len(self.train_loader),
            total_epochs=self.max_epoch,
            milestones=self.milestones
        )

        return scheduler

    def get_trainer(self):
        from ...core.trainer import ClsTrainer as Trainer

        return Trainer(self)

    def get_evaluator(self, train=False):
        from ...core.evaluator import ClsEvaluator

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
        from ...core.predictor import ClsPredictor

        model = self.get_model(train=False) if Path(self.weights).suffix == '.pth' else None
        predictor = ClsPredictor(self.input_size, self.CLASS, 
                                 model=model, weights=self.weights,
                                 preprocess=self.get_transform(mode='predict'),
                                 save_dir=self.output_dir)
        return predictor