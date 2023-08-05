import copy
import json
import math
import os
from pathlib import Path
import random

import albumentations as A
import cv2
import matplotlib
import numpy as np
from loguru import logger
from matplotlib import pyplot as plt
from torch.utils.data import Dataset

try:
    matplotlib.use('TkAgg')
except:
    pass

from tepe.data.utils import IMG_FORMATS


class Albumentations:
    # Albumentations class (optional, only used if package is installed)
    # pip install albumentations
    def __init__(self, transform):
        self.transform = transform

        logger.info('albumentations:\n' + '\n'.join(f'{x}' for x in self.transform.transforms if x.p))

    def __call__(self, im, labels, p=1.0):
        if self.transform and random.random() < p:
            num_line = len(labels)
            # decode
            kpt = np.concatenate([labels[:, :2], labels[:, 2:4]], axis=0)
            kpt[:, 0] *= im.shape[1]
            kpt[:, 1] *= im.shape[0]
            class_labels = np.concatenate([labels[:, -1], labels[:, -1]], axis=0)

            new = self.transform(image=im, keypoints=kpt, class_labels=class_labels)  # transformed
            im, new_kpt = new['image'], np.array(new['keypoints'])
            new_kpt[:, 0] /= im.shape[1]
            new_kpt[:, 1] /= im.shape[0]
            new_line = np.concatenate([new_kpt[:num_line, :], new_kpt[num_line:, :]], axis=1)
            labels = np.array([[*l, c] for l, c in zip(new_line, new['class_labels'][:num_line])])

        return im, labels


