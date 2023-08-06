# -*- encoding: utf-8 -*-
"""
时序数据预报模型的统一接口类。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from abc import abstractmethod, ABCMeta
from typing import Any
import numpy as np


class ABCPredictor(metaclass=ABCMeta):
    """
    时序数据预报模型的统一接口类。几种基本的调用方式：

    1. 方式一，
    初始化(compile) -> 训练(fit) -> 评估(evaluate) -> 预报(predict) -> 保存(save).

    2. 方式二，
    加载(load) -> 预报(predict).

    3. 方式三，
    加载(load) -> 训练(fit) -> 评估(evaluate) -> 保存(save).

    """

    @abstractmethod
    def compile(self, confs: dict):
        """
        初始化模型，配置模型结构。

        Args
        ----
        + confs(dict): 模型配置基本信息, 包括特征IDs、标签IDs、采样步长、预报步长等。
        """
        raise NotImplementedError()

    @abstractmethod
    def fit(self, train_x: np.array, train_y: np.array, confs: dict) -> dict:
        """
        加载训练数据集，训练模型。

        Args
        ----
        + train_x(np.array): 原始二维数据集的特征向量(sample_size*feature_size);
        + train_y(np.array): 原始二维数据集的标签向量(sample_size*label_size);
        + confs(dict): 模型训练配置信息，包括训练次数、批次大小，日志等级等。

        Returns
        ----
        返回模型训练过程信息, 例如训练集和验证集上各项指标的准确率和损失。
        """
        raise NotImplementedError()

    @abstractmethod
    def predict(self, pred_x: np.array) -> np.array:
        """
        预报数据标签向量。

        Args
        ----
        + pred_x(np.array): 原始二维数据集的特征向量(sample_size*feature_size);

        Returns
        ----
        返回预报的标签向量。
        """
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self, test_x: np.array, test_y: np.array) -> dict:
        """
        评估(测试)模型。

        Args
        ----
        + test_x(np.array): 原始二维数据集的特征向量(sample_size*feature_size);
        + test_y(np.array): 原始二维数据集的标签向量(sample_size*label_size);

        Returns
        ----
        返回各标签的各项评估结果, 包括 mse/mae 等等。
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self):
        """
        保存模型到本地。
        """
        raise NotImplementedError()

    @abstractmethod
    def reset(self, **kwars):
        """
        重置模型。
        """
        raise NotImplementedError()

    @staticmethod
    def load(ID: str, load_path: str) -> Any:
        """
        从本地加载模型。

        Args
        ----
        + ID(str): 模型ID;
        + load_path(str): 模型加载路径;

        Returns
        ----
        返回模型对象。
        """
        raise NotImplementedError()

    @abstractmethod
    def summary(self):
        """
        输出模型的配置。
        """
        raise NotImplementedError()

    @property
    def features(self):
        """
        模型预报的特征列表IDs。
        """
        return None

    @property
    def labels(self):
        """
        模型接受的标签列表IDs。
        """
        return None
