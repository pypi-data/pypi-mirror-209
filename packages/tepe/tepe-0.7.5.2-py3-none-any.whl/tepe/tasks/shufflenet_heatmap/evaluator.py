import os.path

import numpy as np
import cv2
from matplotlib import pyplot as plt
import torch
from tepe.core import Evaluator as BaseEvaluator
from tepe.utils import time_synchronized

class Evaluator(BaseEvaluator):
    def __init__(self, dataloader, v2=False, **kwargs):
        super().__init__(dataloader, **kwargs)
        self.v2 = v2
        self.metrics.compute_paf_loss = False

    def evaluate_one_iter(self, data):
        idx, paths = data['idx'], data['path']
        data['img'] = data['img'].to(self.device, non_blocking=True)
        data['target'] = data['target'].to(self.device, non_blocking=True)

        with torch.no_grad():
            start = time_synchronized()

            preds = self.model(data['img'])
            loss_dict = self.metrics(preds, data)

            infer_end = time_synchronized()
            self.inference_time += (infer_end - start)

        if self.iter == 0:
            preds = preds[-1] if self.v2 else preds
            self.visual_add_image_with_heatmap(data['img'], preds, data['target'], paths)

        return loss_dict

    def visual_add_image_with_heatmap(self, images, preds, labels, paths):
        fig = plt.figure(figsize=(10, 10), dpi=100)
        plt.clf()

        label0 = labels[0].cpu().detach().numpy()
        pred0 = preds[0].cpu().detach().numpy()
        image0 = images[0].cpu().detach().numpy().transpose(1, 2, 0)

        std = self.dataloader.dataset.transform.transform[-1].std
        mean = self.dataloader.dataset.transform.transform[-1].mean
        image0 = image0 * np.array(std) * 255
        image0 = image0 + np.array(mean) * 255
        image0 = image0.astype(np.uint8)
        h, w = image0.shape[0:2]

        kp_num = label0.shape[0]

        for kp_c in range(kp_num):
            plt.subplot(2, kp_num, kp_c + 1)
            plt.imshow(image0)
            plt.imshow(cv2.resize(pred0[kp_c], (w, h)), alpha=0.5)

        for kp_c in range(kp_num):
            plt.subplot(2, kp_num, kp_num + kp_c + 1)
            plt.imshow(image0)
            plt.imshow(cv2.resize(label0[kp_c], (w, h)), alpha=0.5)

        self.result_imgs[os.path.basename(paths[0])] = fig

