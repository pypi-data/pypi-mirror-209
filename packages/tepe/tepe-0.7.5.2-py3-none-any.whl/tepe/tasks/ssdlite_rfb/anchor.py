import torch
from .box_utils import box_corner_to_center, box_center_to_corner

def multibox_prior(data, sizes, ratios):
    """
    生成以每个像素为中心具有不同形状的锚框。
    :param data: 在这个上面生成anchor, shape(b, c, h, w)
    :param sizes(list): anchor size, 相对于data的大小
    :param ratios(list): anchor长宽比
    :return: 所有的锚框, shape(b, n, 4), n = w*h*k, k = len(sizes) + len(ratios) - 1
    Example:
    >>> X = torch.rand(size=(1, 3, 561, 728))
    >>> sizes, ratios = [0.75, 0.5, 0.25], [1, 2, 0.5]
    >>> Y = multibox_prior(X, sizes, ratios)
    >>> Y.shape  # (1, 2042040, 4)
    """
    in_height, in_width = data.shape[-2:]
    device, num_sizes, num_ratios = data.device, len(sizes), len(ratios)
    boxes_per_pixel = (num_sizes + num_ratios - 1)
    #     boxes_per_pixel = (num_sizes * num_ratios)
    size_tensor = torch.tensor(sizes, device=device)
    ratio_tensor = torch.tensor(ratios, device=device)

    # 为了将锚点移动到像素的中心，需要设置偏移量。
    # 因为一个像素的的高为1且宽为1，我们选择偏移我们的中心0.5
    offset_h, offset_w = 0.5, 0.5
    steps_h = 1.0 / in_height  # Scaled steps in y axis
    steps_w = 1.0 / in_width  # Scaled steps in x axis

    # 生成锚框的所有中心点
    center_h = (torch.arange(in_height, device=device) + offset_h) * steps_h
    center_w = (torch.arange(in_width, device=device) + offset_w) * steps_w
    shift_y, shift_x = torch.meshgrid(center_h, center_w)
    shift_y, shift_x = shift_y.reshape(-1), shift_x.reshape(-1)

    # 生成“boxes_per_pixel”个高和宽，
    # 之后用于创建锚框的四角坐标 (xmin, xmax, ymin, ymax)
    w = torch.cat((size_tensor * torch.sqrt(ratio_tensor[0]),
                   sizes[0] * torch.sqrt(ratio_tensor[1:]))) \
        * in_height / in_width  # Handle rectangular inputs
    h = torch.cat((size_tensor / torch.sqrt(ratio_tensor[0]),
                   sizes[0] / torch.sqrt(ratio_tensor[1:])))

    # 除以2来获得半高和半宽
    assert torch.stack((-w, -h, w, h), dim=1).numel() == torch.stack((-w, -h, w, h)).T.numel()
    # 等价
    # anchor_manipulations = torch.stack((-w, -h, w, h)).T.repeat(
    #                                     in_height * in_width, 1) / 2
    anchor_manipulations = torch.stack((-w, -h, w, h), dim=1).repeat(
        in_height * in_width, 1) / 2

    # 每个中心点都将有“boxes_per_pixel”个锚框，
    # 所以生成含所有锚框中心的网格，重复了“boxes_per_pixel”次
    out_grid = torch.stack([shift_x, shift_y, shift_x, shift_y],
                           dim=1).repeat_interleave(boxes_per_pixel, dim=0)

    output = out_grid + anchor_manipulations

    return output.unsqueeze(0)


def box_iou(boxes1, boxes2):
    """
    计算两个锚框或边界框列表中成对的交并比。
    :param boxes1: list of boxes, shape is (m, 4)
    :param boxes2: list of boxes, shape is (n, 4)
    :return: iou, shape is (m, n)
    """
    box_area = lambda boxes: ((boxes[:, 2] - boxes[:, 0]) *
                              (boxes[:, 3] - boxes[:, 1]))
    # `areas1`, `areas2`的形状:
    # `areas1`：(m,),
    # `areas2`：(n,)
    areas1 = box_area(boxes1)
    areas2 = box_area(boxes2)
    #  `inter_upperlefts`, `inter_lowerrights`, `inters`的形状: (m, n, 2), 2 is (x, y)
    #  `boxes1[:, None, :2]` shape: (m, 1, 2), `boxes2[:, :2]` shape: (n, 2)
    inter_upperlefts = torch.max(boxes1[:, None, :2], boxes2[:, :2])
    inter_lowerrights = torch.min(boxes1[:, None, 2:], boxes2[:, 2:])
    # 交集的w, h
    inters = (inter_lowerrights - inter_upperlefts).clamp(min=0)
    # `inter_areas` and `union_areas`的形状: (m, n)
    inter_areas = inters[:, :, 0] * inters[:, :, 1]  # (m, n)
    union_areas = areas1[:, None] + areas2 - inter_areas  # (m, n)
    return inter_areas / union_areas


