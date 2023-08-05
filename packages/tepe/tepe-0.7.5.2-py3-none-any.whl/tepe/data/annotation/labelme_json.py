from typing import Union, List, Dict, Literal, Any
import os.path as osp
import json
import numpy as np


class LabelmeJsonWriter:
    """labelme标注文件写入器，保存json标注文件时使用

    Args:
        image_name (str): 图像的文件名，包含后缀
        image_size (List[int]): 图像的高、宽、通道数

    Example:
        img_name = '202111123-003.jpg'
        writer = LabelmeJsonWriter(img_name, img.shape)
        for r in result:
            label, left, top, right, bottom = r
            points = [[left, top], [right, bottom]]
            writer.add_shape(2, points, label)
        save_json_path = 'name.json'
        writer.save(target_file=save_json_path)
    """
    type_dict = {
        1: 'point',
        2: 'rectangle',
        3: 'polygon'
    }
    def __init__(self, image_name: str, image_size: List[int]):

        self.image_name = image_name
        h, w, _ = image_size
        self.info = {
          "version": "4.2.10",
          "flags": {},
          "shapes": [],
          "imagePath": image_name,
          "imageData": None,
          "imageHeight": h,
          "imageWidth": w
        }

    def add_shape(self, shape_type: int, points: List[List[Union[int, float]]], label: str) -> None:
        """添加新的目标标注

        Args:
            shape_type (int): 目标标注类型
                1 -> 'points'
                2 -> 'rectangle'
                3 -> 'polygon'
            points (List[List[Union[int, float]]]): 目标标注的坐标
            label (str): 目标标注的标签
        """

        if isinstance(shape_type, str):
            assert shape_type in self.type_dict.values()

        if isinstance(points, np.ndarray):
            points = points.tolist()

        pts = []
        for p in points:
            pts.append([int(p[0]), int(p[1])])

        element = {
          "label": label,
          "points": pts,
          "group_id": None,
          "shape_type": self.type_dict[shape_type] if isinstance(shape_type, int) else shape_type,
          "flags": {}
        }
        self.info['shapes'].append(element)

    def save(self, target_file: str = None) -> None:
        """保存标注结果到文件夹

        Args:
            target_file (str, optional): 保存的目标路径，如果没有设置，则按照图像名保存在当前目录下
        """
        if target_file is None:
            target_file = self.image_name.replace(osp.splitext(self.image_name)[-1], '.json')
        with open(target_file, "w", encoding='utf-8') as f:
            json.dump(self.info, f, ensure_ascii=False, indent=2)


class LabelmeJsonReader:
    """labelme标注文件读取器，读取labelme标注结果json文件时使用

    Args:
        file_path (str): 标注文件路径
    
    Example:
        reader = LabelmeJsonReader(json_path)
        shapes = reader.get_shapes()
        for shape in shapes:
            label, points, shape_type = shape['label'], shape['points'], shape['shape_type']
            tl, rb = points
            t, l = tl
            r, b = rb
    """

    type_dict = {
        'point': 1,
        'rectangle': 2,
        'polygon': 3,
    }
    def __init__(self, file_path: str):

        self._shapes = []
        self.file_path = file_path
        try:
            self.parse_json()
        except:
            pass

    def parse_json(self) -> None:
        """解析标注json文件
        """
        with open(self.file_path, 'r', encoding='utf-8') as f:
            json_dict = json.load(f)
        self._shapes = []
        for shape in json_dict['shapes']:
            shape['shape_type'] = self.type_dict[shape['shape_type']]
            self._shapes.append(shape)
        self.h = json_dict["imageHeight"]
        self.w = json_dict['imageWidth']

    def get_img_shape(self) -> List[int]:
        """获得标注文件对应图像的宽高

        Returns:
            List[int]: 图像的宽和高
        """
        return [self.h, self.w]

    def round_shapes(self) -> None:
        """将点的坐标转成整形
        """
        new_shapes = []
        for shape in self._shapes:
            if isinstance(shape['points'], list):
                shape['points'] = [list(map(round, p)) for p in shape['points']]
            new_shapes.append(shape)
        self._shapes = new_shapes

    def get_shapes(self) -> List[Dict[Literal["label", "points", "shape_type"], Any]]:
        """获得标注信息

        Returns:
            List: 一个dict列表，dict中含有"label", "points", "shape_type"等信息
            其中shape_type的对应表：
                1 -> 'points'
                2 -> 'rectangle'
                3 -> 'polygon'
        """
        return self._shapes