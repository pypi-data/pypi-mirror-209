# -*- encoding: utf-8 -*-
"""
基于pyswmm的强化学习环境。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
import numpy as np
from pyswmm import Simulation, Nodes, Links
from rl.core import Env  # 非本地版本
from gym import spaces  # 非本地版本


class PySwmmEnv(Env):
    """基于 Env 接口的 pyswmm 强化学习环境。

    该环境通过加载swmm输入文件初始化pyswmm模型, 并暴露指定的控制对象, 包括水池、孔口和节点。
    该环境同时限定了实时控制的方式, 即通过调控孔口对象来维持水池目标水深和减少节点溢流。
    """

    def __init__(self):
        self._input_file = None  # swmm输入文件
        self._fcst_file = None  # 降雨/潮汐时间序列文件
        self._ctrl_step = None  # 调度步长
        self._ponds_id = None  # 目标/受控水池ID
        self._max_depths = {}  # 目标/受控水池最大深度
        self._target_depths = {}  # 目标/受控水池目标深度
        self._orifices_id = None  # 目标/受控孔口ID
        self._juncs_id = None  # 目标/受控节点ID

        self._rainfall_fcst = None  # 降雨/潮位预报数据
        self._swmm = None  # 模型对象
        self._total_steps = None  # 模型总调度步数
        self._curr_step = None  # 模型当前调度步
        self._ponds = None  # 目标/受控水池对象
        self._juncs = None  # 目标/受控节点对象
        self._orifices = None  # 目标/受控闸孔对象
        self._states = None  # 强化学习环境状态

        self.action_space = None  # 强化学习动作空间
        self.observation_space = None  # 强化学习观测空间

    def init(self, inp_file: str, fcst_file: str, ctrl_step: int, ctrl_ponds: list,
             ponds_max_depth: list, ponds_target: list, ctrl_orifices: list,
             ctrl_junctions: list):
        """初始化pyswmm模型控制环境。
        为了能够更加自由的组装强化学习控制器，将初始化方法独立出来。

        Args
        ----
        + inp_file(str): swmm 项目配置文件;
        + fcst_file(str): 降雨/潮位预报文件;
        + ctrl_step(int): 受控闸门调度时间步长(seconds);
        + ctrl_ponds(list of str): 受控水池IDs;
        + ponds_max_depth(list of float): 各受控水池的最大水深;
        + ponds_target(list of float): 各受控水池的目标水深;
        + ctrl_orifices(list of str): 受控孔口/闸门IDs;
        + ctrl_junctions(list of str): 受控节点IDs;
        """
        self.reset()

        self._input_file = inp_file
        self._fcst_file = fcst_file
        self._ctrl_step = ctrl_step
        self._ponds_id = ctrl_ponds
        self._max_depths = dict(zip(ctrl_ponds, ponds_max_depth))
        self._target_depths = dict(zip(ctrl_ponds, ponds_target))
        self._orifices_id = ctrl_orifices
        self._juncs_id = ctrl_junctions

        # 加载降雨/潮位预报数据。
        self._rainfall_fcst = self._load_forecast_file()

        # 初始化pyswmm模型, 获取模型对象以及总调度步数、当前调度步。
        self._swmm, self._total_steps, self._curr_step = self._init_simulation()

        # 获取目标/受控对象。
        self._ponds, self._juncs, self._orifices = self._get_target_objects()

        # 定义强化学习环境状态。
        self._states = self._get_env_states()

        # 定义强化学习动作空间。
        self.action_space = self._get_action_space()

        # 定义强化学习观测空间。
        self.observation_space = self._get_observation_space()

    def _load_forecast_file(self):
        """读入csv格式的降雨/潮位预报文件。
        """
        fcst_data = np.genfromtxt(self._fcst_file, delimiter=',')
        return fcst_data

    def _init_simulation(self):
        """初始化swmm模拟引擎。
        """
        simu = Simulation(self._input_file)
        simu.step_advance(self._ctrl_step)  # 设置模型步进步长（此处即模型调度步长）
        simu.start()

        # 获取调度控制步长信息。
        simu_len = simu.end_time - simu.start_time
        total_ctrl_steps = int(simu_len.total_seconds() / self._ctrl_step)  # 总实时调度步数
        curr_ctrl_step = 1  # 当前调度步
        return simu, total_ctrl_steps, curr_ctrl_step

    def _get_target_objects(self):
        """从模拟引擎中提取目标/控制对象。
        """
        # 水池对象
        node_objs = Nodes(self._swmm)
        ponds = {pond: node_objs[pond] for pond in self._ponds_id}

        # 汊点对象
        juncs = {junc: node_objs[junc] for junc in self._juncs_id}

        # 水闸对象
        link_objs = Links(self._swmm)
        orifices = {orifice: link_objs[orifice] for orifice in self._orifices_id}

        return ponds, juncs, orifices

    def _get_env_states(self):
        """定义环境状态。

        [目标水池深度] + [水池的溢流状态] + [目标节点的溢流状态] + [目标水闸的相对开度] + [降雨/潮位预报]
        """
        pond_depth_states = [pond.depth for pond in self._ponds.values()]  # 目标水池的深度状态
        pond_flooding_states = [pond.flooding
                                for pond in self._ponds.values()]  # 目标水池的溢流状态
        junc_flooding_states = [junc.flooding
                                for junc in self._juncs.values()]  # 目标节点的溢流状态
        orifice_opening_states = [
            orifice.current_setting for orifice in self._orifices.values()
        ]  # 目标水闸的相对开度状态
        fcst_states = self._rainfall_fcst[self._curr_step].tolist()  # 降雨/潮位预报状态

        states = pond_depth_states + pond_flooding_states + junc_flooding_states
        states = states + orifice_opening_states + fcst_states
        states = np.asarray(states)
        return states

    def _get_action_space(self):
        """定义目标水闸的开度（动作）范围。
        """
        low_bounds = [0.0 for _ in self._orifices_id]
        high_bounds = [1.0 for _ in self._orifices_id]
        action_space = spaces.Box(low=np.array(low_bounds),
                                  high=np.array(high_bounds),
                                  shape=(len(self._orifices_id), ),
                                  dtype=np.double)
        return action_space

    def _get_observation_space(self):
        """定义观察空间。（维度与状态空间一致）
        """
        observation_space = spaces.Box(low=0,
                                       high=1000,
                                       shape=(len(self._states), ),
                                       dtype=np.float32)
        return observation_space

    def step(self, actions) -> tuple:
        """执行控制动作并按调度步长执行模拟，更新模型，计算回报。

        Args
        ----
        + actions: 各受控孔口的相对开度状态。

        Returns
        ----
        返回(当前状态, 奖励值, 模型是否结束, 其他模型信息)。
        """
        # 配置动作
        for orifice, action in zip(self._orifices_id, actions):
            action = min(max(float(action), 0.0), 1.0)
            self._orifices[orifice].target_setting = action

        # 推进到下一步。
        # self._swmm.__next__()
        self._swmm.step_advance(self._ctrl_step)

        # 获取当前系统状态。
        self._states = self._get_env_states()

        # 计算奖励。
        pond_num = len(self._ponds_id)
        junc_num = len(self._juncs_id)
        if np.sum(self._rainfall_fcst[self._curr_step, :-1]) > 0.:  # 检查预报降雨状态
            # 降雨期以预防洪水为控制目标。
            pond_flooding = sum(self._states[pond_num:2 * pond_num])
            junc_flooding = sum(self._states[2 * pond_num:2 * pond_num + junc_num])
            reward = -(pond_flooding + junc_flooding)
        else:
            # 干旱期以预防节点溢流和保持蓄水池水位为控制目标。
            junc_flooding = sum(self._states[2 * pond_num:2 * pond_num + junc_num])
            pond_depth = sum([
                abs(self._ponds[pond].depth - self._target_depths[pond])
                for pond in self._ponds_id
            ])
            reward = -(junc_flooding + pond_depth)

        # 判断是否模拟结束。
        if self._curr_step < self._total_steps - 1:
            done = False
        else:
            done = True
        self._curr_step += 1

        info = {}  # 其他信息。
        return self._states, reward, done, info

    def reset(self) -> np.ndarray:
        """重启模型。
        """
        if not self._swmm:
            return None
        self._swmm.close()
        self._swmm, self._total_steps, self._curr_step = self._init_simulation()
        self._states = self._get_env_states()
        return self._states

    def close(self):
        """关闭模型。
        """
        self._swmm.report()
        self._swmm.close()

    @property
    def states(self):
        return self._states

    @property
    def configs(self):
        """
        获取环境配置。
        """
        configs = {}
        configs['input_file'] = self._input_file
        configs['fcst_file'] = self._fcst_file
        configs['ctrl_step'] = self._ctrl_step
        configs['ponds_id'] = self._ponds_id
        configs['ponds_target_depth'] = self._target_depths
        configs['orifices_id'] = self._orifices_id
        configs['juncs_id'] = self._juncs_id
        return configs

    def __del__(self):
        self.close()

    def __str__(self):
        return '<{} instance>'.format(type(self).__name__)

    def get_swmm_file(self) -> str:
        """获取swmm输入文件。

        Returns
        ----
        返回swmm文件全路径名。
        """
        return self._input_file

    def get_ctrl_nodes_id(self) -> tuple:
        """获取受控水池和节点对象Ids.

        Returns
        ----
        返回受控水池和节点对象IDs。
        """
        return self._ponds_id, self._juncs_id

    def get_ctrl_links_id(self) -> list:
        """获取受控水闸对象Ids.

        Returns
        ----
        返回受控水闸对象IDs。
        """
        return self._orifices_id
