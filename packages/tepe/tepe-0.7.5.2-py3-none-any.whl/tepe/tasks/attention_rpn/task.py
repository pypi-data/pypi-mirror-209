import os

import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass
from mmdet.apis import show_result_pyplot
from tepe.tasks.attention_rpn.pipelines import *

from tepe.tasks.attention_rpn.inference import init_detector, inference_detector, process_support_images
from tepe.core import BaseTask
from tepe.utils import ROOT


class AttentionRPNConfig(BaseTask):
    def __init__(self):
        super(AttentionRPNConfig, self).__init__()
        self.task_name = 'attention_rpn'
        self.config_file = os.path.join(ROOT, 'tepe', 'tasks', 'attention_rpn', 'all_config.py')
        self.support_images_dir = ''
        self.weights = ''

        self.device = 'cuda:0'
        self.score_thr = 0.7

    def get_model(self, train=True):
        pass

    def get_train_loader(self):
        pass

    def predict(self, source, view_img=False, save_img=True):
        """
        Examples:
            tepe predict -t configs/samples/attention_rpn.py \
                -s /home/zepei/data/DATA/meter/tese_data/test3.png \
                -w /home/zepei/.cache/torch/hub/checkpoints/attention-rpn_r50_c4_4xb2_coco_base-training_20211102_003348-da28cdfd.pth \
                support-images-dir /home/zepei/data/DATA/meter/tese_data/support
        """

        # build the model from a config file and a checkpoint file
        model = init_detector(self.config_file, self.weights, device=self.device)
        # prepare support images, each demo image only contain one instance
        files = os.listdir(self.support_images_dir)
        support_images = [
            os.path.join(self.support_images_dir, file) for file in files
        ]
        classes = [file.split('.')[0] for file in files]
        support_labels = [[file.split('.')[0]] for file in files]
        process_support_images(
            model, support_images, support_labels, classes=classes)
        # test a single image
        result = inference_detector(model, source)
        # show the results
        show_result_pyplot(model, source, result, score_thr=self.score_thr)

    def export(self):
        model = init_detector(self.config_file, self.weights, device=self.device)
        pass
