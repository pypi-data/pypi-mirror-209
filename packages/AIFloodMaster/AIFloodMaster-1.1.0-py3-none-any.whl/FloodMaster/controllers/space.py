# -*- encoding: utf-8 -*-
"""
强化学习动作状态统一接口定义。

强化学习基础组件的抽象接口，通常包括：
+ `Env`，强化学习中的交互环境；
+ `Agent`，强化学习智能体，在与环境的交互中观察环境状态(`state`)，并通过执行动作(`action`)改变环境；
+ `Processor`，处理器(或耦合器)，当智能体和环境的状态/行动等不匹配时，可以通过该组件进行处理和连接；
+ `Space`，状态行动空间定义器，为环境定义状态行动空间。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""


class Space(object):
    """环境的状态和动作空间。

    `Space` 通常作为参数组件传入深度学习环境中，从而为 `Env` 提供状态和动作空间的定义。
    """

    def sample(self, seed=None):
        """在空间中均匀随机采样一个随机元素。
        """
        raise NotImplementedError()

    def contains(self, x) -> bool:
        """检查指定值是否是空间一个有效成员。
        """
        raise NotImplementedError()
