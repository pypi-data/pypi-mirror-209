import os.path

import numpy as np
from loguru import logger
from matplotlib import pyplot as plt
import cv2
import torch
from tepe.utils.plots import colors
from tepe.utils.torch_utils import select_device, time_synchronized
from tepe.core import Predictor


class KeypointPredictor(Predictor):
    def __init__(self, input_size,
                 v2=False,
                 device=0,
                 model=None,
                 classes=None,
                 preprocess=None,
                 keypoint_thr=0.5,
                 dnn=False,
                 save_dir=None):
        super().__init__(save_dir)
        self.classes = classes
        self.input_size = input_size
        self.keypoint_thr = keypoint_thr
        self.device = select_device(device)
        self.v2 = v2

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
        preds, outputs = self.run(img_meta)
        result_image = self.draw(img_meta, preds, outputs)
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

        outputs = self.postprocess(preds)

        if self.pred2anno:
            self.save_annotation(img_meta, outputs)

        if len(outputs):
            scale_x, scale_y = img0.shape[1] / self.input_size[1], img0.shape[0] / self.input_size[0]
            outputs[:, 0] *= scale_x
            outputs[:, 1] *= scale_y

        return preds, outputs

    def run_cv(self, img):
        img = img.numpy()
        self.model.setInput(img)

        outputs = self.model.forward()
        outputs = outputs[0] if not self.v2 else outputs[-1]

        return outputs

    def run_torch(self, img):

        if "cuda" in self.device.type:
            img = img.cuda()

        with torch.no_grad():
            outputs = self.model(img)
            outputs = outputs if not self.v2 else outputs[-1]

        return outputs.squeeze(0).cpu().detach().numpy()

    def postprocess(self, preds):

        all_points = []
        for cls, heatmap in enumerate(preds):
            heatmap = cv2.resize(heatmap, self.input_size)
            _, bin_map = cv2.threshold(heatmap, self.keypoint_thr, 1, cv2.THRESH_BINARY)
            num_labels, labels, stats, center_loc = cv2.connectedComponentsWithStats(bin_map.astype(np.int8))

            for i in range(1, len(center_loc)):
                x = center_loc[i][0]
                y = center_loc[i][1]
                all_points.append([x, y, cls])

        return np.array(all_points, dtype='float32')

    def draw(self, img_meta, preds, outputs):
        if outputs is None:
            return img_meta['img']

        path, img = img_meta['path'], img_meta['img']
        kp_num = preds.shape[0]
        vis_res = img.copy()

        show_heatmap = getattr(self, 'show_heatmap', False)
        if show_heatmap:
            img_resize = cv2.resize(img, self.input_size)[:, :, [2, 1, 0]]
            for c in range(kp_num):
                plt.subplot(1, kp_num + 1, c + 1)
                plt.axis('off')
                heatmap = cv2.resize(preds[c], self.input_size)
                plt.imshow(img_resize)
                plt.imshow(heatmap, alpha=0.5)

                plt.subplot(1, kp_num + 1, kp_num + 1)
                plt.axis('off')
                plt.imshow(img_resize)

        scale_x, scale_y = img.shape[1] / self.input_size[1], img.shape[0] / self.input_size[0]
        for real_x, real_y, c in outputs:
            if show_heatmap:
                hex_color = colors(c, hex=True)
                pos_x, pos_y = real_x / scale_x, real_y / scale_y
                plt.scatter(pos_x, pos_y, s=60, c=hex_color)

            color = colors(c, bgr=True)
            cv2.circle(vis_res, (int(real_x), int(real_y)), 4, color, -1)

        if show_heatmap:
            if self.view_result:
                plt.show()
            if self.save_result:
                name, _ = os.path.splitext(os.path.basename(path))
                plt.savefig(f'{self.save_dir}/{name}_heatmap.jpg')
            plt.close()
        return vis_res

    def save_annotation(self, img_meta, outputs):
        from tepe.data.annotation import LabelmeJsonWriter

        save_anno_dir = os.path.join(self.save_dir, 'json')
        os.makedirs(save_anno_dir, exist_ok=True)

        img, img_path = img_meta['img'], img_meta['path']
        img_name = os.path.basename(img_path)
        scale_x, scale_y = img.shape[1] / self.input_size[1], img.shape[0] / self.input_size[0]

        writer = LabelmeJsonWriter(img_name, img.shape)
        for pos_x, pos_y, cls in outputs:
            real_x, real_y = pos_x * scale_x, pos_y * scale_y
            points = [[real_x, real_y]]
            writer.add_shape(1, points, self.classes[cls])

        save_json_path = os.path.join(save_anno_dir, img_name.rsplit('.', 1)[0] + '.json')
        writer.save(target_file=save_json_path)
