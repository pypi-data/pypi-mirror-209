# -*- encoding: utf-8 -*-
"""
强化学习环境统一接口定义。

强化学习基础组件的抽象接口，通常包括：
+ `Env`，强化学习中的交互环境；
+ `Agent`，强化学习智能体，在与环境的交互中观察环境状态(`state`)，并通过执行动作(`action`)改变环境；
+ `Processor`，处理器(或耦合器)，当智能体和环境的状态/行动等不匹配时，可以通过该组件进行处理和连接；
+ `Space`，状态行动空间定义器，为环境定义状态行动空间。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
import numpy as np
from abc import abstractmethod, ABCMeta


class Env(ABCMeta):
    """深度学习环境。
    作为项目中所有 `Agent` 交互学习的环境，定义统一的抽象接口（基于 OpenAI Gym 接口）。
    通常将 `Env` 作为参数传入深度学习智能体，为 `Agent` 的训练提供交互环境。
    """

    reward_range = (-np.inf, np.inf)
    action_space = None
    observation_space = None

    @abstractmethod
    def step(self, action: object) -> tuple:
        """执行一个时间步下的环境交互。

        Args
        ----
        + action(object): 由智能体提供的动作;

        Returns
        ----
        Tuple (observation, reward, done, info), which:
        + observation(object), 智能体观察的当前环境状态；
        + reward(float), 执行动作后获得的奖励值；
        + done(bool), 当前回合是否结束；
        + info(dict), 辅助诊断信息;
        """
        raise NotImplementedError()

    @abstractmethod
    def reset(self) -> object:
        """重置环境状态并返回初始观察。

        Returns
        ----
        Observation(object): 环境状态空间的初始观察(初始奖励设为 0)。
        """
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        """关闭环境并清理内存。
        """
        raise NotImplementedError()

    @abstractmethod
    def render(self, mode: str = 'human', close: bool = False):
        """渲染环境。
        支持的渲染模型因各自环境的实现而定，甚至可能完全不支持任何渲染。

        Args
        ----
        + mode(str): 渲染模式;
        + close(bool): 是否关闭所有渲染;
        """
        raise NotImplementedError()

    @abstractmethod
    def seed(self, seed: list = None) -> list:
        """设置环境中随机数生成器种子。

        Args
        ----
        + seed(list of int) : 随机数生成器种子;

        Returns
        ----
        环境中随机数生成器使用的种子的列表。
        """
        raise NotImplementedError()

    @abstractmethod
    def setup(self, *args, **kwargs):
        """提供环境运行时配置。

        配置中应该包含环境如何运行的相关信息/数据（比如远程服务器地址，数据路径等），
        但是同时不能影响环境语义。
        """
        raise NotImplementedError()

    @abstractmethod
    def load(filepath: str):
        """从本地加载环境。

        Args
        ----
        + filepath(str): 环境保存文件路径;
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self, filepath: str, overwrite: bool = False):
        """保存环境模型到本地文件。

        Args
        ----
        + filepath(str): 环境模型保存文件路径;
        + overwrite(bool): 是否覆盖重写已有的权重文件(如果`False`且`filepath`已经存在，则抛出异常);
        """
        raise NotImplementedError()

    @property
    def states(self) -> list:
        """环境当前所有状态。
        """
        raise NotImplementedError()

    @property
    def layers(self) -> list:
        """环境模型所有隐藏层列表。
        如果模型使用多个内部模型实现，则以连接列表的形式返回。
        """
        raise NotImplementedError()

    @property
    def configs(self) -> dict:
        """
        获取环境配置。
        """
        raise NotImplementedError()

    def __del__(self):
        self.close()

    def __str__(self):
        return '<{} instance>'.format(type(self).__name__)
