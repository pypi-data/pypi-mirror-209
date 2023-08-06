# -*- encoding: utf-8 -*-
"""
数据滤波器，用于数据滤波处理，提供了两种卡尔曼滤波和一种离散贝叶斯综合算法。

卡尔曼滤波算法：

>> 预测
x = F @ x + B @ u
P = alpha * F @ P @ F^T + Q

>> 更新
K = P @ H^T @ (H @ P @ H^T + R)^-1
y = z - H @ x
P = (1 - K @ H) @ P

其中,
x 为状态变量向量, 个数为 nx, 形状为 nx * 1;
z 为观测变量向量, 个数为 nz, 形状为 nz * 1;
u 为控制变量向量, 个数为 nu, 形状为 nu * 1;

然后,
F 为状态转移矩阵, 用于状态更新, 形状为 nx * nx;
B 为控制输入矩阵, 用于将控制变量转换为状态变量, 形状为 nx * nu;
alpha 为遗忘系数, 用于调节对过往信息的依赖程度, 值越大依赖越小;
P 为状态变量的协方差矩阵, 描述状态间的关联关系, 形状为 nx * nx;
Q 为预测误差矩阵, 形状为 nx * nx;
R 为观测误差矩阵, 形状为 nz * nz;
H 为量测矩阵, 用于将状态变量转换为观测变量, 形状为 nz * nx;
K 为卡尔曼增益矩阵, 表征状态最优估计中 Q 与 R 的比重, 形状为 nx * nz;

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from filterpy.kalman import KalmanFilter as KF
from filterpy import discrete_bayes as DB
import numpy as np


class KalmanFilter():
    """卡尔曼滤波滤波器。
    """

    def __init__(self,
                 dim_x: int = 1,
                 dim_z: int = 1,
                 Q: list = None,
                 R: list = None,
                 P: list = None,
                 F: list = None,
                 H: list = None):
        """初始化卡尔曼滤波器。
    
        Args
        ----
        + dim_x(int): 状态变量个数；
        + dim_z(int): 观测变量个数；
        + Q(list): 状态噪声;         
        + R(list): 测量噪声;
        + P(list): 状态协方差矩阵;
        + F(list): 状态转移矩阵;
        + H(list): 测量矩阵;
        """
        # if R and len(R) != dim_z:
        #     raise RuntimeError("All observations' noise should be given in R.")
        # if Q and len(Q) != dim_x:
        #     raise RuntimeError("All states' noise should be given in Q.")

        # filter
        self._kf = KF(dim_x, dim_z)  # dim_x:隐状态大小，dim_z:量测大小

        # 定义参数
        self._kf.x = np.zeros(dim_x).reshape(dim_x, 1)  # 初始状态值, 在利用观测值进行更新时逐渐趋近真实值
        self._kf.P = np.eye(dim_x) if P is None else P  # 状态协方差矩阵, 默认状态间独立不相关
        self._kf.F = np.eye(dim_x) if F is None else F  # 状态转移矩阵, 默认状态间独立不相关

        default_H = np.zeros([dim_z, dim_x])
        default_H[0][0] = 1.0
        self._kf.H = default_H if H is None else H  # 量测矩阵, 默认只取第一个状态值

        self._kf.Q = np.diag([1.] * dim_x) if Q is None else np.diag(Q)  # 预测噪声, 默认为1.0
        self._kf.R = np.diag([1.] * dim_z) if R is None else np.diag(R)  # 量测噪声, 默认为1.0

    def filter(self, measurements: list) -> list:
        """预测更新。

        Args
        ----
        + measurements(list): 观测值序列;

        Returns
        ----
        返回校正结果。
        """
        inputs = np.array(measurements).reshape(-1, self._kf.dim_z)

        filter_result = list()
        for z in inputs:
            self._kf.predict()
            self._kf.update(z)
            filter_result.append(self._kf.x)

        return np.squeeze(np.array(filter_result))


class KalmanFilter2():
    """一维卡尔曼滤波器, 用于滤波实测状态。
    """

    def __init__(self, Q: float, R: float):
        """一维简化卡尔曼滤波器。

        Args
        ----
        + Q(float): 预测预估误差；
        + R(float): 测量误差；
        """
        self._Q = Q
        self._R = R
        self._accumulate_err = 1
        self._last_pred = 0

    def filter(self, obs: float, pred: float) -> float:
        """预测更新。

        Args
        ----
        + obs(float): 当前观测值

        Returns
        ----
        返回校正值。
        """
        # 检查新值和旧值的差异是否在合理范围内
        old_val = None
        if abs(self._last_pred) > 1.e-4 and abs(
            (obs - self._last_pred) / self._last_pred) > 0.25:
            old_val = obs * 0.382 + self._last_pred * 0.618
        else:
            old_val = self._last_pred

        # 计算总误差：累计误差^2 + 预估误差^2
        old_err = (self._accumulate_err**2 + self._Q**2)**(1 / 2)

        # 计算 H
        H = old_err**2 / (old_err**2 + self._R**2)

        # 预测
        pred = old_val + H * (obs - old_val)

        # 更新累积误差
        self._accumulate_err = ((1 - H) * old_err**2)**(1 / 2)
        self._last_pred = pred

        return pred


class BayesFilter():
    """离散贝叶斯滤波器。
    """

    def __init__(self):
        """
        """
        pass


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # KalmanFilter2
    array = np.array([50] * 500)
    mu, sigma = 0, 3
    s = np.random.normal(mu, sigma, 500)
    test_array = array + s

    plt.plot(test_array)

    kf2 = KalmanFilter2(1.e-4, 1.e-1)
    adc = []
    for i in range(500):
        adc.append(kf2.filter(test_array[i]))

    plt.plot(adc)
    plt.plot(array)
    plt.show()

    # KalmanFilter
    measurements = np.linspace(1, 500, 500)
    mu, sigma = 0, 3
    noise = np.random.normal(mu, sigma, 500)
    z_noise = measurements + noise

    plt.plot(z_noise, label="z_noise")

    dim_x, dim_z = 2, 1
    P = np.array([[1, 0], [0, 1]])
    F = np.array([[1, 1], [0, 1]])
    Q = np.array([[0.001, 0], [0, 0.0001]])
    H = np.array([[1, 0]])
    R = np.array([1])
    kf = KalmanFilter(dim_x, dim_z, Q, R, P, F, H)

    z_corr = [v[0] for v in kf.filter(z_noise)]
    plt.plot(z_corr, label="z_corr")
    plt.show()

    # 1d KalmanFilter
    kf3 = KalmanFilter(1, 1, [1.e-4], [1.e-1])
    corr = kf3.filter(test_array)
    plt.plot(test_array)
    plt.plot(array)
    plt.plot(corr)
    plt.show()
