# -*- encoding: utf-8 -*-
"""
实时控制模型的统一接口类。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from abc import abstractmethod, ABCMeta


class ABCController(metaclass=ABCMeta):
    """
    实时控制模型的统一接口类。
    """

    @abstractmethod
    def init(self, env: object, agent: object, processor: object, confs: dict):
        """
        初始化模型，配置模型结构。

        Args
        ----
        + env(`Env`): 强化学习环境;
        + agent(`Agent`): 强化学习引擎;
        + confs(dict): 强化学习调度模型配置。
        """
        raise NotImplementedError()

    @abstractmethod
    def fit(self, confs: dict) -> dict:
        """
        批训练模型。

        Args
        ----
        + confs(dict): 模型训练配置信息，包括训练次数、批次大小等。

        Returns
        ----
        返回模型训练过程信息, 例如准确度和收敛信息等。
        """
        raise NotImplementedError()

    @abstractmethod
    def step(self, observation: object) -> tuple:
        """
        步进模型。

        Args
        ----
        + observation(object): 当前环境观察状态；

        Returns
        ----
        返回模型当前状态(当前观测状态, 下一步执行的动作, 当前评估结果, 当前奖励).
        """
        raise NotImplementedError()

    @abstractmethod
    def run(self) -> dict:
        """
        在环境中运行模型直到环境结束。

        Returns
        ----
        返回模型全程状态，内容包括：
        {
            "obervations": [], # 全程观测状态
            "actions": [],     # 所有执行的动作
            "metrics": [],     # 所有评估结果
            "rewards": []      # 所有奖励
        }
        """
        raise NotImplementedError()

    @abstractmethod
    def reset(self, confs: dict):
        """
        重置模型, 如果没有重配置则恢复到初始状态。

        Args
        ----
        + confs(dict): 强化学习调度模型配置。
        """
        raise NotImplementedError()

    @property
    def configs(self):
        """
        模型的配置信息。
        """
        raise NotImplementedError()

    @property
    def actions(self):
        """
        模型采用的动作组。
        """
        raise NotImplementedError()

    @property
    def observations(self):
        """
        模型观察的状态组。
        """
        raise NotImplementedError()
