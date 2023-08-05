import os
import warnings
from addict import Dict

import pytorch_lightning as pl
import torch
from pytorch_lightning.callbacks import TQDMProgressBar as ProgressBar

from tepe.core import BaseTask, register_config
from tepe.data.datasets.public_class_names import coco_classes

from tepe.tasks.nanodet.data.collate import naive_collate
from tepe.tasks.nanodet.trainer import TrainingTask
from tepe.tasks.nanodet.util import NanoDetLightningLogger, convert_old_model, load_model_weight, mkdir

logger = NanoDetLightningLogger(name='NanoDet')

@register_config('nanodet')
class NanoDetConfig(BaseTask):
    def __init__(self):
        super().__init__()
        self.task_name = 'nanodet_plus_m'
        self.seed = None

        # data------------------------------
        self.class_names = coco_classes
        self.num_classes = 80
        self.input_size = [416, 416]  # width, height
        self.dataset_type = 'coco'
        self.data_root = 'coco/'
        self.keep_ratio = True
        self.train_pipeline = Dict(
            perspective=0.0,
            scale=[0.6, 1.4],
            stretch=[[1, 1], [1, 1]],
            rotation=0,
            shear=0,
            translate=0.2,
            flip=0.5,
            brightness=0.2,
            contrast=[0.8, 1.2],
            saturation=[0.8, 1.2],
            normalize=[[103.53, 116.28, 123.675], [57.375, 57.12, 58.395]],
        )
        self.val_pipeline = Dict(
            normalize=[[103.53, 116.28, 123.675], [57.375, 57.12, 58.395]],
        )

        # model-----------------------------
        self.weight_averager = Dict(
            decay=0.9998
        )
        self.arch_name = 'NanoDetPlus'
        self.backbone = Dict(
            name='ShuffleNetV2',
            model_size='1.0x',
            out_stages=[2, 3, 4],
            activation='LeakyReLU'
        )
        self.fpn = Dict(
            name='GhostPAN',
            in_channels=[116, 232, 464],
            out_channels=96,
            kernel_size=5,
            num_extra_level=1,
            use_depthwise=True,
            activation='LeakyReLU',
        )
        self.head = Dict(
            name='NanoDetPlusHead',
            input_channel=96,
            feat_channels=96,
            stacked_convs=2,
            kernel_size=5,
            strides=[8, 16, 32, 64],
            activation='LeakyReLU',
            reg_max=7,
            norm_cfg=Dict(type='BN'),
        )
        # loss
        self.loss_qfl = Dict(
            name='QualityFocalLoss',
            use_sigmoid=True,
            beta=2.0,
            loss_weight=1.0
        )
        self.loss_dfl = Dict(
            name='DistributionFocalLoss',
            loss_weight=0.25
        )
        self.loss_bbox = Dict(
            name='GIoULoss',
            loss_weight=2.0
        )
        # Auxiliary head, only use in training time.
        self.detach_epoch = 10
        self.aux_head = Dict(
            name='SimpleConvHead',
            input_channel=192,
            feat_channels=192,
            stacked_convs=4,
            strides=[8, 16, 32, 64],
            activation='LeakyReLU',
            reg_max=7
        )

        # device
        self.device = [0]
        self.workers_per_gpu = 8
        self.batch_size = 48  # batchsize per gpu

        # train schedule
        self.local_rank = -1
        self.basic_lr_per_img = 0.001 / 48
        self.max_epoch = 300
        self.optimizer = Dict(
            name='AdamW',
            weight_decay=0.05
        )
        self.warmup = Dict(
            name='linear',
            steps=500,
            ratio=0.0001
        )
        self.lr_schedule = Dict(
            name='CosineAnnealingLR',
            T_max=300,
            eta_min=0.00005
        )
        self.grad_clip = 35

        # evaluate
        self.eval_interval = 10  # epoch
        self.print_interval = 10  # iter
        self.save_key = 'mAP'
        self.test_mode = 'train'

        # predict
        self.conf_thre = 0.35

    def build_model(self):
        from .model.arch.nanodet_plus import NanoDetPlus
        from .model.arch.one_stage_detector import OneStageDetector

        self.head.update(Dict(
            num_classes=self.num_classes,
            loss=Dict(
                loss_qfl=self.loss_qfl,
                loss_dfl=self.loss_dfl,
                loss_bbox=self.loss_bbox
            )
        ))
        arch_type = self.arch_name
        if arch_type == "OneStageDetector":
            model = OneStageDetector(
                self.backbone, self.fpn, self.head
            )
        elif arch_type == "NanoDetPlus":
            self.aux_head.update(Dict(num_classes=self.num_classes))
            model = NanoDetPlus(
                self.backbone, self.fpn, self.aux_head, self.head, detach_epoch=self.detach_epoch
            )
        else:
            raise NotImplementedError
        return model

    def build_dataset(self, mode):
        from .data.dataset import CocoDataset, XMLDataset, CustomXML

        dataset_cfg = Dict(
            class_names=self.class_names,
            input_size=self.input_size,
            keep_ratio=self.keep_ratio,
            pipeline=self.train_pipeline if mode == 'train' else self.val_pipeline
        )
        name = self.dataset_type
        if name == "coco":
            dataset_cfg.update(
                Dict(img_path=os.path.join(self.data_root, 'train2017'),
                     ann_path=os.path.join(self.data_root, 'annotations/instances_train2017.json')
                     )
            )
            return CocoDataset(mode=mode, **dataset_cfg)
        elif name == "voc":
            dataset_cfg.update(
                Dict(img_path=os.path.join(self.data_root, 'JPEGImages'),
                     ann_path=os.path.join(self.data_root, 'Annotations')
                     )
            )
            return XMLDataset(mode=mode, **dataset_cfg)
        elif name == "custom_voc":
            dataset_cfg.update(
                Dict(img_path=os.path.join(self.data_root, 'JPEGImages'),
                     ann_path=os.path.join(self.data_root, 'Annotations')
                     )
            )
            return CustomXML(mode=mode, **dataset_cfg)
        else:
            raise NotImplementedError("Unknown dataset type!")

    def build_evaluator(self, dataset):
        from .evaluator import CocoDetectionEvaluator

        return CocoDetectionEvaluator(dataset)

    def train(self):
        if self.num_classes != len(self.class_names):
            raise ValueError(
                "self.num_classes must equal len(self.class_names), "
                "but got {} and {}".format(
                    self.num_classes, len(self.class_names)
                )
            )
        torch.backends.cudnn.enabled = True
        torch.backends.cudnn.benchmark = True
        local_rank = int(self.local_rank)
        mkdir(local_rank, self.output_dir)

        # logger = NanoDetLightningLogger(self.output_dir)
        logger.init(save_dir=self.output_dir)
        logger.dump_cfg(self)

        if self.seed is not None:
            logger.info("Set random seed to {}".format(self.seed))
            pl.seed_everything(self.seed)

        logger.info("Setting up data...")
        train_dataset = self.build_dataset(mode="train")
        val_dataset = self.build_dataset(mode="val")

        evaluator = self.build_evaluator(val_dataset)

        train_dataloader = torch.utils.data.DataLoader(
            train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.workers_per_gpu,
            pin_memory=True,
            collate_fn=naive_collate,
            drop_last=True,
        )
        val_dataloader = torch.utils.data.DataLoader(
            val_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.workers_per_gpu,
            pin_memory=True,
            collate_fn=naive_collate,
            drop_last=False,
        )

        logger.info("Creating model...")
        task = TrainingTask(self, evaluator)

        if self.pretrained and self.weights is not None:
            ckpt = torch.load(self.weights)
            if "pytorch-lightning_version" not in ckpt:
                warnings.warn(
                    "Warning! Old .pth checkpoint is deprecated. "
                    "Convert the checkpoint with tools/convert_old_checkpoint.py "
                )
                ckpt = convert_old_model(ckpt)
            load_model_weight(task.model, ckpt, logger)
            logger.info("Loaded model weight from {}".format(self.weights))

        model_resume_path = None
        if self.resume:
            model_resume_path = (
                os.path.join(self.output_dir, "model_last.ckpt")
                if self.resume_ckpt is None
                else self.resume_ckpt
            )

        self.device = [self.device] if isinstance(self.device, int) else self.device
        accelerator = None if len(self.device) <= 1 else "ddp"

        trainer = pl.Trainer(
            default_root_dir=self.output_dir,
            max_epochs=self.max_epoch,
            gpus=self.device,
            check_val_every_n_epoch=self.eval_interval,
            accelerator=accelerator,
            log_every_n_steps=self.print_interval,
            num_sanity_val_steps=0,
            resume_from_checkpoint=model_resume_path,
            callbacks=[ProgressBar(refresh_rate=0)],  # disable tqdm bar
            logger=logger,
            benchmark=True,
            gradient_clip_val=self.grad_clip,
        )

        trainer.fit(task, train_dataloader, val_dataloader)

    def eval(self):
        import datetime

        local_rank = -1
        torch.backends.cudnn.enabled = True
        torch.backends.cudnn.benchmark = True

        timestr = datetime.datetime.now().__format__("%Y%m%d%H%M")
        save_dir = os.path.join(self.output_dir, 'eval' + timestr)
        mkdir(local_rank, save_dir)
        logger.init(save_dir=save_dir)

        self.test_mode = 'val'

        logger.info("Setting up data...")
        val_dataset = self.build_dataset(mode='val')
        val_dataloader = torch.utils.data.DataLoader(
            val_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.workers_per_gpu,
            pin_memory=True,
            collate_fn=naive_collate,
            drop_last=False,
        )

        evaluator = self.build_evaluator(val_dataset)

        logger.info("Creating model...")
        task = TrainingTask(self, evaluator)

        ckpt = torch.load(self.weights)
        if "pytorch-lightning_version" not in ckpt:
            warnings.warn(
                "Warning! Old .pth checkpoint is deprecated. "
                "Convert the checkpoint with tools/convert_old_checkpoint.py "
            )
            ckpt = convert_old_model(ckpt)
        task.load_state_dict(ckpt["state_dict"])

        trainer = pl.Trainer(
            default_root_dir=self.output_dir,
            gpus=[self.device] if isinstance(self.device, int) else self.device,
            accelerator="ddp",
            log_every_n_steps=self.print_interval,
            num_sanity_val_steps=0,
            logger=logger,
        )
        logger.info("Starting testing...")
        trainer.test(task, val_dataloader)

    def predict(self, source, view_img=False, save_img=True):
        if "predictor" not in self.__dict__:
            from .predictor import Predictor

            self.predictor = Predictor(
                cfg=self,
                model_path=self.weights,
                save_dir=self.output_dir
            )

        self.predictor.predict(source, view_img, save_img)

    def export(self):
        from tepe.core import Exporter

        model = self.build_model()
        ckpt = torch.load(self.weights, map_location=lambda storage, loc: storage)
        load_model_weight(model, ckpt)
        if self.backbone.name == "RepVGG":
            self.backbone.update({"deploy": True})
            deploy_model = self.build_model()
            from .model.backbone.repvgg import repvgg_det_model_convert

            model = repvgg_det_model_convert(model, deploy_model)

        exporter = Exporter(self, model=model)
        exporter.export()

    def get_model(self, train=True):
        pass

    def get_train_loader(self):
        pass


if __name__ == '__main__':
    task = NanoDetConfig()
    print(task)