def assign_anchor_to_bbox1(ground_truth, anchors, device, iou_threshold=0.5):
    """
    将最接近的真实边界框分配给锚框。
    :param ground_truth: shape: (ngt, 4)
    :param anchors: shape: (na, 4)
    :param device: "cuda" or "cpu"
    :param iou_threshold: iou threshold
    :return: 每个锚点框对应的标签（有可能有的anchor不会被分配标签），形状：(na,)
    """
    num_anchors, num_gt_boxes = anchors.shape[0], ground_truth.shape[0]
    # 位于第i行和第j列的元素 x_ij 是锚框i和真实边界框j的IoU
    jaccard = box_iou(anchors, ground_truth) # (na, ngt)
    # 对于每个锚框，分配的真实边界框的张量
    anchors_bbox_map = torch.full((num_anchors,), -1, dtype=torch.long,
                                  device=device)
    # 根据阈值，决定是否分配真实边界框
    # print(jaccard)
    max_ious, indices = torch.max(jaccard, dim=1)
    anc_i = torch.nonzero(max_ious >= iou_threshold).reshape(-1)
    box_j = indices[max_ious >= iou_threshold]
    anchors_bbox_map[anc_i] = box_j  # 给符合条件的anchor分配标签
    col_discard = torch.full((num_anchors,), -1, dtype=torch.long)
    row_discard = torch.full((num_gt_boxes,), -1, dtype=torch.long)
    for i in range(num_gt_boxes):
        max_idx = torch.argmax(jaccard)
        box_idx = (max_idx % num_gt_boxes).long()
        anc_idx = (max_idx // num_gt_boxes).long()
        anchors_bbox_map[anc_idx] = box_idx
        jaccard[:, box_idx] = col_discard
        jaccard[anc_idx, :] = row_discard

    return anchors_bbox_map


def assign_anchor_to_bbox(ground_truth, anchors, device, iou_threshold=0.5):
    """
    将最接近的真实边界框分配给锚框。
    :param ground_truth: shape: (ngt, 4)
    :param anchors: shape: (na, 4)
    :param device: "cuda" or "cpu"
    :param iou_threshold: iou threshold
    :return: 每个锚点框对应的标签（有可能有的anchor不会被分配标签），形状：(na,)
    """
    num_anchors, num_gt_boxes = anchors.shape[0], ground_truth.shape[0]
    # 位于第i行和第j列的元素 x_ij 是锚框i和真实边界框j的IoU
    jaccard = box_iou(anchors, ground_truth)  # (na, ngt)
    # 对于每个锚框，分配的真实边界框的张量
    anchors_bbox_map = torch.full((num_anchors,), -1, dtype=torch.long,
                                  device=device)
    # step1: 1. 遍历每个gt（确保每个gt都有分配），找与之iou最大的anchor，将此anchor分配gt的id，此anchor不再被分配。
    for i in range(num_gt_boxes):
        max_an_id = torch.argmax(jaccard[:, i])
        anchors_bbox_map[max_an_id] = i
    # step: 2. 遍历每个没被分配的anchor，找与之iou最大的gt，如果iou＞0.5，将此gt的id分配给anchor，否则不分配。
    for j in range(num_anchors):
        if anchors_bbox_map[j] != -1:
            continue
        max_gt_id = torch.argmax(jaccard[j, :])
        if jaccard[j, max_gt_id] >= iou_threshold:
            anchors_bbox_map[j] = max_gt_id

    return anchors_bbox_map


def offset_boxes(anchors, assigned_bb, eps=1e-6):
    """对锚框偏移量的转换。"""
    c_anc = box_corner_to_center(anchors)
    c_assigned_bb = box_corner_to_center(assigned_bb)
    offset_xy = 10 * (c_assigned_bb[:, :2] - c_anc[:, :2]) / c_anc[:, 2:]
    offset_wh = 5 * torch.log(eps + c_assigned_bb[:, 2:] / c_anc[:, 2:])
    offset = torch.cat([offset_xy, offset_wh], dim=1)
    return offset


def multibox_target(anchors, labels):
    """
    使用真实边界框标记锚框。
    :param anchors: shape(batch_size, num_anchors, 4),
        last dim: [anchor_tl_x, anchor_tl_y, anchor_br_x, anchor_br_y]
    :param labels: shape(batch_size, num_anchors, 5),
        last dim: [class, gt_tl_x, gt_tl_y, gt_br_x, gt_br_y]
    :return: bbox_offset, shape (batch_size, num_anchors*4)
             bbox_mask, 对offset的mask, shape (batch_size, num_anchors*4)
             class_labels, shape (batch_size, num_anchors)
    """
    batch_size, anchors = labels.shape[0], anchors.squeeze(0)
    batch_offset, batch_mask, batch_class_labels = [], [], []
    device, num_anchors = anchors.device, anchors.shape[0]
    for i in range(batch_size):
        label = labels[i, :, :]
        gt_bbox = label[:, 1:]
        anchors_bbox_map = assign_anchor_to_bbox(gt_bbox, anchors, device)
        bbox_mask = ((anchors_bbox_map >= 0).float().unsqueeze(-1)).repeat(1, 4)
        # 将类标签和分配的边界框坐标初始化为零
        class_labels = torch.zeros(num_anchors, dtype=torch.long,
                                   device=device)
        assigned_bb = torch.zeros((num_anchors, 4), dtype=torch.float32,
                                  device=device)
        # 使用真实边界框来标记锚框的类别。
        # 如果一个锚框没有被分配，我们标记其为背景（值为零）
        indices_true = torch.nonzero(anchors_bbox_map >= 0)
        bb_idx = anchors_bbox_map[indices_true]
        class_labels[indices_true] = label[bb_idx, 0].long() + 1
        assigned_bb[indices_true] = label[bb_idx, 1:]
        # 偏移量转换
        offset = offset_boxes(anchors, assigned_bb) * bbox_mask
        batch_offset.append(offset.reshape(-1))
        batch_mask.append(bbox_mask.reshape(-1))
        batch_class_labels.append(class_labels)
    bbox_offset = torch.stack(batch_offset)
    bbox_mask = torch.stack(batch_mask)
    class_labels = torch.stack(batch_class_labels)
    return (bbox_offset, bbox_mask, class_labels)


def offset_inverse(anchors, offset_preds):
    """根据带有预测偏移量的锚框来预测边界框。"""
    anc = box_corner_to_center(anchors)
    pred_bbox_xy = (offset_preds[:, :2] * anc[:, 2:] / 10.0) + anc[:, :2]
    pred_bbox_wh = torch.exp(offset_preds[:, 2:] / 5.0) * anc[:, 2:]
    pred_bbox = torch.cat((pred_bbox_xy, pred_bbox_wh), dim=1)
    predicted_bbox = box_center_to_corner(pred_bbox)
    return predicted_bbox


def nms(boxes, scores, iou_threshold):
    """对预测边界框的置信度进行排序。
       这里不区分类别，每个框均对应一个预测偏移量和置信度"""
    B = torch.argsort(scores, dim=-1, descending=True)
    keep = []  # 保留预测边界框的指标
    while B.numel() > 0:
        i = B[0]
        keep.append(i)
        if B.numel() == 1: break
        iou = box_iou(boxes[i, :].reshape(-1, 4),
                      boxes[B[1:], :].reshape(-1, 4)).reshape(-1)
        inds = torch.nonzero(iou <= iou_threshold).reshape(-1)
        B = B[inds + 1]
    return torch.tensor(keep, device=boxes.device)


if __name__ == '__main__':
    ground_truth = torch.tensor([[0, 0.1, 0.08, 0.52, 0.92],
                                 [1, 0.55, 0.2, 0.9, 0.88]])
    anchors = torch.tensor([[0, 0.1, 0.2, 0.3], [0.15, 0.2, 0.4, 0.4],
                            [0.63, 0.05, 0.88, 0.98], [0.66, 0.45, 0.8, 0.8],
                            [0.57, 0.3, 0.92, 0.9]])
    labels = multibox_target(anchors.unsqueeze(dim=0),
                             ground_truth.unsqueeze(dim=0))