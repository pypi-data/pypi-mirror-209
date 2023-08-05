import copy
import json
import math
import os
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


class Albumentations:
    # Albumentations class (optional, only used if package is installed)
    # pip install albumentations
    def __init__(self, transform):
        self.transform = transform

        logger.info('albumentations:\n' + '\n'.join(f'{x}' for x in self.transform.transforms if x.p))

    def __call__(self, im, labels, p=1.0):
        if self.transform and random.random() < p:
            # decode
            kp = labels[:, :2]
            kp[:, 0] *= im.shape[1]
            kp[:, 1] *= im.shape[0]

            new = self.transform(image=im, keypoints=kp, class_labels=labels[:, 2])  # transformed
            im, labels = new['image'], np.array([[*k, c] for k, c in zip(new['keypoints'], new['class_labels'])])
            labels[:, 0] /= im.shape[1]
            labels[:, 1] /= im.shape[0]

        return im, labels


class KeyPointsDataset(Dataset):
    def __init__(self, root, num_keypoint_cls, transform=None, class_name=(), image_sets=None,
                 is_train=False, imgsz=224, stride=8, body_part_kpt_ids=(),
                 gauss_ratio=1, gauss_sigma=0.5):
        self.root = root
        class_name = list(range(num_keypoint_cls)) if not class_name else class_name
        self.class_name = {cls: idx for idx, cls in enumerate(class_name)}
        if num_keypoint_cls != len(self.class_name):
            logger.info("override number of keypoint classes")
        self.kp_num = len(self.class_name)

        self.transform = transform
        if isinstance(transform, A.Compose):
            self.transform = Albumentations(transform)
        self.data = []

        imgsz = [imgsz, imgsz] if isinstance(imgsz, int) else imgsz
        input_h, input_w = imgsz
        self.input_size = self.heatmap_h, self.heatmap_w = input_h, input_w
        self.gauss_ratio = gauss_ratio * stride * (input_w // 224)
        self.gauss_sigma = gauss_sigma * stride
        self.stride = stride
        self.body_part_kpt_ids = body_part_kpt_ids

        is_dir = True if image_sets is None else False
        if is_dir:
            for name in os.listdir(root):
                if name.split('.')[-1] not in ['jpg', 'png']:
                    continue
                path, label = self.get_data(name)
                if label is None or not label:
                    continue
                self.data.append((path, np.stack(label, axis=0)))
        else:
            if not isinstance(image_sets, list):
                image_sets = [image_sets]
            is_txt = True
            txt_paths = []
            for dset in image_sets:
                txt = os.path.join(root, dset + '.txt')
                txt_paths.append(txt)
                is_txt &= os.path.exists(txt)
            # split dataset
            if not is_txt:
                logger.info(f'Not found {image_sets}.txt, generate it.')
                self.split_train_val(root)
                txt_name = 'train' if is_train else 'val'
                txt_paths = [os.path.join(root, txt_name + '.txt')]
            for txt in txt_paths:
                with open(txt, 'r') as f:
                    for line in f:
                        name = line.strip()
                        path, label = self.get_data(name)
                        if label is None or not label:
                            continue
                        self.data.append((path, np.stack(label, axis=0)))

        logger.info(f'class name: {self.class_name}')

        desc = 'train' if is_train else 'val' if not is_dir else 'IMG'
        desc += f': found {len(self.data)} images'
        logger.info(desc)

    def get_data(self, img_name):
        img_path = os.path.join(self.root, 'images', img_name)
        if not os.path.exists(img_path):
            logger.info(f"{img_path} is not exists")
            return None, None
        suffix = img_name.split('.')[-1]
        json_path = os.path.join(self.root, 'json', img_name.replace(suffix, 'json'))
        if not os.path.exists(json_path):
            logger.info(f"{img_path}'s label is not exists")
            return None, None
        return img_path, self.read_label(json_path)

    def read_label(self, json_path):
        with open(json_path, 'r') as f:
            json_dict = json.load(f)
        img_width, img_height = json_dict["imageWidth"], json_dict["imageHeight"]
        shapes = [shape for shape in json_dict['shapes'] if shape["shape_type"] != "rectangle"]
        # sort shapes
        # shapes.sort(key=lambda x: float(x['points'][0][0]) + float(x['points'][0][1]))

        labels = []
        for shape in shapes:
            cls = self.class_name[shape["label"]]
            points = shape["points"]
            x, y = points[0][0], points[0][1]
            # normalize
            x /= img_width
            y /= img_height
            label = np.array([x, y, cls], dtype=np.float32)
            labels.append(label)
        # for shape in shapes:
        #     for cls, (x, y) in enumerate(shape["points"]):
        #         # normalize
        #         x /= img_width
        #         y /= img_height
        #         label = np.array([x, y, cls], dtype=np.float32)
        #         labels.append(label)
        return labels

    def __getitem__(self, idx):
        img_path, label_ori = self.data[idx]
        labels = copy.deepcopy(label_ori)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.transform is not None:
            img, labels = self.transform(img, labels)

        img = img.transpose(2, 0, 1)

        kpt_maps = self.generate_target(labels)

        if self.body_part_kpt_ids:
            paf_maps = self._generate_paf_maps(labels)
            meta_data = dict(img=img, path=img_path, target=kpt_maps, paf_maps=paf_maps, idx=idx)
        else:
            meta_data = dict(img=img, path=img_path, target=kpt_maps, idx=idx)
        return meta_data

    def __len__(self):
        return len(self.data)

    def generate_target(self, labels):
        """

        :param labels:  [num_joints, 3]
        :param joints_vis: [num_joints, 3]
        :return: target, target_weight(1: visible, 0: invisible)
        """

        target = np.zeros((
            self.heatmap_h,
            self.heatmap_w,
            self.kp_num
            ), dtype=np.float32)

        tmp_size = self.gauss_ratio

        for kp_id in range(labels.shape[0]):
            label = labels[kp_id]
            kp_cls = int(label[2])
            heatmap = target[...,kp_cls]
            mu_x = int(label[0] * self.heatmap_w + 0.5)
            mu_y = int(label[1] * self.heatmap_h + 0.5)

            # Check that any part of the gaussian is in-bounds
            ul = [int(mu_x - tmp_size), int(mu_y - tmp_size)]
            br = [int(mu_x + tmp_size + 1), int(mu_y + tmp_size + 1)]
            if ul[0] >= self.heatmap_w or ul[1] >= self.heatmap_h \
                    or br[0] < 0 or br[1] < 0:
                continue

            # Generate gaussian
            size = 2 * tmp_size + 1
            x = np.arange(0, size, 1, np.float32)
            y = x[:, np.newaxis]
            x0 = y0 = size // 2
            # The gaussian is not normalized, we want the center value to equal 1
            g = np.exp(- ((x - x0) ** 2 + (y - y0) ** 2) / (2 * self.gauss_sigma ** 2))

            # Usable gaussian range
            g_x = max(0, -ul[0]), min(br[0], self.heatmap_w) - ul[0]
            g_y = max(0, -ul[1]), min(br[1], self.heatmap_h) - ul[1]
            # Image range
            img_x = max(0, ul[0]), min(br[0], self.heatmap_w)
            img_y = max(0, ul[1]), min(br[1], self.heatmap_h)

            heatmap[img_y[0]:img_y[1], img_x[0]:img_x[1]] = g[g_y[0]:g_y[1], g_x[0]:g_x[1]]

        tgt_h, tgt_w = self.heatmap_h // self.stride, self.heatmap_w // self.stride
        target = cv2.resize(target, (tgt_w, tgt_h)).reshape(tgt_w, tgt_h, -1).transpose(2, 0, 1)
        return target

    def _generate_paf_maps(self, keypoints):
        n_pafs = len(self.body_part_kpt_ids)
        assert n_pafs > 0
        n_rows, n_cols = self.input_size

        paf_maps = np.zeros(shape=(n_pafs * 2, n_rows // self.stride, n_cols // self.stride), dtype=np.float32)

        self._paf_thickness = 2
        for paf_idx in range(n_pafs):
            ai, bi = self.body_part_kpt_ids[paf_idx][0], self.body_part_kpt_ids[paf_idx][1]
            if ai >= len(keypoints) or bi >= len(keypoints): continue
            keypoint_a, keypoint_b = keypoints[ai], keypoints[bi]

            self._set_paf(paf_maps[paf_idx * 2:paf_idx * 2 + 2],
                          keypoint_a[0], keypoint_a[1], keypoint_b[0], keypoint_b[1],
                          self.stride, self._paf_thickness)

        return paf_maps

    def _generate_segment_maps(self, keypoints):
        n_rows, n_cols = self.input_size
        seg_maps = np.zeros(shape=(2, n_rows // self.stride, n_cols // self.stride), dtype=np.uint8)

        for keypoint in keypoints:
            kp = keypoint[:,:2]
            kp /= self._stride
            kp = np.array([kp]).reshape(1, -1, 2).round().astype(np.int32)
            seg_maps[0] = cv2.polylines(seg_maps[0], kp, isClosed=False, color=255, thickness=self._paf_thickness)

        paf_maps = seg_maps / 255
        paf_maps[-1] = 1 - paf_maps[0]

        return paf_maps

    def _set_paf(self, paf_map, x_a, y_a, x_b, y_b, stride, thickness):
        x_a /= stride
        y_a /= stride
        x_b /= stride
        y_b /= stride
        x_ba = x_b - x_a
        y_ba = y_b - y_a
        _, h_map, w_map = paf_map.shape
        x_min = int(max(min(x_a, x_b) - thickness, 0))
        x_max = int(min(max(x_a, x_b) + thickness, w_map))
        y_min = int(max(min(y_a, y_b) - thickness, 0))
        y_max = int(min(max(y_a, y_b) + thickness, h_map))
        norm_ba = (x_ba * x_ba + y_ba * y_ba) ** 0.5
        if norm_ba < 1e-7:  # Same points, no paf
            return
        x_ba /= norm_ba
        y_ba /= norm_ba

        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                x_ca = x - x_a
                y_ca = y - y_a
                d = math.fabs(x_ca * y_ba - y_ca * x_ba)
                if d <= thickness:
                    paf_map[0, y, x] = x_ba
                    paf_map[1, y, x] = y_ba

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
    RESIZE = (640, 640)

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
    dataset_train = KeyPointsDataset(data_path, 7, transform=transform,
                                     image_sets='train', is_train=True,
                                     body_part_kpt_ids=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])

    print('dataset size:', len(dataset_train))
    # for idx in range(10):
    data = dataset_train[2]
    images, labels, parfs = data['img'], data['target'], data['paf_maps']
    print(images.shape)
    print(labels.shape)
    print(parfs.shape)
