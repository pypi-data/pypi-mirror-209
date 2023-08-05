import torch

from .data.batch_process import stack_batch_img
from .data.collate import naive_collate
from .data.transform import Pipeline
from .util import load_model_weight
from tepe.core import Predictor as BasePredictor


class Predictor(BasePredictor):
    def __init__(self, cfg, model_path, device="cuda:0", save_dir=None):
        super(Predictor, self).__init__(save_dir=save_dir)
        self.cfg = cfg
        self.device = device
        model = cfg.build_model()
        ckpt = torch.load(model_path, map_location=lambda storage, loc: storage)
        load_model_weight(model, ckpt)
        if cfg.backbone.name == "RepVGG":
            cfg.backbone.update({"deploy": True})
            deploy_model = cfg.build_model()
            from .model.backbone.repvgg import repvgg_det_model_convert

            model = repvgg_det_model_convert(model, deploy_model)
        self.model = model.to(device).eval()
        self.pipeline = Pipeline(cfg.val_pipeline, cfg.keep_ratio)

    def __call__(self, img_meta):
        meta, res = self.run(img_meta)
        result_image = self.draw(res[0], meta)
        return result_image

    def run(self, img_meta):
        img = img_meta['img']
        img_info = {"id": 0}
        img_info["file_name"] = None
        height, width = img.shape[:2]
        img_info["height"] = height
        img_info["width"] = width
        meta = dict(img_info=img_info, raw_img=img, img=img)
        meta = self.pipeline(None, meta, self.cfg.input_size)
        meta["img"] = torch.from_numpy(meta["img"].transpose(2, 0, 1)).to(self.device)
        meta = naive_collate([meta])
        meta["img"] = stack_batch_img(meta["img"], divisible=32)
        with torch.no_grad():
            results = self.model.inference(meta)
        return meta, results

    def draw(self, dets, meta):
        result_img = self.model.head.show_result(
            meta["raw_img"][0], dets, self.cfg.class_names,
            score_thres=self.cfg.conf_thre, show=False
        )
        return result_img
