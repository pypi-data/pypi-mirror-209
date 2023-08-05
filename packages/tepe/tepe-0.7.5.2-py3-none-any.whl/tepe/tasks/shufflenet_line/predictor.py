import os.path

import numpy as np
from loguru import logger
from matplotlib import pyplot as plt
import cv2
import torch
from tepe.utils.plots import colors
from tepe.utils.torch_utils import select_device, time_synchronized
from tepe.core import Predictor


class LinePredictor(Predictor):
    def __init__(self, input_size,
                 v2=False,
                 device=0,
                 model=None,
                 classes=None,
                 preprocess=None,
                 line_thr=0.5,
                 dnn=False,
                 save_dir=None):
        super().__init__(save_dir)
        self.classes = classes
        self.input_size = input_size
        self.line_thr = line_thr
        self.device = select_device(device)

        self.onnx = dnn
        if self.onnx:
            self.model = model
            logger.info('OpenCV DNN backend.')
        else:
            self.model = model.eval()

            if self.device.type != 'cpu':
                self.model.cuda()
                self.model(torch.zeros(1, 3, *input_size).to(self.device).type_as(
                    next(self.model.parameters())))  # run once

        self.preprocess = preprocess

    def __call__(self, img_meta):
        preds, lines = self.run(img_meta)
        result_image = self.draw(img_meta, preds, lines)
        return result_image

    def run(self, img_meta):
        img0 = img_meta['img']
        if self.preprocess is not None:
            img = self.preprocess(img0)
            img = img.unsqueeze(0)
        if self.onnx:
            preds = self.run_cv(img)
        else:
            preds = self.run_torch(img)

        lines = self.extract_lines(preds)

        scale_x, scale_y = img0.shape[1] / self.input_size[1], img0.shape[0] / self.input_size[0]
        lines[:, 0] *= scale_x
        lines[:, 1] *= scale_y
        lines[:, 2] *= scale_x
        lines[:, 3] *= scale_y

        return preds, lines

    def run_cv(self, img):
        img = img.numpy()
        self.model.setInput(img)

        outputs = self.model.forward()[-1]
        return outputs

    def run_torch(self, img):

        if "cuda" in self.device.type:
            img = img.cuda()

        with torch.no_grad():
            outputs = self.model(img)[-1]

        return outputs.squeeze(0).cpu().detach().numpy()

    def extract_lines(self, preds):
        lines = []
        for cls, heatmap in enumerate(preds):
            heatmap = cv2.resize(heatmap, self.input_size)
            _, bin_map = cv2.threshold(heatmap, self.line_thr, 255, cv2.THRESH_BINARY)
            bin_map = bin_map.astype(np.uint8)
            contours, hierarchy = cv2.findContours(bin_map, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if not contours:
                continue
            contours = np.concatenate(contours, axis=0).squeeze(axis=1)  # 所有的轮廓点

            xmin = np.min(contours[:,0])
            xmax = np.max(contours[:,0])
            ymin = np.min(contours[:,1])
            ymax = np.max(contours[:,1])

            vx, vy, x0, y0 = cv2.fitLine(contours, cv2.DIST_L1, 0, 0.01, 0.01)
            if vx == 0:
                pt1, pt2 = [x0, ymin], [x0, ymax]
            else:  # y = k * x + b
                k = float(vy / vx)
                b = float(y0 - k*x0)
                if abs(k) > 1:
                    pt1, pt2 = [(ymin - b)/k, ymin], [(ymax - b)/k, ymax]
                else:
                    pt1, pt2 = [xmin, k*xmin + b], [xmax, k*xmax + b]

            lines.append(pt1 + pt2 + [cls])  # [x1, y1, x2, y2, cls]
        return np.array(lines, dtype=np.float32)

    def draw(self, img_meta, preds, lines):
        if lines is None or not len(lines):
            return img_meta['img']
            
        path, img = img_meta['path'], img_meta['img']
        line_num = preds.shape[0]
        vis_res = img.copy()

        lines = lines.round().astype(np.int32)
        for c, line in enumerate(lines):
            color = colors(c, bgr=True)
            pt1, pt2 = line[:2], line[2:4]
            vis_res = cv2.line(vis_res, pt1, pt2, color, 3)
            vis_res = cv2.circle(vis_res, pt1, 2, (255, 0, 0), -1)
            vis_res = cv2.circle(vis_res, pt2, 2, (0, 255, 0), -1)

        show_heatmap = getattr(self, 'show_heatmap', False)
        if show_heatmap:
            img_resize = cv2.resize(img, self.input_size)[:, :, [2, 1, 0]]
            for c in range(line_num):
                plt.subplot(1, line_num + 1, c + 1)
                plt.axis('off')
                heatmap = cv2.resize(preds[c], self.input_size)
                plt.imshow(img_resize)
                plt.imshow(heatmap, alpha=0.5)

            plt.subplot(1, line_num + 1, line_num + 1)
            plt.axis('off')
            plt.imshow(img_resize)

        if show_heatmap:
            if self.view_result:
                plt.show()
            if self.save_result:
                name, _ = os.path.splitext(os.path.basename(path))
                plt.savefig(f'{self.save_dir}/{name}_heatmap.jpg')
            plt.close()
        return vis_res