class LineDataset(Dataset):
    def __init__(self, img_dir, ann_dir, num_line_cls, transform=None, class_name=(),
                 is_train=False, imgsz=224, stride=8):

        self.img_dir = img_dir
        self.ann_dir = ann_dir
        class_name = list(range(num_line_cls)) if not class_name else class_name
        self.class_name = {cls: idx for idx, cls in enumerate(class_name)}
        if num_line_cls != len(self.class_name):
            logger.info("override number of keypoint classes")
        self.num_line_cls = len(self.class_name)

        self.transform = transform
        if isinstance(transform, A.Compose):
            self.transform = Albumentations(transform)

        imgsz = [imgsz, imgsz] if isinstance(imgsz, int) else imgsz
        input_h, input_w = imgsz
        self.input_size = self.heatmap_h, self.heatmap_w = input_h, input_w
        self.stride = stride
        # self.line_thickness = 1 * (input_w // 224) if input_w > 224 else 1
        self.line_thickness = 1

        self.data = self.parse_data()

        logger.info(f'class name: {self.class_name}')

        desc = 'train' if is_train else 'val'
        desc += f': found {len(self.data)} images'
        logger.info(desc)

    def get_data(self, img_name):
        img_path = os.path.join(self.img_dir, img_name)
        if not os.path.exists(img_path):
            logger.info(f"{img_path} is not exists")
            return None, None
        suffix = Path(img_name).suffix
        json_path = os.path.join(self.ann_dir, img_name.replace(suffix, '.json'))
        if not os.path.exists(json_path):
            logger.info(f"{img_path}'s label is not exists")
            return None, None
        return img_path, self.read_label(json_path)

    def read_label(self, json_path):
        with open(json_path, 'r') as f:
            json_dict = json.load(f)
        img_width, img_height = json_dict["imageWidth"], json_dict["imageHeight"]
        shapes = [shape for shape in json_dict['shapes'] if shape["shape_type"] == "line"]
        # sort shapes
        # shapes.sort(key=lambda x: float(x['points'][0][0]) + float(x['points'][0][1]))

        labels = []
        for shape in shapes:
            if shape["label"] not in self.class_name:
                continue
            cls = self.class_name[shape["label"]]
            points = shape["points"]
            pt1, pt2 = points
            x1, y1 = pt1
            x2, y2 = pt2
            # normalize
            x1 /= img_width
            y1 /= img_height
            x2 /= img_width
            y2 /= img_height
            label = np.array([x1, y1, x2, y2, cls], dtype=np.float32)
            labels.append(label)

        return labels

    def __getitem__(self, idx):
        img_path, label_ori = self.data[idx]
        labels = copy.deepcopy(label_ori)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.transform is not None:
            img, labels = self.transform(img, labels)

        img = img.transpose(2, 0, 1)

        target = self.generate_target(labels)

        meta_data = dict(img=img, path=img_path, target=target, idx=idx)

        return meta_data

    def __len__(self):
        return len(self.data)

    def parse_data(self):
        data = []
        for name in os.listdir(self.img_dir):
            suffix = Path(name).suffix
            if suffix[1:] not in IMG_FORMATS:
                continue
            path, label = self.get_data(name)
            if label is None or not label:
                continue
            data.append((path, np.stack(label, axis=0)))
        return data

    def generate_target(self, line_points: np.ndarray):
        tgt_h, tgt_w = self.input_size[0] // self.stride, self.input_size[1] // self.stride
        targets = np.zeros(
            shape=(self.num_line_cls, tgt_h, tgt_w),
            dtype=np.float32
        )

        line_points[:,0] *= tgt_w
        line_points[:,1] *= tgt_h
        line_points[:,2] *= tgt_w
        line_points[:,3] *= tgt_h
        line_points = line_points.round().astype(np.int32)
        for line in line_points:
            pt1 = line[:2]
            pt2 = line[2:4]
            cls_id = line[-1]
            heatmap = targets[cls_id]
            heatmap = cv2.line(heatmap, pt1, pt2, color=255, thickness=self.line_thickness)
            heatmap = cv2.GaussianBlur(heatmap, (3,3), 0.0)

        targets /= 255.0

        return targets

    @staticmethod
    def split_train_val(root):
        image_list = []
        folder_path = os.path.join(root, 'images')
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            image_list += [name + '\n' for name in os.listdir(folder_path)
                           if name.split('.')[-1] in ['jpg', 'png']]

        random.shuffle(image_list)
        num_images = len(image_list)
        num_train = int(0.75 * num_images)
        train_images = image_list[:num_train]
        val_images = image_list[num_train:]

        random.shuffle(train_images)
        random.shuffle(val_images)

        ftrain = open(os.path.join(root, 'train.txt'), 'w')
        ftrain.writelines(train_images)
        ftrain.close()
        fval = open(os.path.join(root, 'val.txt'), 'w')
        fval.writelines(val_images)
        fval.close()

        logger.info(f'train.txt and val.txt are generated in {root}')

    @staticmethod
    def visual_add_image_with_heatmap(images, labels):
        """
        Args:
            images: (np.ndarray)
            labels:

        Returns:

        """
        fig = plt.figure(figsize=(10, 10), dpi=100)
        plt.clf()

        label0 = labels
        images = images.transpose(1, 2, 0)
        images *= np.array([57.12, 58.395, 57.375])
        images += np.array([123.675, 103.53, 116.28])
        image0 = images.astype(np.uint8)
        h, w = image0.shape[0:2]

        kp_num = label0.shape[0]
        for kp_c in range(kp_num):
            plt.subplot(2, kp_num, kp_c + 1)
            plt.imshow(image0)

        for kp_c in range(kp_num):
            plt.subplot(2, kp_num, kp_num + kp_c + 1)
            plt.imshow(image0)
            plt.imshow(cv2.resize(label0[kp_c], (w, h)), alpha=0.5)

        # plt.savefig('./tran_%d.jpg' % epoch)
        plt.show()


if __name__ == '__main__':
    RESIZE = (512, 512)

    transform = A.Compose([
        A.Resize(RESIZE[0], RESIZE[1], p=1),
        A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.4),
        A.Rotate(limit=15, border_mode=cv2.BORDER_REPLICATE, p=0.3),
        A.OneOf([
            A.HueSaturationValue(p=0.4),
            A.ChannelShuffle(p=0.5)
        ], p=1),
        A.Normalize(),
        # ToTensorV2()
    ], keypoint_params=A.KeypointParams(format='xy', label_fields=['class_labels']))

    data_path = '/home/zepei/data/DATA/meter/dataset/samll_meter/yolo_h_1'
    dataset_train = LineDataset(
        img_dir='/home/zepei/data/DATA/meter/state_meter/data/3/pointer',
        ann_dir='/home/zepei/data/DATA/meter/state_meter/data/3/pointer',
        transform=transform,
        num_line_cls=2,
        class_name=['pointer_line', 'bottom'],
        is_train=True,
        imgsz=RESIZE
    )
    print('dataset size:', len(dataset_train))
    # for idx in range(10):
    data = dataset_train[2]
    image, label = data['img'], data['target']
    image = image.transpose(1, 2, 0)
    print(image.shape)
    print(label.shape)
    cv2.imshow('img', image)
    cv2.imshow('label1', label[0] * 255)
    cv2.imshow('label2', label[1] * 255)
    cv2.waitKey()
