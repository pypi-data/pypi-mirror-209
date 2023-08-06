# -*- encoding: utf-8 -*-
"""
数据集规范化工具。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import os
import joblib
import json


class StdScaler():
    """
    采用 sklearn 的 StandardScaler 的数据标准化工具，其归一化原理为：

    先通过计算数据集中特征的均值、标准差，对每个特征进行独立居中和缩放；
    然后，将平均值和标准偏差存储起来，在以后的测试集上有相同比例来缩放。

    标准化是对列操作的，一维数组每列中只有一个值，无法计算。解决办法是，
    通过reshape(-1, 1)，将一维数组改为二维数组。
    """
    def __init__(self, ID: str):
        """设置标准缩放器的基本配置。

        Args
        ----
        + ID(str): 定标器ID
        """
        self._scaler = StandardScaler()
        self._id = ID
        self._fitted = False  # 标准缩放器是否训练好的标识

    def fit_transform(self, train_df: pd.DataFrame) -> np.array:
        """计算并存储数据集各列的均值、标准差，并对数据集执行标准化。

        Args
        ----
        + train_df(pd.DataFrame): 训练数据集;

        Returns
        ----
        返回标准化之后的数据集。
        """
        self._fitted = False
        train_df_scaled = self._scaler.fit_transform(train_df)
        self._fitted = True
        return train_df_scaled

    def fit(self, train_df: pd.DataFrame):
        """计算并存储数据集各列的均值、标准差。

        Args
        ----
        + train_df(pd.DataFrame): 训练数据集;
        """
        self._fitted = False
        self._scaler.fit(train_df)
        self._fitted = True

    def partial_fit(self, train_df: pd.DataFrame):
        """计算并存储数据集各列的均值、标准差(可以保留之前训练结果作增量训练)。

        Args
        ----
        + train_df(pd.DataFrame): 训练数据集;
        """
        self._scaler.partial_fit(train_df)
        self._fitted = True

    def transform(self, test_df: pd.DataFrame) -> np.array:
        """以已经训练好的标准缩放器，通过居中和缩放执行标准化。

        Args
        ----
        + test_df(pd.DataFrame): 测试数据集;

        Returns
        ----
        返回标准化之后的数据集; 如果没有训练好的缩放器, 则返回None。
        """
        if not self._fitted:
            print(f"ERROR: StdScaler({self._id}) is not fitted yet.")
            return None

        test_df_scaled = self._scaler.transform(test_df)
        return test_df_scaled

    def inverse_transform(self, pred_arr: np.array) -> np.array:
        """以已经训练好的标准缩放器，将数据按比例恢复到以前的大小。

        Args
        ----
        + pred_arr(np.array): 标准化后的数据集;

        Returns
        ----
        返回逆标准化后的数据集; 如果没有训练好的缩放器, 则返回None。
        """
        if not self._fitted:
            print(f"ERROR: StdScaler({self._id}) is not fitted yet.")
            return None

        pred_arr_anti = self._scaler.inverse_transform(pred_arr)
        return pred_arr_anti

    def is_fitted(self) -> bool:
        """缩放器是否经过训练。
        """
        return self._fitted

    def save(self, scaler_file: str, property_file: str):
        """将缩放器保存到本地。

        Args
        ----
        + scaler_file(str): 保存文件名(.pkl文件, 完整路径);
        + property_file(str): 保存缩放器器属性文件名(.json文件, 完整路径);
        """
        # 保持缩放器。
        scaler_path = os.path.dirname(scaler_file)
        if not os.path.exists(scaler_path):
            os.makedirs(scaler_path)
        joblib.dump(self._scaler, scaler_file)

        # 保存缩放器属性。
        property_path = os.path.dirname(property_file)
        if not os.path.exists(property_path):
            os.makedirs(property_path)
        with open(property_file, 'w', encoding='utf8') as fo:
            json.dump({"fitted": self._fitted}, fo)

    def set_scaler(self, scaler: StandardScaler, fitted: bool):
        """直接设置(训练好的)数据缩放器。

        Args
        ----
        + scaler(StandardScaler): 训练好的缩放器;
        + fitted(bool): 缩放器是否是训练过;
        """
        self._scaler = scaler
        self._fitted = fitted

    @staticmethod
    def load(ID: str, scaler_file: str, property_file: str):
        """从本地加载到缩放器。

        Args
        ----
        + ID(str): 定标器ID;
        + scaler_file(str): 本地缩放器文件名(.pkl文件, 完整路径);
        + property_file(str): 保存缩放器器属性文件名(.json文件, 完整路径);
        """
        with open(property_file, 'r', encoding='utf8') as fi:
            encoder_properties = json.load(fi)
        fitted = encoder_properties['fitted']

        scaler = StdScaler(ID)
        scaler.set_scaler(joblib.load(scaler_file), fitted)
        return scaler
