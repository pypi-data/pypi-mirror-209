from typing import Optional, Union, List, Dict, Tuple
import os
import shutil
import time
import math
from copy import deepcopy
import datetime
import numpy as np
import yaml
from tqdm import tqdm
import random
from loguru import logger

import torch
from torch.optim.lr_scheduler import LambdaLR

from tepe.utils.general import (ROOT, increment_path, init_seeds, colorstr, download_pretrained_model, 
                                show_runtime_info, save_task_config_py)
from tepe.utils.torch_utils import select_device, ModelEMA, EarlyStopping
from tepe.modules import MODEL_ZOO
from tepe.tasks.yolov5 import YOLOv5Config
from . import *


model_type_map = {
    'n': 'yolov5n',
    's': 'yolov5s',
    'm': 'yolov5m',
    'l': 'yolov5l',
    'x': 'yolov5x'
}


class Trainer:
    """YOLOv5 trainer
    Args:
        task: YOLOv5Config的实例
    """
    def __init__(self, task: YOLOv5Config) -> None:
        show_runtime_info()
        self.task = task

        self.resume = task.resume
        if self.resume:
            self.train_result_path = os.path.dirname(task.resume_ckpt)
        else:
            self.train_result_path = increment_path(
                task.output_dir, mkdir=True, increment=False)
        self.epoch = 0
        self.max_epoch = task.max_epoch
        self.batch_size = task.batch_size

        hyp_update = task.hyp_update

        # Hyperparameters
        hyp_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hyps', task.hyp_file)
        with open(hyp_path, errors='ignore') as f:
            hyp = yaml.safe_load(f)  # load hyps dict
        hyp.update(hyp_update)
        logger.info(colorstr('hyperparameters: ') + ', '.join(f'{k}={v}' for k, v in hyp.items()))
        self.hyp = hyp

        # Save run settings
        with open(os.path.join(self.train_result_path, 'hyp.yaml'), 'w') as f:
            yaml.safe_dump(hyp, f, sort_keys=False)
        opt = task.__dict__
        with open(os.path.join(self.train_result_path, 'opt.yaml'), 'w') as f:
            yaml.safe_dump(opt, f, sort_keys=False)

        self.device = select_device(task.device)
        self.plot = True
        self.cuda = self.device.type != 'cpu'

        self.freeze_layer = task.freeze_layer
        self.scaler = torch.cuda.amp.GradScaler(enabled=self.cuda)
        self.stopper = EarlyStopping(patience=task.early_stop_patience)

        init_seeds(self.task.seed + 1, deterministic=True)


    def train(self):
        self.before_train()

        for self.epoch in range(self.start_epoch, self.max_epoch):
            self.before_epoch()

            self.train_one_epoch()

            stop = self.after_epoch()
            # early stop
            if stop < 0:
                break

        self.after_train()

    def before_train(self):
        self.start_epoch, self.best_fitness = 0, 0.0
        # model
        model = self.task.get_model(train=True)
        model.to(self.device)

        resume = self.task.resume
        # load pretrained weights
        if self.task.pretrained:
            model = self.load_pretrained_weights(model, self.task.yolov5_type, self.device, 
                                                 exclude=['anchor'] if not resume else [])

        # freeze layer
        freeze = [f'model.{x}.' for x in range(self.freeze_layer)] # layers to freeze
        for k, v in model.named_parameters():
            v.requires_grad = True  # train all layers
            if any(x in k for x in freeze):
                logger.info(f'freezing {k}')
                v.requires_grad = False

        # Image size
        assert self.task.input_size % 32 == 0

        # optimizer
        self.optimizer = self.task.get_optimizer()
        self.nbs = self.task.nbs
        self.accumulate = self.task.accumulate  # accumulate loss before optimizing
        self.hyp['weight_decay'] *= self.batch_size * self.accumulate / self.nbs  # scale weight_decay

        # Scheduler
        if self.task.linear_lr:
            lf = lambda x: (1 - x / (self.max_epoch - 1)) * (1.0 - self.hyp['lrf']) + self.hyp['lrf']  # linear
        else:
            lf = one_cycle(1, self.hyp['lrf'], self.max_epoch)  # cosine 1->hyp['lrf']
        self.scheduler = LambdaLR(self.optimizer, lr_lambda=lf)  # plot_lr_scheduler(optimizer, scheduler, epochs)
        self.lf = lf
        self.scheduler.last_epoch = self.start_epoch - 1  # do not move

        # EMA
        self.ema_model = ModelEMA(model)

        # dataset
        nc = self.task.num_classes
        self.train_loader, train_dataset = self.task.get_train_loader()
        self.imgsz = train_dataset.img_size
        self.names = self.task.CLASS
        mlc = int(np.concatenate(train_dataset.labels, 0)[:, 0].max())  # max label class
        self.max_iter = len(self.train_loader)  # number of batches
        assert mlc < nc, f'Label class {mlc} exceeds nc={nc} in dataset. Possible class labels are 0-{nc - 1}'
        self.max_iter = len(self.train_loader)

        if resume:
            assert os.path.isfile(self.task.resume_ckpt), "model's weights path is not exist"
            ckpt = torch.load(self.task.resume_ckpt, map_location=self.device)  # load checkpoint
            csd = intersect_dicts(ckpt, model.state_dict(), exclude=[])  # intersect
            model.load_state_dict(csd, strict=False)
            logger.info(f'Resume train, load ckpt from {self.task.resume_ckpt}')
            # Optimizer
            if ckpt['optimizer'] is not None:
                self.optimizer.load_state_dict(ckpt['optimizer'])
                self.best_fitness = ckpt['best_fitness']

            # EMA
            if self.task.ema and ckpt.get('ema'):
                self.ema_model.ema.load_state_dict(ckpt['ema'].float().state_dict())
                self.ema_model.updates = ckpt['updates']

            # Epochs
            self.start_epoch = ckpt['epoch'] + 1
            shutil.copyfile(self.task.resume_ckpt,
                            os.path.join(self.train_result_path, f'epoch-{self.start_epoch - 1}.pt'))
            logger.info(f"start epoch is {self.start_epoch}")
            assert self.start_epoch > 0, \
                f'{self.task.resume_ckpt} training to {self.max_epoch} epochs is finished, nothing to resume.'
            if self.max_epoch < self.start_epoch:
                logger.info(
                    f"{self.task.resume_ckpt} has been trained for {ckpt['epoch']} epochs. "
                    f"Fine-tuning for {self.max_epoch} more epochs.")
                self.max_epoch += ckpt['epoch']  # finetune additional epochs
            del ckpt, csd
        else:
            labels = np.concatenate(train_dataset.labels, 0)
            plot_labels(labels, self.names, self.train_result_path)
            check_anchors(train_dataset, model=model, thr=self.hyp['anchor_t'], imgsz=self.imgsz)
            model.half().float()  # pre-reduce anchor precision

        # Model parameters
        nl = de_parallel(model).model[-1].nl  # number of detection layers (to scale hyps)
        self.hyp['box'] *= 3 / nl  # scale to layers
        self.hyp['cls'] *= nc / 80 * 3 / nl  # scale to classes and layers
        self.hyp['obj'] *= (self.imgsz / 640) ** 2 * 3 / nl  # scale to image size and layers
        self.hyp['label_smoothing'] = self.task.label_smoothing
        model.nc = nc  # attach number of classes to model
        model.hyp = self.hyp  # attach hyperparameters to model
        model.class_weights = labels_to_class_weights(train_dataset.labels, nc).to(self.device) * nc  # attach class weights
        model.names = self.names
        self.gs = max(int(model.stride.max()), 32)

        # loss
        self.compute_loss = ComputeLoss(model)  # init loss class

        self.results = (0, 0, 0, 0, 0, 0, 0)  # P, R, mAP@.5, mAP@.5-.95, val_loss(box, obj, cls)

        # number of warmup iterations, max(3 epochs, 1k iterations)
        self.nw = max(round(self.hyp['warmup_epochs'] * self.max_iter), 1000)
        # nw = min(nw, (epochs - start_epoch) / 2 * nb)  # limit warmup to < 1/2 of training
        self.last_opt_step = -1

        # show model info
        self.model = model
        self.model.info()

        # evaluator
        self.evaluator = self.task.get_evaluator(train=True)
        self.evaluator.save_dir = self.train_result_path
        self.evaluator.metrics = self.compute_loss
        
        # save task config
        save_task_config_py(self.task, self.train_result_path)

        self.t0 = time.time()
        logger.info("Training start...")

    def before_epoch(self):
        self.model.train()
        self.mloss = torch.zeros(3, device=self.device)  # mean losses
        print(('\n' + '%10s' * 7) % ('Epoch', 'gpu_mem', 'box', 'obj', 'cls', 'labels', 'img_size'))
        self.pbar = tqdm(enumerate(self.train_loader), total=self.max_iter)  # progress bar
        self.optimizer.zero_grad()

    def train_one_epoch(self):
        for i, (imgs, targets, paths, _) in self.pbar:  # batch -------------------------------------------------------
            ni = i + self.max_iter * self.epoch  # number integrated batches (since train start)
            imgs = imgs.to(self.device, non_blocking=True).float() / 255  # uint8 to float32, 0-255 to 0.0-1.0

            # Warmup
            if ni <= self.nw:
                xi = [0, self.nw]  # x interp
                # compute_loss.gr = np.interp(ni, xi, [0.0, 1.0])  # iou loss ratio (obj_loss = 1.0 or iou)
                self.accumulate = max(1, np.interp(ni, xi, [1, self.nbs / self.batch_size]).round())
                for j, x in enumerate(self.optimizer.param_groups):
                    # bias lr falls from 0.1 to lr0, all other lrs rise from 0.0 to lr0
                    x['lr'] = np.interp(ni, xi, [self.hyp['warmup_bias_lr']
                                                 if j == 2 else 0.0, x['initial_lr'] * self.lf(self.epoch)])
                    if 'momentum' in x:
                        x['momentum'] = np.interp(ni, xi, [self.hyp['warmup_momentum'], self.hyp['momentum']])

            # Multi-scale
            if self.task.multi_scale:
                sz = random.randrange(self.imgsz * 0.5, self.imgsz * 1.5 + self.gs) // self.gs * self.gs  # size
                sf = sz / max(imgs.shape[2:])  # scale factor
                if sf != 1:
                    ns = [math.ceil(x * sf / self.gs) * self.gs for x in imgs.shape[2:]]  # new shape (stretched to gs-multiple)
                    imgs = torch.nn.functional.interpolate(imgs, size=ns, mode='bilinear', align_corners=False)

            # Forward
            with torch.cuda.amp.autocast(enabled=self.cuda):
                pred = self.model(imgs)  # forward
                loss, loss_items = self.compute_loss(pred, targets.to(self.device))  # loss scaled by batch_size

            # Backward
            self.scaler.scale(loss).backward()

            # Optimize
            if ni - self.last_opt_step >= self.accumulate:
                self.scaler.step(self.optimizer)  # optimizer.step
                self.scaler.update()
                self.optimizer.zero_grad()
                if self.ema_model:
                    self.ema_model.update(self.model)
                self.last_opt_step = ni

            # Log
            self.mloss = (self.mloss * i + loss_items) / (i + 1)  # update mean losses
            mem = f'{torch.cuda.memory_reserved() / 1E9 if torch.cuda.is_available() else 0:.3g}G'  # (GB)
            self.pbar.set_description(('%10s' * 2 + '%10.4g' * 5) % (
                f'{self.epoch}/{self.max_epoch - 1}', mem, *self.mloss, targets.shape[0], imgs.shape[-1]))

    def after_epoch(self):
        # Scheduler
        lr = [x['lr'] for x in self.optimizer.param_groups]  # for loggers
        self.scheduler.step()

        # mAP
        self.ema_model.update_attr(self.model, include=['yaml', 'nc', 'hyp', 'names', 'stride', 'class_weights'])
        final_epoch = (self.epoch + 1 == self.max_epoch) or self.stopper.possible_stop
        if self.epoch % self.task.eval_interval == 0:  # Calculate mAP
            self.results, maps, _ = self.evaluator.evaluate(model=self.ema_model.ema)

        # save model
        best_ckpt, last_ckpt = [os.path.join(self.train_result_path, pt) for pt in ['best.pth', 'last.pth']]

        ckpt = {'epoch': self.epoch,
                'best_fitness': self.best_fitness,
                'model': self.ema_model.ema.state_dict(),
                # 'model': deepcopy(de_parallel(self.model)).half(),
                # 'model': deepcopy(self.ema_model.ema).half(),
                # 'updates': self.ema_model.updates,
                'optimizer': self.optimizer.state_dict(),
                'date': datetime.datetime.now().isoformat()}

        # Save last, best and delete
        torch.save(ckpt, last_ckpt)
        del ckpt

        # Update best mAP
        fi = fitness(np.array(self.results).reshape(1, -1))  # weighted combination of [P, R, mAP@.5, mAP@.5-.95]

        if fi > self.best_fitness:
            self.best_fitness = fi
            shutil.copyfile(last_ckpt, best_ckpt)

        # Stop Single-GPU
        stop = self.stopper(epoch=self.epoch, fitness=fi)
        return stop

    def after_train(self):
        logger.info(f'{self.epoch - self.start_epoch + 1} epochs completed in '
                    f'{(time.time() - self.t0) / 3600:.3f} hours.')
        for f in [os.path.join(self.train_result_path, pt) for pt in ['best.pt', 'last.pt']]:
            if 'best' in f and os.path.exists(f):
                setattr(self.task, 'weights', f)
                setattr(self.evaluator, 'training', False)
                logger.info(f'\nValidating {f}...')
                results, _, _ = self.evaluator.evaluate(model=self.ema_model.ema) # val best model with plots
        logger.info(f"Results saved to {colorstr('bold', self.train_result_path)}")
        
    @staticmethod
    def load_pretrained_weights(model, model_type, device, exclude=()):
        pretrained_weights_path = download_pretrained_model(MODEL_ZOO[model_type_map[model_type]])
        pretrained_ckpt = torch.load(pretrained_weights_path, map_location=select_device(device))  # load checkpoint
        # exclude = ['anchor'] if not resume else []
        csd = intersect_dicts(pretrained_ckpt, model.state_dict(), exclude=exclude)  # intersect
        model.load_state_dict(csd, strict=False)
        logger.info(
            f'Transferred {len(csd)}/{len(model.state_dict())} items from {pretrained_weights_path}'
        )  # report
        del pretrained_ckpt, csd
        return model
