""" Step Scheduler

Basic step LR schedule with warmup, noise.

Hacked together by / Copyright 2020 Ross Wightman
"""
import math
import torch

from .scheduler import Scheduler


class StepLRScheduler(Scheduler):
    """
    """

    def __init__(
            self,
            optimizer: torch.optim.Optimizer,
            decay_t: float,          # 下降间隔
            decay_rate: float = 1.,  # 每次下降率
            warmup_t=0,              # warmup间隔，0说明不进行warmup
            warmup_lr_init=0,        # warmup初始lr
            warmup_prefix=True,      # True-第一次更新的间隔中包含warmup阶段
            t_in_epochs=True,        # 按epoch更新
            noise_range_t=None,      # 添加噪声开始、结束范围
            noise_pct=0.67,          # 控制噪声的大小
            noise_std=1.0,           # 
            noise_seed=42,
            initialize=True,         # 在优化器的group_param中加入'initial_lr'字段
    ) -> None:
        super().__init__(
            optimizer, 
            param_group_field="lr", 
            t_in_epochs=t_in_epochs,
            noise_range_t=noise_range_t, 
            noise_pct=noise_pct, 
            noise_std=noise_std, 
            noise_seed=noise_seed,
            initialize=initialize
        )

        self.decay_t = decay_t
        self.decay_rate = decay_rate
        self.warmup_t = warmup_t
        self.warmup_lr_init = warmup_lr_init
        self.warmup_prefix = warmup_prefix
        if self.warmup_t:
            # warmup阶段，每次更新时lr增加量
            self.warmup_steps = [(v - warmup_lr_init) / self.warmup_t for v in self.base_values]
            super().update_groups(self.warmup_lr_init)
        else:
            self.warmup_steps = [1 for _ in self.base_values]

    def _get_lr(self, t):
        if t < self.warmup_t:
            lrs = [self.warmup_lr_init + t * s for s in self.warmup_steps]
        else:
            if self.warmup_prefix:
                t = t - self.warmup_t
            lrs = [v * (self.decay_rate ** (t // self.decay_t)) for v in self.base_values]
        return lrs