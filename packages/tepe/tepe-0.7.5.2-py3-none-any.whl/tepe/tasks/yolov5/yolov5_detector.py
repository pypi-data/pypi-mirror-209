from typing import Optional, Union, Callable, List, Dict, Tuple
from pathlib import Path
from typing import Dict
from loguru import logger
import numpy as np
import cv2
import torch

from tepe.utils.torch_utils import select_device
from . import letterbox, non_max_suppression, scale_coords, Annotator, colors
from tepe.core.base_predictor import Predictor


class YOLOv5Predictor(Predictor):
    def __init__(self, 
        save_dir=None,
        weights=None,
        model=None,
        classes=None,
        imgsz=640,  # inference size (pixels)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device=0,  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        half=False,  # use FP16 half-precision inference
        dnn=False,  # use OpenCV DNN for ONNX inference
        ):
        super().__init__(save_dir)

        # Initialize
        self.device = select_device(device)
        half &= self.device.type != 'cpu'  # half precision only supported on CUDA
        self.half = half
        self.classes = classes
        if isinstance(imgsz, int):
            imgsz = [imgsz, imgsz]

        self.pt = Path(weights).suffix in ['.pt', '.pth']
        onnx = Path(weights).suffix == '.onnx'
        if model:
            self.pt = True
            model.to(self.device)
            if self.half:
                model.half()  # to FP16
            if self.device.type != 'cpu':
                model(torch.zeros(1, 3, *imgsz).to(device).type_as(next(model.parameters())))  # run once
        elif onnx:
            logger.info('OpenCV DNN backend.')
            model = cv2.dnn.readNetFromONNX(weights)
        else:
            raise Exception('only suport pth model and onnx model.')

        self.model = model
        self.img_size = imgsz
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.max_det = max_det
        self.agnostic_nms = agnostic_nms

    def __call__(self, img_meta: Dict) -> np.ndarray:
        return self.draw(img_meta['img'], self.run(img_meta))

    def run(self, img_meta: Dict):
        """
        args:
            img_meta: dict contains img and path
        return :
            detection: list of [x1, y1, x2, y2, conf, cls]
        """
        im0 = img_meta['img']
        img = letterbox(im0, self.img_size, auto=self.pt, stride=32)[0]
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)
        if self.pt:
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
        else:
            img = img.astype('float32')

        img /= 255  # 0 - 255 to 0.0 - 1.0
        if len(img.shape) == 3:
            img = img[None]  # expand for batch dim
        
        input_shape = img.shape
        # Inference
        if self.pt:
            with torch.no_grad():
                pred = self.model(img, augment=False, visualize=False)[0]
        else:
            self.model.setInput(img)
            outs = self.model.forward()
            pred = torch.tensor(outs)

        # NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, 
                                   agnostic=self.agnostic_nms,
                                   max_det=self.max_det)
        det = pred[0]
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(input_shape[2:], det[:, :4], im0.shape).round()
        return det.cpu().detach().numpy()

    def draw(self, im0, det) -> np.ndarray:
        # Process predictions
        annotator = Annotator(im0, line_width=3, example='abc')
        if len(det):

            # Write results
            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                label = f'{self.classes[c]} {conf:.2f}'
                annotator.box_label(xyxy, label, color=colors(c, True))
        
        # Stream results
        im0 = annotator.result()
        
        return im0
    
    def annotate(self, 
                 source: Union[str, Path],
                 format: str = "labelme", 
                 target: Optional[Union[str, Path]] = None,) -> None:
        """将yolov5预测结果保存到标注文件

        Args:
            source (str | Path): 图片/视频路径
            format (str, optional): 保存标注的格式，目前支持json和voc格式. Defaults to "labelme".
            target (Optional[Union[str, Path]], optional): 标注文件保存的文件夹路径. 默认保存在output_dir下.

        Raises:
            NotImplementedError: 基类不实现
        """
        if target is None:
            target = Path(self.save_dir) / 'annotations'
        target = Path(target)
        if not target.exists():
            target.mkdir(exist_ok=True)

        from tepe.data.annotation import LabelmeJsonWriter, PascalVocWriter

        dataset = self._parse_source(source)

        num_img = 0
        for path, img0, vid_cap, idx in dataset:
            """
            img0: BRG image, HWC
            """
            if not vid_cap:
                logger.info("file: " + path)

            img_meta = dict(img=img0, path=path, is_vid=dataset.mode != 'image', idx=idx)

            det = self.run(img_meta)

            if len(det):
                img_name = Path(path).name
                suffix = Path(img_name).suffix
                if vid_cap:
                    img_name = img_name.replace(suffix, f'-{dataset.frame}{suffix}')

                if format == 'labelme':
                    writer = LabelmeJsonWriter(img_name, img0.shape)
                else:
                    writer = PascalVocWriter('VOC2007', img_name, img0.shape)
                # Write results
                for *xyxy, conf, cls in reversed(det):
                    p1, p2 = [int(xyxy[0]), int(xyxy[1])], [int(xyxy[2]), int(xyxy[3])]
                    c = int(cls)  # integer class
                    label = self.classes[c]
                    if format == 'labelme':
                        writer.add_shape(shape_type=2, points=[p1, p2], label=label)
                    else:
                        writer.add_bnd_box(x_min=p1[0], y_min=p1[1], x_max=p2[0], y_max=p2[1], name=label)

                target_file = target / img_name.replace(
                    suffix, '.json' if format == 'labelme' else '.xml')
                writer.save(str(target_file))
        logger.info(f"save annotations in {str(target)}")
