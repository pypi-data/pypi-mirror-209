import addict
from loguru import logger
from tepe.core import BaseTask, register_config
from tepe.utils.general import ROOT


@register_config('shufflenet_line')
class ShufflenetLine(BaseTask):
    def __init__(self):
        super(ShufflenetLine, self).__init__()
        self.task_name = 'shufflenet_line'

        # model config-------------
        self.num_refinement_stages = 1
        self.channel_ratio = 1.0
        self.pretrained = True
        self.only_train = []  # v1 ['conv_compress', 'duc1', 'duc2', 'duc3', 'conv_result']

        # data config--------------
        self.train_img_dir: str = ''
        self.train_ann_dir: str = ''
        self.valid_img_dir: str = ''
        self.valid_ann_dir: str = ''
        self.CLASS = []
        self.class_weights = []
        self.num_line_cls = len(self.CLASS)
        self.batch_size = 32
        self.input_size = [224, 224]
        self.workers = 4

        # train config-------------
        self.max_epoch = 700
        self.basic_lr_per_img = 0.001 / 32
        self.early_stop = False
        self.optimizer_type = 'adam'
        self.momentum = 0.9
        self.weight_decay = 3e-5

        self.scheduler_type = 'multistep'
        self.step_on_epochs = False
        self.decay_epochs = [150, 250, 450, 800]
        self.decay_rate = 0.1  # LR decay rate (default: 0.1)
        self.warmup_lr = 0.0001
        self.warmup_epochs = 3  # epochs to warmup LR, if scheduler supports

        # predict config
        self.line_thr = 0.3

        # export config
        self.opset = None  # default

    def get_model(self, train=True):
        from pathlib import Path
        if Path(self.weights or '').suffix == '.onnx':
            import cv2
            model = cv2.dnn.readNet(self.weights)
            return model

        from tepe.tasks.shufflenet_line.model import ShuffleNetv2Line
        model = ShuffleNetv2Line(num_line_classes=self.num_line_cls, pretrain=True)

        if not train and Path(self.weights).suffix == '.pth':
            self.load_ckpt(model, self.weights, load_keys='model')

        self.model = model
        return self.model

    def get_train_loader(self):
        from torch.utils.data import DataLoader
        from tepe.data.datasets import LineDataset

        transform = self.get_transform(mode='train')
        dataset = LineDataset(self.train_img_dir, self.train_ann_dir, self.num_line_cls,
                              imgsz=self.input_size, transform=transform,
                              class_name=self.CLASS, is_train=True,)

        self.train_loader = DataLoader(dataset, batch_size=self.batch_size,
                                       shuffle=True, num_workers=self.workers)
        return self.train_loader

    def get_eval_loader(self):
        from torch.utils.data import DataLoader
        from tepe.data.datasets import LineDataset

        transform = self.get_transform(mode='eval')
        dataset = LineDataset(self.valid_img_dir, self.valid_ann_dir, self.num_line_cls,
                              imgsz=self.input_size, transform=transform,
                              class_name=self.CLASS, is_train=False,)

        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False,
                                num_workers=self.workers)
        return dataloader

    def get_transform(self, mode='train'):
        import cv2
        import albumentations as A
        from tepe.data.utils import IMAGENET_DEFAULT_STD, IMAGENET_DEFAULT_MEAN

        if mode == 'train':
            transform_list = [
                A.Resize(self.input_size[0], self.input_size[1], p=1),
                A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.4),
                A.Rotate(limit=15, border_mode=cv2.BORDER_REPLICATE, p=0.3),
                A.OneOf([
                    A.HueSaturationValue(p=0.4),
                    A.ChannelShuffle(p=0.5)
                ], p=1),
                A.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD)
            ]
            transform = A.Compose(
                transform_list,
                keypoint_params=A.KeypointParams(format='xy', label_fields=['class_labels'])
            )
        elif mode == 'eval':
            transform_list = [
                A.Resize(self.input_size[0], self.input_size[1], p=1),
                A.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD),
            ]
            transform = A.Compose(
                transform_list,
                keypoint_params=A.KeypointParams(format='xy', label_fields=['class_labels'])
            )
        elif mode == 'predict':
            from torchvision import transforms
            import cv2

            transform = transforms.Compose([
                lambda img : cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
                lambda img : cv2.resize(img, self.input_size, interpolation=cv2.INTER_LINEAR),
                transforms.ToTensor(),
                transforms.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD)
            ])
        else:
            raise Exception("mode should be 'train', 'eval' or 'predict'")

        return transform

    def get_optimizer(self):
        from tepe.modules.optim import create_optimizer_v2
        from tepe.tasks.shufflenet_heatmap.utils import check_only_train

        model = self.model if hasattr(self, 'model') else self.get_model(train=True)
        params = []
        for name, parameter in model.named_parameters():
            if parameter.requires_grad and check_only_train(name, self.only_train):
                if 'bias' in name:
                    params += [{'params': [parameter], 'lr': self.learning_rate, 'weight_decay': 0}]
                else:
                    params += [{'params': [parameter], 'lr': self.learning_rate, 'weight_decay': self.weight_decay}]
            else:
                logger.info("op: %s do not need train" % name)
                parameter.requires_grad = False

        self.optimizer = create_optimizer_v2(
            params, opt=self.optimizer_type,
            lr=self.learning_rate,
            momentum=self.momentum
        )

        return self.optimizer

    def get_lr_scheduler(self, **kwargs):
        from tepe.modules.scheduler import create_scheduler

        optimizer = self.optimizer if hasattr(self, 'optimizer') else self.get_optimizer()
        lr_scheduler, self.max_epoch = create_scheduler(
            self, sched=self.scheduler_type, optimizer=optimizer
        )

        return lr_scheduler

    def get_loss(self):
        from tepe.tasks.shufflenet_line.model import ComputeLoss

        return ComputeLoss(class_weights=self.class_weights)

    def get_trainer(self):
        from tepe.tasks.shufflenet_line.trainer import LineTrainer
        return LineTrainer(self)

    def get_evaluator(self, train=False):
        from tepe.tasks.shufflenet_line.evaluator import Evaluator
        evaluator = Evaluator(
            model=self.get_model(train=train) if not train else None,
            dataloader=self.get_eval_loader(),
            img_size=self.input_size,
            num_classes=self.num_line_cls,
            metrics=self.get_loss(),
            training=train,
            save_dir=self.output_dir
        )
        return evaluator

    def get_predictor(self):
        from pathlib import Path
        from tepe.tasks.shufflenet_line.predictor import LinePredictor

        model = self.get_model(train=False)
        predictor = LinePredictor(
            model=model,
            classes=self.CLASS,
            preprocess=self.get_transform(mode='predict'),
            line_thr=self.line_thr,
            input_size=self.input_size,
            device=self.device,
            dnn=Path(self.weights).suffix == '.onnx',
            save_dir=self.output_dir,
        )
        return predictor