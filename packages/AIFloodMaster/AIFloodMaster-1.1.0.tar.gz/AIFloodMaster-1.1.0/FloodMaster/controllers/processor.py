# -*- encoding: utf-8 -*-
"""
强化学习中环境和智能体之间的状态动作耦合器的统一接口定义。

强化学习基础组件的抽象接口，通常包括：
+ `Env`，强化学习中的交互环境；
+ `Agent`，强化学习智能体，在与环境的交互中观察环境状态(`state`)，并通过执行动作(`action`)改变环境；
+ `Processor`，处理器(或耦合器)，当智能体和环境的状态/行动等不匹配时，可以通过该组件进行处理和连接；
+ `Space`，状态行动空间定义器，为环境定义状态行动空间。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""


class Processor(object):
    """状态动作处理器。
    处理器充当 `Agent` 和 `Env` 之间的耦合机制。如果`Agent`对观察、行动和对环境的回报有不同的格式或数据要求，
    通过实现自定义处理器，可以无需更改智能体或环境的底层实现的情况下完成两者之间有效地转换。

    通常将 `Processor` 作为参数传入智能体，从而为 `Agent` 提供与环境交互耦合的工具。
    """

    def process_step(self, observation: object, reward: float, done: bool,
                     info: dict) -> tuple:
        """通过处理/转换观察结果、奖励、是否结束、训练信息，完成一个完整的训练回合。

        Args
        ----
        + observation(object): 智能体观察到的当前环境状态；
        + reward(float): 执行动作后获得的奖励值；
        + done(bool): 当前回合是否结束；
        + info(dict): 辅助诊断信息;

        Returns
        ----
        经过处理后的元组 (observation, reward, done, reward)。
        """
        observation = self.process_observation(observation)
        reward = self.process_reward(reward)
        info = self.process_info(info)
        return observation, reward, done, reward

    def process_observation(self, observation: object) -> object:
        """处理/转换直接观察的环境状态为智能体需要的格式/数据。

        Args
        ----
        + observation(object): 智能体观察到的当前环境状态；

        Returns
        ----
        observation(object): 经过处理后的环境观察结果。
        """
        raise NotImplementedError()

    def process_reward(self, reward: float) -> float:
        """处理/转换直接返回的动作奖励为智能体需要的格式/数据。

        Args
        ----
        + reward(float): 执行动作后获得的奖励值；

        Returns
        ----
        reward(float): 经过处理后的动作奖励。
        """
        raise NotImplementedError()

    def process_info(self, info: dict) -> dict:
        """处理/转换直接返回的训练信息为智能体需要的格式/数据。

        Args
        ----
        + info(dict): 训练过程中辅助诊断信息;

        Returns
        ----
        info(dict): 经过处理后的训练信息。
        """
        raise NotImplementedError()

    def process_action(self, action: object) -> object:
        """处理/转换智能体预报的原始动作为环境中可以执行的动作。

        Args
        ----
        + action(object): 智能体预报的下一个动作；

        Returns
        ----
        action(object): 经过处理后可以再环境中执行的动作。
        """
        raise NotImplementedError()

    def process_state_batch(self, batch: list) -> list:
        """处理整个批次的状态值。

        Args
        ----
        + batch(list): 观察到的状态值列表。

        Returns
        ----
        batch(list): 经处理的状态值列表。
        """
        raise NotImplementedError()

    @property
    def metrics(self) -> list:
        """处理器中的评估器列表(List of `lambda y_true, y_pred: metric` functions)。
        """
        return []

    def metrics_names(self) -> list:
        """处理器中的评估器名称列表。
        """
        return []
