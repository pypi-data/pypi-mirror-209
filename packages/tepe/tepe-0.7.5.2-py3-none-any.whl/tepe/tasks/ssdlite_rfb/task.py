from loguru import logger
import torch
from tepe.core import BaseTask, register_config


@register_config('ssdlite_rfb')
class SSDLiteRFBConfig(BaseTask):
    def __init__(self):
        super().__init__()
        self.task_name = 'ssd-rfb'
        self.CLASS = ('face')

        self.input_size = (320, 240)
        self.device = 'cuda:0'
        self.early_stop = False  # this task's metrics is loss
        
        self.data_root = ''

        self.basic_lr_per_img = 0.01 / 24

        self.image_mean = [127, 127, 127]
        self.image_std = 128.0
        self.min_boxes = [[10, 16, 24], [32, 48], [64, 96], [128, 192, 256]]

        self.center_variance = 0.1
        self.size_variance = 0.2
        self.overlap_threshold = 0.35

        self.freeze_base_net = False  # Freeze task_base net layers.
        self.base_net_lr = None  # initial learning rate for base net.
        self.extra_layers_lr = None  # initial learning rate for the layers not in base net and prediction heads.
        self.freeze_net = False  # Freeze all the layers except the prediction head.

        self.adam = False  # optimizer type, False for SGD
        self.scheduler = 'multi-step'
        self.milestones = [120, 210]

        self.conf_thre = 0.6
        self.nms_thre = 0.3

    def get_model(self, train=True):
        import itertools
        from .creat_model import create_model

        self._define_img_size()
        self.num_classes = len(self.CLASS) + 1
        model = create_model(self.num_classes, self.priors, is_test=not train)

        if not train:
            self.load_ckpt(model, self.weights, load_keys='model')
            setattr(model, 'center_variance', self.center_variance)
            setattr(model, 'size_variance', self.size_variance)
            return model
        base_net_lr = self.base_net_lr if self.base_net_lr is not None else self.learning_rate
        extra_layers_lr = self.extra_layers_lr if self.extra_layers_lr is not None else self.learning_rate
        if self.freeze_base_net:
            self._freeze_net_layers(model.base_net)
            params = itertools.chain(
                model.source_layer_add_ons.parameters(), model.extras.parameters(),
                model.regression_headers.parameters(), model.classification_headers.parameters()
            )
            params = [
                {'params': itertools.chain(
                    model.source_layer_add_ons.parameters(),
                    model.extras.parameters()
                ), 'lr': self.extra_layers_lr},
                {'params': itertools.chain(
                    model.regression_headers.parameters(),
                    model.classification_headers.parameters()
                )}
            ]
        elif self.freeze_net:
            self._freeze_net_layers(model.base_net)
            self._freeze_net_layers(model.source_layer_add_ons)
            self._freeze_net_layers(model.extras)
            params = itertools.chain(
                model.regression_headers.parameters(),
                model.classification_headers.parameters())
            logger.info("Freeze all the layers except prediction heads.")
        else:
            params = [
                {'params': model.base_net.parameters(), 'lr': base_net_lr},
                {'params': itertools.chain(
                    model.source_layer_add_ons.parameters(),
                    model.extras.parameters()
                ), 'lr': extra_layers_lr},
                {'params': itertools.chain(
                    model.regression_headers.parameters(),
                    model.classification_headers.parameters()
                )}
            ]
        self.params = params

        return model

    def get_train_loader(self):
        from torch.utils.data import DataLoader
        from .augmentation import TrainAugmentation
        from tepe.data.datasets.ssdrfb_voc import VOCDataset

        train_transform = TrainAugmentation(
            self.input_size, self.image_mean, self.image_std)

        dataset = VOCDataset(self.data_root, self.CLASS,
                             transform=train_transform,
                             target_transform=self.matcher)
        num_workers = 4
        train_loader = DataLoader(dataset, self.batch_size,
                                  num_workers=num_workers,
                                  shuffle=True)
        return train_loader
        
    def get_eval_loader(self):
        from torch.utils.data import DataLoader
        from .augmentation import TestTransform
        from tepe.data.datasets.ssdrfb_voc import VOCDataset

        test_transform = TestTransform(
            self.input_size, self.image_mean, self.image_std)

        val_dataset = VOCDataset(self.data_root, self.CLASS,
                                 transform=test_transform,
                                 target_transform=self.matcher, is_test=True)
        num_workers = 4
        val_loader = DataLoader(val_dataset, self.batch_size,
                                num_workers=num_workers,
                                shuffle=False)
        return val_loader

    def get_loss(self):
        from .loss import MultiboxLoss

        criterion = MultiboxLoss(self.priors, neg_pos_ratio=3,
                                 center_variance=self.center_variance, 
                                 size_variance=self.size_variance,
                                 device=self.device)
        return criterion

    def get_optimizer(self):
        from torch.optim import SGD, Adam

        if not self.adam:
            momentum = 0.9
            weight_decay = 5e-4
            optimizer = SGD(self.params, lr=self.learning_rate,
                            momentum=momentum, weight_decay=weight_decay)
        else:
            optimizer = Adam(self.params, lr=self.learning_rate)
            logger.info("use Adam optimizer")
        self.optimizer = optimizer
        return self.optimizer

    def get_lr_scheduler(self, **kwargs):
        from torch.optim.lr_scheduler import MultiStepLR, CosineAnnealingLR

        if self.scheduler == 'multi-step':
            logger.info("Uses MultiStepLR scheduler.")
            scheduler = MultiStepLR(self.optimizer, milestones=self.milestones, gamma=0.1)
        elif self.scheduler == 'cosine':
            logger.info("Uses CosineAnnealingLR scheduler.")
            t_max = 120  # T_max value for Cosine Annealing Scheduler
            scheduler = CosineAnnealingLR(self.optimizer, t_max, last_epoch=-1)
        else:
            raise Exception(f"Unsupported Scheduler: {self.scheduler}.")
        return scheduler

    def _define_img_size(self):
        from .box_utils import generate_priors
        from .ssd import MatchPrior

        img_size_dict = {128: [128, 96],
                         160: [160, 120],
                         320: [320, 240],
                         480: [480, 360],
                         640: [640, 480],
                         1280: [1280, 960]}
        size = self.input_size[0]
        self.input_size = img_size_dict[size]

        feature_map_w_h_list_dict = {128: [[16, 8, 4, 2], [12, 6, 3, 2]],
                                     160: [[20, 10, 5, 3], [15, 8, 4, 2]],
                                     320: [[40, 20, 10, 5], [30, 15, 8, 4]],
                                     480: [[60, 30, 15, 8], [45, 23, 12, 6]],
                                     640: [[80, 40, 20, 10], [60, 30, 15, 8]],
                                     1280: [[160, 80, 40, 20], [120, 60, 30, 15]]}
        self.feature_map_w_h_list = feature_map_w_h_list_dict[size]

        self.strides = []
        for i in range(0, len(self.input_size)):
            item_list = []
            for k in range(0, len(self.feature_map_w_h_list[i])):
                item_list.append(self.input_size[i] / self.feature_map_w_h_list[i][k])
            self.strides.append(item_list)
        self.priors = generate_priors(
            self.feature_map_w_h_list, self.strides,
            self.input_size, self.min_boxes)

        self.matcher = MatchPrior(
            self.priors, self.center_variance,
            self.size_variance, self.overlap_threshold)

    @staticmethod
    def _freeze_net_layers(net):
        for param in net.parameters():
            param.requires_grad = False

    def get_evaluator(self, train=False):
        val_loader = self.get_eval_loader()
        evalutor = SSDRFBEvaluator(dataloader=val_loader,
                                   img_size=self.input_size,
                                   num_classes=self.num_classes,
                                   metrics=self.get_loss(),
                                   training=train,
                                   save_dir=self.output_dir
                                   )
        return evalutor

    def train(self):
        trainer = SSDRFBTrainer(self)
        trainer.train()

    def predict(self, source, view_img=False, save_img=True):
        from .augmentation import PredictionTransform

        model = self.get_model(train=False)
        transform = PredictionTransform(
            self.input_size, self.image_mean, self.image_std)
        predictor = SSDRFBPredictor(
            model, 
            transform=transform,
            nms_method='hard',  # hard or soft
            iou_threshold=self.nms_thre,
            filter_threshold=self.conf_thre,
            candidate_size=1500,
            sigma=0.5,
            device=self.device,
            save_dir=self.output_dir
            )

        predictor.predict(source, view_img=view_img, save_img=save_img)


