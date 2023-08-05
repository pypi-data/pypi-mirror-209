def build_backbone(cfg):
    """Build backbone."""
    from .model.backbone.resnet import ResNet
    obj_type = cfg.pop('type')
    return ResNet(**cfg)


def build_neck(cfg):
    """Build neck."""
    return NotImplementedError


def build_roi_extractor(cfg):
    """Build roi extractor."""
    obj_type = cfg.pop('type')
    if obj_type == 'SingleRoIExtractor':
        from tepe.tasks.attention_rpn.model.roi_extractors import SingleRoIExtractor
        return SingleRoIExtractor(**cfg)
    else:
        return NotImplementedError


def build_shared_head(cfg):
    """Build shared head."""
    obj_type = cfg.pop('type')
    if obj_type == 'ResLayer':
        from .model.roi_heads.shared_head import ResLayer
        return ResLayer(**cfg)
    else:
        return NotImplementedError


def build_head(cfg):
    """Build head."""
    obj_type = cfg.pop('type')
    if obj_type == 'AttentionRPNHead':
        from .model.dense_heads import AttentionRPNHead
        return AttentionRPNHead(**cfg)
    elif obj_type == 'MultiRelationRoIHead':
        from .model.roi_heads import MultiRelationRoIHead
        return MultiRelationRoIHead(**cfg)
    elif obj_type == 'MultiRelationBBoxHead':
        from .model.roi_heads.bbox_heads import MultiRelationBBoxHead
        return MultiRelationBBoxHead(**cfg)
    else:
        return NotImplementedError


def build_loss(cfg):
    """Build loss."""
    return NotImplementedError


def build_aggregator(cfg):
    """Build aggregator."""
    obj_type = cfg.pop('type')
    if obj_type == 'AggregationLayer':
        from .utils.aggregation_layer import AggregationLayer
        return AggregationLayer(**cfg)
    elif obj_type == 'DepthWiseCorrelationAggregator':
        from .utils.aggregation_layer import DepthWiseCorrelationAggregator
        return DepthWiseCorrelationAggregator(**cfg)
    else:
        return NotImplementedError