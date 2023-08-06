# -*- encoding: utf-8 -*-
"""
采用深度确定性策略梯度算法(DDPG)的深度强化学习(Deep Reinforcement Learning, DRL)的闸门联调模型。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
import numpy as np
from copy import deepcopy

import os
import sys

sys.path.append(os.path.abspath(r"."))

from FloodMaster.controllers.controller import ABCController


class DdpgRtc(ABCController):
    """采用 DDPG 深度强化算法、基于 PySwmm 模型的闸门联调实现管网水力系统实时控制(RTC).
    """

    def __init__(self, ID: str):
        """实时控制器初始化。
        """
        self._id = ID
        self._configs = {}
        self._env = None
        self._agent = None
        self._processor = None

        self._rewards = []
        self._actions = []
        self._observations = []

    def init(self, env: object, agent: object, processor: object, confs: dict):
        self._rewards = []
        self._actions = []
        self._observation = []

        # 环境配置
        self._env = env
        self._configs['env'] = self._env.configs

        # 引擎配置
        self._agent = agent
        self._configs['agent'] = self._agent.get_config()

        # 适配器
        if processor:
            self._processor = processor

        # 其他配置
        self._configs['env_path'] = confs['env_path']
        self._configs['agent_path'] = confs['agent_path']

    def fit(self, confs: dict):
        history = self._agent.fit(self._env,
                                  nb_steps=confs['nb_steps'],
                                  verbose=confs['verbose'],
                                  action_repetition=confs['action_repetition'],
                                  log_interval=confs['log_interval'])
        self._configs.update(confs)
        self._agent.save_weights(self._configs['agent_path'], True)
        return history

    def run(self):
        done = False
        history = {'actions': [], 'rewards': [], 'observations': [], 'metrics': []}

        # 引擎和环境的初始化
        self.reset(None)
        observation = deepcopy(self._env.states)  # 重置环境并获取初始状态
        if self._processor:  # 通过适配器处理环境原始状态为引擎的输入数据
            observation = self._processor.process_observation(observation)
        assert observation is not None

        # 在环境中执行模拟直到环境结束
        while (not done):
            # 调用引擎生成环境动作
            action, observation, metrics, r, done = self.step(observation)
            # 记录日志
            history['actions'].append(action)
            history['observations'].append(observation)
            history['metrics'].append(metrics)
            history['rewards'].append(r)
            # 环境结束后再对引擎执行以此前向预报和反向更新
            if done:
                self._agent.forward(observation)
                self._agent.backward(0., terminal=False)
                observation = None
        # 提取强化学习过程状态
        self._actions = history['actions']
        self._observations = history['observations']
        self._rewards = history['rewards']
        return history['actions']

    def step(self, observation):
        # 调用引擎生成环境动作
        action = self._agent.forward(observation)
        if self._processor:  # 通过适配器处理引擎动作为环境动作
            action = self._processor.process_action(action)

        # 在环境中执行动作并获得新的环境状态以及执行动作的奖励等
        observation, r, done, info = self._env.step(action)
        observation = deepcopy(observation)
        if self._processor:
            observation, r, done, info = self._processor.process_step(
                observation, r, done, info)

        # 保持过程状态
        reward = self._rewards[-1] if len(self._rewards) > 0 else np.float32(0)
        reward += r
        self._rewards.append(reward)
        self._actions.append(action)
        self._observations.append(observation)

        # 更新引擎
        metrics = self._agent.backward(reward, terminal=done)
        return action, observation, metrics, r, done

    def reset(self, configs):
        self._agent.reset_states()
        self._env.reset()
        self._rewards.clear()
        self._actions.clear()
        self._observations.clear()

    @property
    def configs(self):
        return self._configs

    @property
    def actions(self):
        return self._actions

    @property
    def observations(self):
        return self._observations


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd
    from DdpgEnv import PySwmmEnv
    from DdpgAgent import DdpgAgent
    import os
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

    # 配置环境
    confs = {}
    proj_dir = r".\data\ddpg-swmm-data\\"
    mid_dir1 = r"obs_data_1month_all_controlled\\"
    mid_dir2 = r"obs_data_daily_fcsts\\"
    swmm_inp = proj_dir + mid_dir1 + r"test_01012018_01312018.inp"
    fcst_inp = proj_dir + mid_dir2 + r"test_01012018_01312018.csv"
    ctrl_step = 900
    ctrl_ponds = ["St1", "St2"]
    ponds_max_depth = [4.61, 4.61]
    ponds_target = [2.0, 2.0]
    ctrl_orifices = ["R1", "R2"]
    ctrl_juncs = ["J1"]
    swmm_env = PySwmmEnv()
    swmm_env.init(swmm_inp, fcst_inp, ctrl_step, ctrl_ponds, ponds_max_depth,
                  ponds_target, ctrl_orifices, ctrl_juncs)

    # 强化学习引擎
    agent_Id = "ddpg-1"
    agent = DdpgAgent(agent_Id)

    action_space_shape = swmm_env.action_space.shape
    obs_space_shape = swmm_env.observation_space.shape
    agent.init(action_space_shape, obs_space_shape)

    dense_units = [16, 16, 8]
    activations = ['relu', 'relu', 'relu']
    agent.set_actor_configs(dense_units, activations)
    dense_units = [32, 32, 32]
    activations = ['relu', 'relu', 'relu']
    agent.set_critic_configs(dense_units, activations)
    memory_limit = 1000000
    window_len = 1
    actor_warmup_steps = 50
    critic_warmup_steps = 50
    gamma = 0.99
    init_lr = 0.001
    target_lr = 0.001
    agent.set_compile_configs(memory_limit, window_len, actor_warmup_steps,
                              critic_warmup_steps, gamma, init_lr, target_lr)
    agent.compile()

    # 组装控制器
    rtc_Id = "rtc-1"
    rtc = DdpgRtc(rtc_Id)
    confs["env_path"] = "./tests/models/ddpg_env/"
    confs["agent_path"] = "./tests/models/ddpg_agent/"
    rtc.init(swmm_env, agent, None, confs)

    # 强化学习训练
    print("\n==== fit process ====\n")
    rtc_confs = {}
    rtc_confs["nb_steps"] = 6000
    rtc_confs['verbose'] = 1
    rtc_confs['action_repetition'] = 1
    rtc_confs['log_interval'] = 1000
    rtc.fit(rtc_confs)

    # 强化学习调度
    print("\n==== run ====\n")
    actions0 = rtc.run()

    # 强化学习步进调度
    print("\n==== run by step ====\n")
    rtc.reset(None)
    done = False
    observation = deepcopy(swmm_env.states)
    while (not done):
        action, observation, metrics, r, done = rtc.step(observation)

    # 测试并提取结果
    def extract_result(env, agent):
        """提取强化学习结果。
        """
        # 提取强化学习日志。
        ctrl_steps = env._total_steps
        all_actions = np.array(list(agent._memory.actions)[0:ctrl_steps])
        all_rewards = np.array(list(agent._memory.rewards)[0:ctrl_steps])
        all_states = np.array(list(agent._memory.observations)[0:ctrl_steps])

        # 提取水池水深。
        ponds_id, juncs_id = env.get_ctrl_nodes_id()
        num_ponds = len(ponds_id)
        num_juncs = len(juncs_id)
        all_ponds_depth = all_states[:, :num_ponds]

        # 提取总溢流体积。
        all_flooding = all_states[:, num_ponds:2 * num_ponds + num_juncs]

        # 统计每回合的平均奖励。
        avg_rewards = []
        num_episodes = int(agent._memory.nb_entries / ctrl_steps)
        for i in range(num_episodes):
            temp_rwd = all_rewards[ctrl_steps * i:ctrl_steps * (i + 1)]
            avg_rewards.append(np.mean(temp_rwd))

        return all_rewards, all_actions, all_ponds_depth, all_flooding, avg_rewards

    rewards, actions, depths, flooding, avg_rewards = extract_result(swmm_env, agent)
    # total_flood = agent._extract_flooding_volume()
    actions = np.maximum(actions, 0.0)  # env类生效的动作（孔口相对开度为0~1）
    actions = np.minimum(actions, 1.0)
    rainfalls = pd.read_csv(fcst_inp)
    total_rainfalls = rainfalls['rain1_total'] + rainfalls['rain2_total']

    # 展示结果
    plt.subplot(5, 1, 1)
    depth_plot = plt.plot(depths)
    plt.ylim(0, 6)
    plt.title('depths')
    plt.ylabel('ft')

    plt.subplot(5, 1, 2)
    plt.plot(total_rainfalls, color='b')
    plt.title('total_rainfalls')
    plt.ylabel('rainfall')
    plt.xlabel('time step')

    plt.subplot(5, 1, 3)
    act_plot = plt.plot(actions[:, 0], '-', actions[:, 1], ':')
    plt.ylim(0, 1.05)
    plt.title('Policy')
    plt.ylabel('Valve Position')
    plt.xlabel('time step')
    first_legend = plt.legend(act_plot, ctrl_orifices)

    plt.subplot(5, 1, 4)
    plt.plot(flooding, label=ctrl_ponds + ctrl_juncs)
    plt.ylim(0)
    plt.title('Flooding')
    plt.ylabel('CFS')
    # flood_str = "Total Vol. = " + str(round(total_flood, 3)) + "MG"
    # _, top = plt.gca().get_ylim()
    # flood_max = top * 0.85
    # plt.text(0, flood_max, flood_str)

    plt.subplot(5, 1, 5)
    plt.plot(rewards, color='k')
    plt.title('Rewards')
    plt.ylabel('reward')
    plt.xlabel('time step')

    plt.tight_layout()
    plt.show()