from tepe.core.base_trainer import Trainer

class SSDRFBTrainer(Trainer):
    def __init__(self, task):
        super(SSDRFBTrainer, self).__init__(task)

    def before_epoch(self):
        if self.epoch != 0:
            if not self.task.adam:
                self.lr_scheduler.step()

    def train_one_iter(self, data):
        images, boxes, labels, _ = data
        images = images.to(self.device)
        boxes = boxes.to(self.device)
        labels = labels.to(self.device)

        self.optimizer.zero_grad()
        confidence, locations = self.model(images)
        regression_loss, classification_loss = self.loss_fn(
            confidence, locations, labels, boxes
        )
        loss = regression_loss + classification_loss
        self.scaler.scale(loss).backward()
        self.scaler.step(self.optimizer)
        lr = self.optimizer.param_groups[0]['lr']

        return {'loss': loss, 'lr': lr}


from tepe.core.base_evaluator import Evaluator

class SSDRFBEvaluator(Evaluator):
    def __init__(self, dataloader, **kwargs):
        super().__init__(dataloader, **kwargs)

    def evaluate_one_iter(self, data):

        images, boxes, labels, _ = data
        images = images.to(self.device)
        boxes = boxes.to(self.device)
        labels = labels.to(self.device)

        with torch.no_grad():
            confidence, locations = self.model(images)
            regression_loss, classification_loss = self.metrics(
                confidence, locations, labels, boxes
            )
            loss = regression_loss + classification_loss

        return {'loss': loss,
                'reg_loss': regression_loss,
                'cls_loss': classification_loss
                }


