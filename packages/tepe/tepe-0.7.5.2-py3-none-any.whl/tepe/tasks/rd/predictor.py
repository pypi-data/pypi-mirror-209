import os
from typing import Optional, Callable
from scipy import ndimage as ndi
import cv2
import numpy as np
import torch
import torchvision
from loguru import logger
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter, maximum_filter

from skimage.feature import peak_local_max
from skimage import data, img_as_float

from tepe.core import Predictor as BasePredictor
from tepe.core.predictor.anomaly_detector import AnomalyDetector
from tepe.tasks.cfa.utils import denormalization
from tepe.utils import increment_path


class Predictor(BasePredictor, AnomalyDetector):
    def __init__(
            self,
            model: torch.nn.Module,
            input_size: int or tuple or list,
            resize_fn: Optional[Callable] = None,
            threshold: float = 0.5,
            transform: Optional[torchvision.transforms.Compose] = None,
            save_path: str = None,
            onnx_inf: bool = False,
            num_slice: int = 1
    ) -> None:
        super(Predictor, self).__init__(save_dir=save_path)
        self.model = model
        self.input_size = input_size
        self.resize_fn = resize_fn
        self.threshold = threshold
        self.transform = transform
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.onnx_inf = onnx_inf
        self.num_slice = num_slice

    def __call__(self, img_meta):
        results = self.run(img_meta)
        if not getattr(self, 'no_draw', False):
            results['dst'] = self.draw(img_meta['img'], results)

        return results

    def run(self, img_meta):
        img, path, is_vid, idx = img_meta['img'], img_meta['path'], img_meta['is_vid'], img_meta['idx']
        if isinstance(self.input_size, int):
            self.input_size = [self.input_size, self.input_size]

        inp = img
        ratio = (1, 1)
        dwh = (0, 0)
        if self.resize_fn:
            inp, ratio, dwh = self.resize_fn(img)
            assert dwh == (0, 0)
        if self.transform:
            inp = self.transform(inp)

        if self.onnx_inf:
            anomaly_map = self.model.run(
                None,
                {'images': inp.unsqueeze(0).numpy().astype('float32')}
            )[0]
        else:
            with torch.no_grad():
                anomaly_map = self.model(inp.unsqueeze(0).to(self.device))
            anomaly_map = anomaly_map.cpu().detach().numpy()



        anomaly_map = gaussian_filter(anomaly_map, sigma=4)

        anomaly_map = cv2.resize(anomaly_map, self.input_size)

        gray_map = np.uint8(anomaly_map * 255)
        im = img_as_float(gray_map)
        image_max = maximum_filter(im, size=10, mode='constant')
        # Comparison between image_max and im to find the coordinates of local maxima
        coordinates = peak_local_max(im, min_distance=35)  # 返回[行，列]，即[y, x]
        coordinates = coordinates[anomaly_map[coordinates[:, 0], coordinates[:, 1]] > 0.8*np.max(anomaly_map)]
        inp = inp.numpy() if isinstance(inp, torch.Tensor) else inp
        resized_img = denormalization(inp)

        if getattr(self, 'show_heatmap', False) and not is_vid:
            self.plot_fig(resized_img, anomaly_map,coordinates, path)

        mask = anomaly_map.copy()
        mask[mask > self.threshold] = 1
        mask[mask <= self.threshold] = 0

        mask *= 255
        mask = mask.astype(np.uint8)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        anomaly_area = []
        for contour in contours:
            contour = cv2.approxPolyDP(contour, len(contours), True)
            x, y, w, h = cv2.boundingRect(contour)
            if w < 17 or h < 17 or w*h<1200:
                continue
            x1, y1 = round((x - dwh[0]) / ratio[0]), round((y - dwh[1]) / ratio[1])
            x2, y2 = round(x1 + w / ratio[0]), round(y1 + h / ratio[1])
            anomaly_area.append([x1, y1, x2, y2])

        if getattr(self, 'save_xml', False):
            if is_vid:
                logger.warning('Source is video, can not save results to xml.')

            save_xml_dir = getattr(self, 'save_xml_dir')
            self.save_xml_dir = save_xml_dir if save_xml_dir is not None \
                else os.path.join(self.save_dir, 'predict')
            os.makedirs(self.save_xml_dir, exist_ok=True)
            self.save_result_to_xml(path, img.shape, anomaly_area, self.save_xml_dir)

        return dict(
            anomaly_area=anomaly_area
        )

    def draw(self, img: np.ndarray, results) -> np.ndarray:
        for rect in results['anomaly_area']:
            x1, y1, x2, y2 = rect
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        return img

    def plot_fig(self, resize_img, anomaly_map,coordinates, path):
        fig = plt.figure()
        ax0 = fig.add_subplot(221)
        ax0.axis('off')
        ax0.imshow(resize_img)
        ax0.title.set_text('Image')

        ax2 = fig.add_subplot(222)
        ax2.axis('off')
        ax2.imshow(resize_img, cmap='gray', interpolation='none')
        ax2.imshow(anomaly_map, cmap='jet', alpha=0.5, interpolation='none')
        ax2.title.set_text('Predicted heat map')

        ax3 = fig.add_subplot(223)
        ax3.axis('off')
        ax3.imshow(resize_img, cmap='gray', interpolation='none')
        ax3.plot(coordinates[:, 1], coordinates[:, 0], 'r.', marker='o')
        # ax3.imshow(anomaly_map, cmap='jet', alpha=0.5, interpolation='none')
        ax3.title.set_text('Predicted key point')

        fig.tight_layout()

        if self.view_result:
            plt.show()

        if self.save_result:
            basename = os.path.basename(path)
            name, suffix = os.path.splitext(basename)
            fig.savefig(f'{self.save_dir}/{name}_heatmap{suffix}', dpi=100)

        plt.close()