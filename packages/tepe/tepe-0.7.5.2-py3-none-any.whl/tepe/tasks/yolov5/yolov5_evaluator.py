import os
from pathlib import Path
from threading import Thread
from tqdm import tqdm
from loguru import logger
import numpy as np
import torch

from tepe.core.base_evaluator import Evaluator
from tepe.utils.torch_utils import time_synchronized
from .utils.metrics import ConfusionMatrix, ap_per_class
from .utils.plots import plot_images, output_to_target
from .utils.general import non_max_suppression, scale_coords, xywh2xyxy, box_iou


class YOLOv5Evaluator(Evaluator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.conf_thre = kwargs.get('conf_thre', 0.4)
        self.nms_thre = kwargs.get('nms_thre', 0.5)
        self.plots = kwargs.get('plots', True)
        self.single_cls = kwargs.get('single_cls', False)

    @torch.no_grad()
    def evaluate(self, model=None):
        model.to(self.device)
        model.half() if self.half else model.float()
        # Configure
        model.eval()

        iouv = torch.linspace(0.5, 0.95, 10).to(self.device)  # iou vector for mAP@0.5:0.95
        niou = iouv.numel()
        seen = 0
        confusion_matrix = ConfusionMatrix(nc=self.num_classes)
        names = {k: v for k, v in enumerate(model.names if hasattr(model, 'names') else model.module.names)}
        s = ('%20s' + '%11s' * 6) % ('Class', 'Images', 'Labels', 'P', 'R', 'mAP@.5', 'mAP@.5:.95')
        dt, p, r, f1, mp, mr, map50, map = [0.0, 0.0, 0.0], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        loss = torch.zeros(3, device=self.device)
        jdict, stats, ap, ap_class = [], [], [], []
        for batch_i, (img, targets, paths, shapes) in enumerate(tqdm(self.dataloader, desc=s)):
            t1 = time_synchronized()
            img = img.to(self.device, non_blocking=True)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255  # 0 - 255 to 0.0 - 1.0
            targets = targets.to(self.device)
            nb, _, height, width = img.shape  # batch size, channels, height, width
            t2 = time_synchronized()
            dt[0] += t2 - t1

            # Run model
            out, train_out = model(img, augment=False)  # inference and training outputs
            dt[1] += time_synchronized() - t2

            # Compute loss
            if self.metrics:
                loss += self.metrics([x.float() for x in train_out], targets)[1]  # box, obj, cls

            # Run NMS
            targets[:, 2:] *= torch.Tensor([width, height, width, height]).to(self.device)  # to pixels
            lb = []  # for autolabelling
            t3 = time_synchronized()
            out = non_max_suppression(out, self.conf_thre, self.nms_thre,
                                      labels=lb, multi_label=True, agnostic=self.single_cls)
            dt[2] += time_synchronized() - t3

            # Statistics per image
            for si, pred in enumerate(out):
                labels = targets[targets[:, 0] == si, 1:]
                nl = len(labels)
                tcls = labels[:, 0].tolist() if nl else []  # target class
                path, shape = Path(paths[si]), shapes[si][0]
                seen += 1

                if len(pred) == 0:
                    if nl:
                        stats.append((torch.zeros(0, niou, dtype=torch.bool),
                                      torch.Tensor(), torch.Tensor(), tcls))
                    continue

                # Predictions
                if self.single_cls:
                    pred[:, 5] = 0
                predn = pred.clone()
                scale_coords(img[si].shape[1:], predn[:, :4], shape, shapes[si][1])  # native-space pred

                # Evaluate
                if nl:
                    tbox = xywh2xyxy(labels[:, 1:5])  # target boxes
                    scale_coords(img[si].shape[1:], tbox, shape, shapes[si][1])  # native-space labels
                    labelsn = torch.cat((labels[:, 0:1], tbox), 1)  # native-space labels
                    correct = self.process_batch(predn, labelsn, iouv)  # Tensor[N, 10]
                    if self.plots:
                        confusion_matrix.process_batch(predn, labelsn)
                else:
                    correct = torch.zeros(pred.shape[0], niou, dtype=torch.bool)  # Tensor[N, 10]
                stats.append((correct.cpu(), pred[:, 4].cpu(), pred[:, 5].cpu(), tcls))  # (correct, conf, pcls, tcls)

            # Plot images
            if self.plots and batch_i < 3:
                f = os.path.join(self.save_dir, f'val_batch{batch_i}_labels.jpg')  # labels
                Thread(target=plot_images, args=(img, targets, paths, f, names), daemon=True).start()
                f = os.path.join(self.save_dir, f'val_batch{batch_i}_pred.jpg')  # predictions
                Thread(target=plot_images, args=(img, output_to_target(out), paths, f, names), daemon=True).start()

        # Compute statistics
        stats = [np.concatenate(x, 0) for x in zip(*stats)]  # to numpy
        if len(stats) and stats[0].any():
            p, r, ap, f1, ap_class = ap_per_class(*stats, plot=self.plots, save_dir=self.save_dir, names=names)
            ap50, ap = ap[:, 0], ap.mean(1)  # AP@0.5, AP@0.5:0.95
            mp, mr, map50, map = p.mean(), r.mean(), ap50.mean(), ap.mean()
            nt = np.bincount(stats[3].astype(np.int64), minlength=self.num_classes)  # number of targets per class
        else:
            nt = torch.zeros(1)

        # Print results
        pf = '%20s' + '%11i' * 2 + '%11.3g' * 4  # print format
        print(pf % ('all', seen, nt.sum(), mp, mr, map50, map))

        # Print results per class
        if self.num_classes > 1 and len(stats):
            for i, c in enumerate(ap_class):
                print(pf % (names[c], seen, nt[c], p[i], r[i], ap50[i], ap[i]))

        # Print speeds
        t = tuple(x / seen * 1E3 for x in dt)  # speeds per image
        if not self.training:
            logger.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image' % t)

        # Plots
        if self.plots:
            confusion_matrix.plot(save_dir=self.save_dir, names=list(names.values()))

        # Return results
        model.float()  # for training

        maps = np.zeros(self.num_classes) + map
        for i, c in enumerate(ap_class):
            maps[c] = ap[i]
        return (mp, mr, map50, map, *(loss.cpu() / len(self.dataloader)).tolist()), maps, t

    @staticmethod
    def process_batch(detections, labels, iouv):
        """
        Return correct predictions matrix. Both sets of boxes are in (x1, y1, x2, y2) format.
        Arguments:
            detections (Array[N, 6]), x1, y1, x2, y2, conf, class
            labels (Array[M, 5]), class, x1, y1, x2, y2
        Returns:
            correct (Array[N, 10]), for 10 IoU levels
        """
        correct = torch.zeros(detections.shape[0], iouv.shape[0], dtype=torch.bool, device=iouv.device)
        iou = box_iou(labels[:, 1:], detections[:, :4])
        x = torch.where(
            (iou >= iouv[0]) & (labels[:, 0:1] == detections[:, 5]))  # IoU above threshold and classes match
        if x[0].shape[0]:
            matches = torch.cat((torch.stack(x, 1), iou[x[0], x[1]][:, None]),
                                1).cpu().numpy()  # [label, detection, iou]
            if x[0].shape[0] > 1:
                matches = matches[matches[:, 2].argsort()[::-1]]
                matches = matches[np.unique(matches[:, 1], return_index=True)[1]]
                # matches = matches[matches[:, 2].argsort()[::-1]]
                matches = matches[np.unique(matches[:, 0], return_index=True)[1]]
            matches = torch.Tensor(matches).to(iouv.device)
            correct[matches[:, 1].long()] = matches[:, 2:3] >= iouv
        return correct
