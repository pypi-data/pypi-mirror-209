# -*- encoding: utf-8 -*-
"""
强化学习智能体统一接口定义。

强化学习基础组件的抽象接口，通常包括：
+ `Env`，强化学习中的交互环境；
+ `Agent`，强化学习智能体，在与环境的交互中观察环境状态(`state`)，并通过执行动作(`action`)改变环境；
+ `Processor`，处理器(或耦合器)，当智能体和环境的状态/行动等不匹配时，可以通过该组件进行处理和连接；
+ `Space`，状态行动空间定义器，为环境定义状态行动空间。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from keras.callbacks import History, Callback
from keras.optimizers import Optimizer
from abc import abstractmethod, ABCMeta
from typing import Any
from env import Env


class Agent(metaclass=ABCMeta):
    """深度学习智能体。
    作为模型核心，智能体实现强化学习算法，定义统一的抽象接口（基于 OpenAI Gym 接口）。
    智能体与环境交互，首先观察环境的状态，基于观察结果、通过执行动作改变环境。
    """

    def get_config(self) -> dict:
        """获取智能体配置。

        Returns
        ----
        智能体配置。
        """
        return {}

    @abstractmethod
    def compile(self, optimizer: Optimizer, metrics: list, configs: dict):
        """合成智能体。

        Args
        ----
        + optimizer(`keras.optimizer.Optimizer`): 训练期间的优化器；
        + metrics(list of `lambda y_true, y_pred: metric`): 训练期间的评估器；
        + configs(dict of additional arguments): 其他相关参数配置;
        """
        raise NotImplementedError()

    @abstractmethod
    def fit(self, env: Env, nb_steps: int, action_repetition: int, callbacks: Callback,
            verbose: int, visualize: bool, nb_max_start_steps: int,
            start_step_policy: Any, log_interval: int,
            nb_max_episode_steps: int) -> History:
        """在给定环境中训练智能体。

        Args
        ----
        + env(`Env`实例): 深度学习环境；
        + nb_steps(int): 最大训练回合步数；
        + action_repetition(int): 智能体在不观察环境时重复相同动作的次数 (如果一个动作对环境影响很小，设为 >1会有帮助);
        + callbacks(list of `keras.callbacks.Callback`): 训练期间的回调函数列表 ;
        + verbose(int): 控制台日志等级(0 为无日志, 1 为间隔日志, 2 为每局训练日志);
        + visualize(bool): 是否在训练期间可视化环境（开启可视化会降低训练速度，通常用于模型调试）;
        + nb_max_start_steps(int): 智能体在每局训练开始、按照`start_step_policy`执行的最大步数;
        + start_step_policy(`lambda observation: action`): 每局起始步数内采用的动作策略;
        + log_interval(int): 日志间隔步数(当`verbose`=1生效);
        + nb_max_episode_steps(int): 每局训练在自动重置前可以执行的最大步数，若为`None`表示无限进行下去、直到环境终止;

        Returns
        ----
        History 实例，包含整个训练过程的信息。
        """
        raise NotImplementedError()

    @abstractmethod
    def test(self, env: Env, nb_episodes: int, action_repetition: int,
             callbacks: Callback, visualize: bool, nb_max_episode_steps: int,
             nb_max_start_steps: int, start_step_policy: Any, verbose: int) -> History:
        """模型测试。

        Args
        ----
        + env(`Env`实例): 深度学习环境；
        + nb_episodes(int): 最大训练局数；
        + action_repetition(int): 智能体在不观察环境时重复相同动作的次数 (如果一个动作对环境影响很小，设为 >1会有帮助);
        + callbacks(list of `keras.callbacks.Callback`): 训练期间的回调函数列表;
        + visualize(bool): 是否在训练期间可视化环境（开启可视化会降低训练速度，通常用于模型调试）;
        + nb_max_episode_steps(int): 每局训练在自动重置前可以执行的最大步数，若为`None`表示无限进行下去、直到环境终止;
        + nb_max_start_steps(int): 智能体在每局训练开始、按照`start_step_policy`执行的最大步数;
        + start_step_policy(`lambda observation: action`): 每局起始步数内采用的动作策略;
        + verbose(int): 控制台日志等级(0 为无日志, 1 为间隔日志, 2 为每局训练日志);

        Returns
        ----
        History 实例，包含整个训练过程的信息。
        """
        raise NotImplementedError()

    @abstractmethod
    def reset_states(self):
        """重置所有内部状态。

        每局训练结束后，重置模型所有内部保持的状态。
        """
        raise NotImplementedError()

    @abstractmethod
    def forward(self, observation: object) -> object:
        """计算下一步要执行的动作。
        基于当前环境观察状态，生成下一步动作。如果智能体策略由神经网络实现，这时对应一次前向计算。

        Args
        ----
        + observation(object): 当前环境观察状态；

        Returns
        ----
        下一步动作。
        """
        raise NotImplementedError()

    @abstractmethod
    def backward(self, reward: float, terminal: bool) -> list:
        """更新智能体。
        在执行上一步动作后，根据奖励更新智能体。若智能体策略由神经网络实现，则对应一次反向传播的权值更新。

        Args
        ----
        + reward(float): 通过执行智能体动作后获得的当前回合的奖励；
        + terminal(bool): 训练是否结束；

        Returns
        ----
        智能体评估值列表。
        """
        raise NotImplementedError()

    @abstractmethod
    def load_weights(filepath: str):
        """从HDF5文件中加载智能体权重。

        Args
        ----
        + filepath(str): 智能体权重hdf5文件路径;
        """
        raise NotImplementedError()

    @abstractmethod
    def save_weights(self, filepath: str, overwrite: bool = False):
        """保存智能体权重文件到HDF5文件。

        Args
        ----
        + filepath(str): 智能体权重hdf5文件路径;
        + overwrite(bool): 是否覆盖重写已有的权重文件(如果`False`且`filepath`已经存在，则抛出异常);
        """
        raise NotImplementedError()

    @property
    def layers(self) -> list:
        """模型所有隐藏层列表。
        如果模型使用多个内部模型实现，则以连接列表的形式返回。
        """
        raise NotImplementedError()

    @property
    def metrics_names(self) -> list:
        """智能体使用的评估器名称列表。
        """
        return []

    @property
    def _on_train_begin(self):
        """训练开始前调用的回调函数。
        """
        raise NotImplementedError()

    @property
    def _on_train_end(self):
        """训练结束后调用的回调函数。
        """
        raise NotImplementedError()

    @property
    def _on_test_begin(self):
        """测试开始前调用的回调函数。
        """
        raise NotImplementedError()

    @property
    def _on_test_end(self):
        """测试结束后调用的回调函数。
        """
        raise NotImplementedError()
