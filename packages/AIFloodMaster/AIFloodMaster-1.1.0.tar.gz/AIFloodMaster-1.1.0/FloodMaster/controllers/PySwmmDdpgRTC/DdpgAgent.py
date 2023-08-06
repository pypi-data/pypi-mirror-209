# -*- encoding: utf-8 -*-
"""
基于 DDPG 算法的深度强化学习引擎。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@xxx.xxx'
"""
import warnings
from typing import Any
import numpy as np

from tensorflow.keras import models, layers, optimizers  # 统一从keras中导出接口
from rl.agents import DDPGAgent
from rl.memory import SequentialMemory
from rl.random import OrnsteinUhlenbeckProcess
from rl.core import Agent  # 非本地版本
from rl.core import Env  # 非本地版本


class DdpgAgent(Agent):
    """采用 DDPG 算法的深度强化学习引擎.

    这里实际上是对 DDPGAgent的封装。
    """

    def __init__(self, Id: str):
        self._id = Id
        self._configs = {}  # 强化学习配置
        self._agent = None  # 强化学习引擎
        self._memory = None  # 强化学习内存池
        self._nb_actions = None  # 动作数量
        self._actions_shape = None  # 动作状态数据形状
        self._obs_shape = None  # 环境状态数据形状

    def init(self, action_space_shape: tuple, obs_space_shape: tuple):
        """初始化模型。
        为了能够更加自由的组装强化学习控制器，将初始化方法独立出来。

        Args
        ----
        + action_space_shape(tuple): 环境动作状态空间数据形状；
        + obs_space_shape(tuple): 环境观察状态空间数据形状；
        """
        # 动作数量
        self._nb_actions = action_space_shape[0]

        # 一维结构
        self._actions_shape = (self._nb_actions, )

        # 二维结构
        self._obs_shape = (1, ) + obs_space_shape

    def set_actor_configs(self, dense_units: list, activations: list):
        """设置 “行动者” 神经网络参数。

        Args
        ----
        + dense_units(list of int): 神经网络中各全连接层的单元数量(不含最后输出层);
        + activations(list of str): 神经网络中各全连接层的激活函数(不含最后输出层);
        """
        assert len(dense_units) > 1 or len(
            activations) > 1, "Empty actor neural network settings."
        assert len(dense_units) == len(
            activations
        ), "Number of units and activations of actor neural network dosen't match."

        nb = self._nb_actions
        if min(dense_units) < nb:
            warnings(f"Actor neural network dense units should bigger than {nb}.")

        units = [max(n, nb) for n in dense_units]
        self._configs['actor_units'] = units
        self._configs['actor_activations'] = activations

    def _build_actor_nn(self):
        """搭建 “行动者” 神经网络用于逼近策略函数，生成环境动作。

        “行动者” 模型输入当前环境状态，输出下一步要执行的动作。
        """
        actor = models.Sequential()
        actor.add(layers.Flatten(input_shape=self._obs_shape))

        units = self._configs['actor_units']
        funcs = self._configs['actor_activations']
        for units, activation in zip(units, funcs):
            actor.add(layers.Dense(units))
            actor.add(layers.Activation(activation))

        actor.add(layers.Dense(self._nb_actions))
        actor.add(layers.Activation('sigmoid'))
        return actor

    def set_critic_configs(self, dense_units: list, activations: list):
        """设置 “评估者” 神经网络参数。

        Args
        ----
        + dense_units(list of int): 神经网络中各全连接层的单元数量(不含最后输出层);
        + activations(list of str): 神经网络中各全连接层的激活函数(不含最后输出层);
        """
        assert len(dense_units) > 1 or len(
            activations) > 1, "Empty critic neural network settings."
        assert len(dense_units) == len(
            activations
        ), "Number of units and activations of critic neural network dosen't match."
        assert min(dense_units) > 0, "Negative critic network dense units."

        self._configs['critic_units'] = dense_units
        self._configs['critic_activations'] = activations

    def _build_critic_nn(self):
        """搭建 “评估者” 神经网络用于逼近值函数，评价模型生成的动作。

        “评估者” 模型输入当前执行的动作和(执行动作后)的环境状态两部分, 输出Q值。
        """
        action_input = layers.Input(shape=self._actions_shape)  # shape(None, 2)
        observation_input = layers.Input(shape=self._obs_shape)  # shape(None, 1, 10)
        flatten_observation = layers.Flatten()(observation_input)  # shape(None, 10)

        x = layers.Concatenate()([action_input, flatten_observation])  # shape(None, 12)
        units = self._configs['critic_units']
        funcs = self._configs['critic_activations']
        for units, activation in zip(units, funcs):
            x = layers.Dense(units)(x)
            x = layers.Activation(activation)(x)

        x = layers.Dense(1)(x)  # shape(None, 1)
        x = layers.Activation('linear')(x)

        # input shape[(None, 2), (None, 1, 10)], output shape[(None, 1)]
        critic = models.Model(inputs=[action_input, observation_input], outputs=x)
        return critic, action_input, observation_input

    def set_compile_configs(self, memory_limit: int, window_len: int,
                            actor_warmup_steps: int, critic_warmup_steps: int,
                            gamma: float, init_lr: float, target_lr: float):
        """设置ddpg引擎参数。

        Args
        ----
        + memory_limit(int): 动作回放池容量；
        + window_len(int): 动作回放池滑动更新窗口大小(步数);
        + actor_warmup_steps(int): 行动者模型预热期长度(预热之后开始模型更新);
        + critic_warmup_steps(int): 评估者模型预热期长度(预热后开始模型更新);
        + gamma(float): 贝尔曼方程(奖励)折扣系数;
        + init_lr(float): 模型的初始更新步长(学习率);
        + target_lr(float): 目标(辅助)模型的更新步长(学习率，通常低于`lr`);
        """
        self._configs['memory_limit'] = max(int(memory_limit), 1)
        self._configs['window_len'] = max(int(window_len), 1)
        if self._configs['memory_limit'] < self._configs['window_len']:
            raise IOError(
                f"Compile arg: memory_limit({memory_limit}) < window_len({window_len})."
            )

        self._configs['actor_warmup'] = max(int(actor_warmup_steps), 0)
        self._configs['critic_warmup'] = max(int(critic_warmup_steps), 0)
        self._configs['ddpg_gamma'] = min(abs(gamma), 1.0)
        self._configs['ddpg_lr'] = max(abs(init_lr), 1.e-3)
        self._configs['ddpg_target_lr'] = abs(target_lr)

    def _build_ddpg_agent(self, actor, critic, action_input):
        """配置 DDPG 算法模型。
        """
        # 训练过程中动作、状态、奖励等记录器(按指定大小存储)。
        memory = SequentialMemory(limit=self._configs['memory_limit'],
                                  window_length=self._configs['window_len'])

        # 训练过程中按概率采取随机动作（加入随机噪声），探索更好的动作。
        # 随机噪音可能导致agent获得的actions超出action_space。
        # 但是在DdpgEnv内以及pyswmm内会对action做检查。
        random_process = OrnsteinUhlenbeckProcess(size=self._nb_actions,
                                                  theta=0.15,
                                                  mu=0.0,
                                                  sigma=0.1)

        # DDPG 算法引擎。
        # DDPG 引擎配置了行动者和评估者网络，二者配合提高模型的表现；同时，
        # DDPG 引擎配置了模型副本，但使用不同的更新步长，用于稳定训练过程；
        # DDPG 引擎配置了回放池、随机噪音，用于探索可能的更优的动作。
        agent = DDPGAgent(nb_actions=self._nb_actions,
                          actor=actor,
                          critic=critic,
                          critic_action_input=action_input,
                          memory=memory,
                          nb_steps_warmup_actor=self._configs['actor_warmup'],
                          nb_steps_warmup_critic=self._configs['critic_warmup'],
                          random_process=random_process,
                          gamma=self._configs['ddpg_gamma'],
                          target_model_update=self._configs['ddpg_target_lr'])
        return agent, memory

    def compile(self, metrics=['mae']):
        actor = self._build_actor_nn()
        critic, action_input, _ = self._build_critic_nn()
        agent, memory = self._build_ddpg_agent(actor, critic, action_input)
        opt = optimizers.Adam(learning_rate=self._configs['ddpg_lr'], clipnorm=1.0)
        agent.compile(opt, metrics)
        self._agent = agent
        self._memory = memory

    def get_config(self):
        return self._configs

    def forward(self, observation: object):
        return self._agent.forward(observation)

    def backward(self, reward: float, terminal: bool):
        return self._agent.backward(reward, terminal)

    def fit(self,
            env: Env,
            nb_steps: int,
            action_repetition: int = 1,
            callbacks: list = None,
            verbose: int = 1,
            visualize: bool = False,
            nb_max_start_steps: int = 0,
            start_step_policy: Any = None,
            log_interval: int = 10000,
            nb_max_episode_steps: int = None):
        history = self._agent.fit(env, nb_steps, action_repetition, callbacks, verbose,
                                  visualize, nb_max_start_steps, start_step_policy,
                                  log_interval, nb_max_episode_steps)
        return history

    def test(self,
             env: Env,
             nb_episodes: int = 1,
             action_repetition: int = 1,
             callbacks: list = None,
             visualize: bool = False,
             nb_max_episode_steps: int = None,
             nb_max_start_steps: int = 0,
             start_step_policy: Any = None,
             verbose: int = 1):
        self._agent.test(env, nb_episodes, action_repetition, callbacks, visualize,
                         nb_max_episode_steps, nb_max_start_steps, start_step_policy,
                         verbose)

    def reset_states(self):
        self._agent.reset_states()

    def save_weights(self, filepath: str, overwrite: bool = False):
        self._agent.save_weights(filepath, overwrite)

    def load_weights(self, filepath: str):
        self._agent.load_weights(filepath)

    def extract_result(self):
        """提取强化学习结果。
        """
        # 提取强化学习日志。
        ctrl_steps = self._env._total_steps
        all_actions = np.array(list(self._memory.actions)[0:ctrl_steps])
        all_rewards = np.array(list(self._memory.rewards)[0:ctrl_steps])
        all_states = np.array(list(self._memory.observations)[0:ctrl_steps])

        # 提取水池水深。
        ponds_id, juncs_id = self._env.get_ctrl_nodes_id()
        num_ponds = len(ponds_id)
        num_juncs = len(juncs_id)
        all_ponds_depth = all_states[:, :num_ponds]

        # 提取总溢流体积。
        all_flooding = all_states[:, num_ponds:2 * num_ponds + num_juncs]

        # 统计每回合的平均奖励。
        avg_rewards = []
        num_episodes = int(self._memory.nb_entries / ctrl_steps)
        for i in range(num_episodes):
            temp_rwd = all_rewards[ctrl_steps * i:ctrl_steps * (i + 1)]
            avg_rewards.append(np.mean(temp_rwd))

        return all_rewards, all_actions, all_ponds_depth, all_flooding, avg_rewards
