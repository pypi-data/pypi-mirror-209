import os
from pathlib import Path
from loguru import logger

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np
import cv2

from tepe.core import BaseTask, register_config
from tepe.data.datasets.public_class_names import coco_classes
from tepe.tasks.yolov5.utils.augmentations import letterbox
from tepe.utils.general import colorstr


@register_config('yolov5')
class YOLOv5Config(BaseTask):
    def __init__(self):
        super(YOLOv5Config, self).__init__()
        self.task_name = 'yolov5'
        self.CLASS = coco_classes
        self.num_classes = 80
        self.include_class_idx = []

        # model config--------------------------------
        self.yolov5_type = 's'
        self.model_cfg = None
        self.input_size = 640
        self.pretrained = True
        self.weights = '.pth'
        self.resume = False
        self.resume_ckpt = ''
        self.freeze_layer = 0  # Number of layers to freeze. backbone=10, all=24

        # dataset config-------------------------------
        self.data_root = ''
        self.cache = True
        self.workers = 4
        self.multi_scale = False
        self.dataset_format = 'yolo'
        self.single_cls = False  # 所有类别视为一类训练

        # training config------------------------------
        self.seed = 0
        self.device = 0
        self.max_epoch = 80
        self.no_aug_epochs = 0
        self.fp16 = False
        self.ema = True
        self.early_stop_patience = 100

        self.linear_lr = False
        self.warmup_lr = 0.1  # warmup initial bias lr
        self.warmup_epochs = 3  # warmup epochs (fractions ok)
        self.basic_lr_per_img = 0.01 / 64.0  # initial learning rate (SGD=1E-2, Adam=1E-3)
        self.adam = False  # True for Adam, False for SGD
        self.scheduler = "yoloxwarmcos"
        self.min_lr_ratio = 0.05
        self.weight_decay = 5e-4
        self.momentum = 0.937
        self.label_smoothing = 0.0
        self.lrf = 0.1

        self.hyp_file = 'hyp.scratch.yaml'
        # custom hyp
        self.hyp_update = {
            'warmup_epochs': 3.0
        }
        self.transform_hyp = {}

        # test config---------------------------------
        self.conf_thre = 0.3
        self.nms_thre = 0.5

        # export config-------------------------------
        self.nodecode = False  # easy to ncnn deploy

    def get_model(self, train=True):
        from tepe.tasks.yolov5.yolo import Model, Detect, Conv

        if train:
            self.model = Model(self.yolov5_type, ch=3, nc=self.num_classes, model_cfg=self.model_cfg)  # create
            return self.model

        else:
            if Path(self.weights).suffix == '.pt':            
                ckpt = torch.load(self.weights)  # load
                model = ckpt['ema' if ckpt.get('ema') else 'model'].float().fuse().eval()  # FP32 model
            else:
                if not Path(self.weights).exists() and self.weights == '.pth':
                    # use coco pretrained weights
                    model = Model(self.yolov5_type, ch=3, nc=80, model_cfg=None)  # create
                    # logger.info(f"Load COCO pretrained yolov5{self.yolov5_type} model")
                    from tepe.tasks.yolov5 import YOLOv5Trainer
                    model = YOLOv5Trainer.load_pretrained_weights(
                        model, self.yolov5_type, self.device, exclude=()
                    )
                else:
                    model = Model(self.yolov5_type, ch=3, nc=self.num_classes, model_cfg=self.model_cfg)  # create
                    self.load_ckpt(model, self.weights, self.device, load_keys='model')
                model = model.float().fuse().eval()
            # Compatibility updates
            for m in model.modules():
                if type(m) in [nn.Hardswish, nn.LeakyReLU, nn.ReLU, nn.ReLU6, nn.SiLU, Detect, Model]:
                    m.inplace = True  # pytorch 1.7.0 compatibility
                    if type(m) is Detect:
                        if not isinstance(m.anchor_grid, list):  # new Detect Layer compatibility
                            delattr(m, 'anchor_grid')
                            setattr(m, 'anchor_grid', [torch.zeros(1)] * m.nl)
                elif type(m) is Conv:
                    m._non_persistent_buffers_set = set()  # pytorch 1.6.0 compatibility

        self.model = model
        return self.model

    def _get_data_loader(self,
                         data_path,
                         batch_size,
                         augment=False,
                         workers=8,
                         rect=False,
                         pad=0.0,
                         image_weights=False,
                         is_train=True):
        from .datasets import LoadImagesAndLabels
        from .datasets import InfiniteDataLoader

        stride = max(int(self.model.stride.max()), 32)
        transform_hyp = {
            'hsv_h': 0.015,  # image HSV-Hue augmentation (fraction)
            'hsv_s': 0.7,  # image HSV-Saturation augmentation (fraction)
            'hsv_v': 0.4,  # image HSV-Value augmentation (fraction)
            'degrees': 0.0,  # image rotation (+/- deg)
            'translate': 0.1,  # image translation (+/- fraction)
            'scale': 0.5,  # image scale (+/- gain)
            'shear': 0.0,  # image shear (+/- deg)
            'perspective': 0.0,  # image perspective (+/- fraction), range 0-0.001
            'flipud': 0.0,  # image flip up-down (probability)
            'fliplr': 0.5,  # image flip left-right (probability)
            'mosaic': 1.0,  # image mosaic (probability)
            'mixup': 0.0,  # image mixup (probability)
            'copy_paste': 0.0,  # segment copy-paste (probability)
        }
        transform_hyp.update(self.transform_hyp)
        dataset = LoadImagesAndLabels(
            data_path,
            classes=self.CLASS,
            img_size=self.input_size[0] if isinstance(self.input_size, tuple) else self.input_size,
            batch_size=batch_size,
            augment=augment,  # 使用Albumentations进行辅助增强
            hyp=transform_hyp,  # augmentation hyper-parameters
            rect=rect,  # 对输入大小进行排序，使一个batch内的图像大小尽可能相似
            cache_images=self.cache,  # 将所有图像缓存到内存中，加速训练
            single_cls=self.single_cls,  # 所有类别视为一类训练
            stride=int(stride),
            pad=pad,
            image_weights=image_weights,  # use weighted image selection for training
            include_class=self.include_class_idx,
            is_train=is_train,
            dataset_format=self.dataset_format
        )

        batch_size = min(batch_size, len(dataset))
        num_workers = min([
            os.cpu_count(), batch_size if batch_size > 1 else 0, workers])  # number of workers
        sampler = None
        loader = DataLoader if image_weights else InfiniteDataLoader

        dataloader = loader(dataset,
                            batch_size=batch_size,
                            num_workers=num_workers,
                            sampler=sampler,
                            pin_memory=True,
                            collate_fn=LoadImagesAndLabels.collate_fn)
        return dataloader, dataset

    def get_train_loader(self):
        kwargs = dict(
            augment=True,
            workers=self.workers,
            rect=False,
            pad=0.0,
            image_weights=False,
            is_train=True
        )

        self.train_loader, self.train_dataset = self._get_data_loader(
            self.data_root, self.batch_size, **kwargs)
        return self.train_loader, self.train_dataset

    def get_eval_loader(self):
        kwargs = dict(
            augment=False,
            workers=self.workers // 2,
            rect=True,
            pad=0.5,
            image_weights=False,
            is_train=False
        )

        val_loader, val_dataset = self._get_data_loader(self.data_root, self.batch_size, **kwargs)
        return val_loader

    def get_optimizer(self):

        self.nbs = 64  # nominal batch size
        self.accumulate = max(round(self.nbs / self.batch_size), 1)  # accumulate loss before optimizing
        self.weight_decay *= self.batch_size * self.accumulate / self.nbs  # scale weight_decay
        logger.info(f"Scaled weight_decay = {self.weight_decay}")

        pg0, pg1, pg2 = [], [], []  # optimizer parameter groups

        for k, v in self.model.named_modules():
            if hasattr(v, "bias") and isinstance(v.bias, nn.Parameter):
                pg2.append(v.bias)  # biases
            if isinstance(v, nn.BatchNorm2d) or "bn" in k:
                pg0.append(v.weight)  # no decay
            elif hasattr(v, "weight") and isinstance(v.weight, nn.Parameter):
                pg1.append(v.weight)  # apply decay

        if self.adam:
            optimizer = torch.optim.Adam(
                pg0, lr=self.learning_rate, betas=(self.momentum, 0.999))  # adjust beta1 to momentum
        else:
            optimizer = torch.optim.SGD(
                pg0, lr=self.learning_rate, momentum=self.momentum, nesterov=True
            )
        optimizer.add_param_group(
            {"params": pg1, "weight_decay": self.weight_decay}
        )  # add pg1 with weight_decay
        optimizer.add_param_group({"params": pg2})
        logger.info(f"{colorstr('optimizer:')} {type(optimizer).__name__} with parameter groups "
                    f"{len(pg0)} weight, {len(pg1)} weight (no decay), {len(pg2)} bias")
        self.optimizer = optimizer

        del pg0, pg1, pg2

        return self.optimizer

    def get_evaluator(self, train=False):
        from .yolov5_evaluator import YOLOv5Evaluator

        dataloader = self.get_eval_loader()
        evaluator = YOLOv5Evaluator(dataloader=dataloader,
                                    img_size=self.input_size,
                                    num_classes=self.num_classes,
                                    save_result=True,
                                    save_dir=self.output_dir,
                                    conf_thre=self.conf_thre,
                                    nms_thre=self.nms_thre,
                                    single_cls=False,
                                    device=self.device,
                                    training=train
                                    )
        return evaluator

    def train(self):
        from .yolov5_trainer import Trainer
        trainer = Trainer(self)
        trainer.train()

    def eval(self):
        model = self.get_model(train=False)
        evaluator = self.get_evaluator(train=False)
        evaluator.evaluate(model)

    def get_predictor(self):
        from tepe.tasks.yolov5 import YOLOv5Predictor

        model = self.get_model(train=False) if Path(self.weights).suffix in '.pth' else None
        self.predictor = YOLOv5Predictor(
            weights=self.weights, model=model,
            imgsz=self.input_size, classes=self.CLASS,
            conf_thres=self.conf_thre, iou_thres=self.nms_thre,
            device=self.device, save_dir=self.output_dir,
            half=self.fp16, 
        )
        return self.predictor

    def predict(self, source, view_img=False, save_img=True):
        if "predictor" not in self.__dict__:
            self.predictor = self.get_predictor()
        
        self.predictor.predict(source, view_img, save_img)

    def export(self):
        from tepe.core.exporter import Exporter
        from tepe.tasks.yolov5.yolo import Conv, Detect
        from tepe.tasks.yolov5.activations import SiLU

        model = self.get_model(train=False)
        # Update model
        if self.fp16:
            model = model.half()  # to FP16
        for k, m in model.named_modules():
            if isinstance(m, Conv):  # assign export-friendly activations
                if isinstance(m.act, nn.SiLU):
                    m.act = SiLU()
            elif isinstance(m, Detect):
                m.inplace = False
                m.onnx_dynamic = self.dynamic
                m.decoding = not self.nodecode

        if self.export_nms:
            from .common import End2End
            model = End2End(model, iou_thres=self.nms_thre, score_thres=self.conf_thre, max_obj=100).eval()

        self.batch_size = 1
        model.to('cpu')
        exporter = Exporter(self, model=model)

        if 'tensorrt' in self.include:
            if '7' in self.trt_version:  # TensorRT 7 handling https://github.com/ultralytics/yolov5/issues/6012
                grid = model.model[-1].anchor_grid
                model.model[-1].anchor_grid = [a[..., :1, :1, :] for a in grid]
                exporter.task.opset = 12 # opset 12
                exporter.task.suffix = '.trt7'
                exporter.model = model
                exporter.export(YOLOv5Config.preprocess)
                model.model[-1].anchor_grid = grid
            if '8' in self.trt_version:  # TensorRT >= 8
                exporter.task.opset = 13 # opset 13
                exporter.task.suffix = '.trt8'
                exporter.export(YOLOv5Config.preprocess)
        else:
            exporter.export()


    @staticmethod
    def preprocess(im, img_size):
        img = cv2.imread(im)
        img = letterbox(img, img_size, auto=False, stride=32)[0]
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)
        img = img.astype(np.float32)
        img /= 255  # 0 - 255 to 0.0 - 1.0

        return img
