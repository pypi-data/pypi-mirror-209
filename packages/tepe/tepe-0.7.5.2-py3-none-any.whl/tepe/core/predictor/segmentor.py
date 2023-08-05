import cv2
from loguru import logger
from matplotlib.pyplot import axes
import numpy as np

import torch
from torch import nn
from torchvision import transforms as T
from tepe.data.datasets.seg_voc_custom import voc_cmap
from tepe.utils.torch_utils import select_device, time_synchronized
from tepe.core.base_predictor import Predictor


class SegPredictor(Predictor):
    def __init__(self,
                 input_size,
                 classes,
                 model,
                 device=0,
                 half=False,
                 save_dir=None
                 ):
        super().__init__(save_dir)
        
        self.device = select_device(device)
        self.classes = classes
        self.pth = isinstance(model, nn.Module)
        self.half = half
        self.input_size = [input_size, input_size] if isinstance(input_size, int) else input_size
        if self.pth:
            self.model = model.eval()

            if self.device.type != 'cpu':
                self.model.cuda()
                self.model(torch.zeros(1, 3, *self.input_size).to(self.device).type_as(
                    next(self.model.parameters())))  # run once
        else:
            self.model = model

        self.preprocess = T.Compose([
                T.ToTensor(),
                T.Resize(self.input_size),
                T.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225]),
            ])
        self.color_map = voc_cmap()

    def __call__(self, img_meta):
        return self.draw(img_meta['img'], self.run(img_meta))

    def run(self, img_meta):
        img0 = img_meta['img']
        img = self.preprocess(img0).unsqueeze(0) # To tensor of NCHW
        if self.pth:
            img = img.to(self.device)
            if self.device.type == "cuda":
                if self.half:
                    img = img.half()  # to FP16
            
            t0 = time_synchronized()
            with torch.no_grad():
                pred = self.model(img)
            pred = pred.max(1)[1].cpu().numpy()[0] # HW

            logger.info("Infer time: {:.4f}s".format(time_synchronized() - t0))
        else:
            img = img.numpy()
            self.model.setInput(img)
            pred = self.model.forward()
            pred = np.argmax(pred, axis=1).squeeze()

        return pred

    def draw(self, img, output):
        label_map = self.color_map[output].astype('uint8')
        label_map = cv2.resize(label_map, (img.shape[1], img.shape[0]))
        label_map = cv2.cvtColor(label_map, cv2.COLOR_RGB2BGR)
        vis_res = cv2.addWeighted(img, 1, label_map, 0.3, 0)

        return vis_res