import time
import cv2
from tepe.tasks.ssdlite_rfb import box_utils
from tepe.core.base_predictor import Predictor

class SSDRFBPredictor(Predictor):
    def __init__(self, net, transform=None,
                 nms_method=None, iou_threshold=0.3, 
                 filter_threshold=0.01, candidate_size=200, 
                 sigma=0.5, device=None, 
                 save_dir=None):
        super().__init__(save_dir)

        self.net = net
        self.transform = transform
        self.iou_threshold = iou_threshold
        self.filter_threshold = filter_threshold
        self.candidate_size = candidate_size
        self.nms_method = nms_method

        self.sigma = sigma
        if device:
            self.device = device
        else:
            self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.net.to(self.device)
        self.net.eval()

    def __call__(self, img_meta):
        boxes, labels, probs = self.run(img_meta)
        image = self.draw(img_meta['img'], boxes, probs)
        return image

    def run(self, img_meta):
        image = img_meta['img']
        cpu_device = torch.device("cpu")
        height, width, _ = image.shape
        image = self.transform(image)
        images = image.unsqueeze(0)
        images = images.to(self.device)
        with torch.no_grad():
            for i in range(1):
                start = time.time()
                scores, boxes = self.net.forward(images)
                logger.info("Inference time: %s" % (time.time() - start))
        boxes = boxes[0]
        scores = scores[0]

        # this version of nms is slower on GPU, so we move data to CPU.
        boxes = boxes.to(cpu_device)
        scores = scores.to(cpu_device)
        picked_box_probs = []
        picked_labels = []
        for class_index in range(1, scores.size(1)):
            probs = scores[:, class_index]
            mask = probs > self.filter_threshold
            probs = probs[mask]
            if probs.size(0) == 0:
                continue
            subset_boxes = boxes[mask, :]
            box_probs = torch.cat([subset_boxes, probs.reshape(-1, 1)], dim=1)
            box_probs = box_utils.nms(box_probs, self.nms_method,
                                      score_threshold=self.filter_threshold,
                                      iou_threshold=self.iou_threshold,
                                      sigma=self.sigma,
                                      top_k=self.candidate_size // 2,
                                      candidate_size=self.candidate_size)
            picked_box_probs.append(box_probs)
            picked_labels.extend([class_index] * box_probs.size(0))
        if not picked_box_probs:
            return torch.tensor([]), torch.tensor([]), torch.tensor([])
        picked_box_probs = torch.cat(picked_box_probs)
        picked_box_probs[:, 0] *= width
        picked_box_probs[:, 1] *= height
        picked_box_probs[:, 2] *= width
        picked_box_probs[:, 3] *= height
        return picked_box_probs[:, :4], torch.tensor(picked_labels), picked_box_probs[:, 4]

    def draw(self, image, boxes, probs):
        for i in range(boxes.size(0)):
            box = boxes[i, :]
            cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 0, 255), 2)
            # label = f"""{voc_dataset.class_names[labels[i]]}: {probs[i]:.2f}"""
            label = f"{probs[i]:.2f}"
            # cv2.putText(orig_image, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(image, str(boxes.size(0)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        return image
