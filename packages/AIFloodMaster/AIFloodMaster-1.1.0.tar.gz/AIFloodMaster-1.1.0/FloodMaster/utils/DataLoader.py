# -*- encoding: utf-8 -*-
"""
数据集加载及前处理工具。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
import pandas as pd
import numpy as np
from DataPreprocessor import DatasetPreprocessor


class CsvLoader():
    """
    CSV 数据集加载工具。时序数据格式要求为 CSV 格式，同时要求：

    1. 第一行为表头说明;
    2. 空行不影响读取；
    3. 数据集特征和标签均位于同一份文件中。

    对于多站点多日期数据集，应该指定提取某个站点的数据集。
    """
    def __init__(self, data_file: str, features: list, labels: list, **kwargs):
        """
        Args
        ----
        + data_file(str): 数据集csv文件;
        + features(list of str): 数据集特征;
        + labels(list of str): 数据集标签;
        + kwargs: 可选参数，包括：
            + date_col(str): 时间戳列的列名(默认为'Date');
            + time_step(int): 数据的时间步长(seconds, 默认3600);
            + date_fmt(str): 日期数据输入格式(默认'%Y/%m/%d');
            + start_date(str): 截取数据集的起始日期(时间格式和date_fmt相同);
            + end_date(str): 截取数据集的起始日期(时间格式和date_fmt相同);
            + index_col(str): 数据集中的索引列(如站点数据集中'STCD');
            + index_selected(str): 数据集中截取的索引ID(如站点'10001');
        """
        self._features = features
        self._labels = labels
        self._data_file = data_file
        self._opt_confs = self._check_optional_args(kwargs)

        if "index_col" in self._opt_confs.keys() and self._opt_confs['index_col']:
            index = self._opt_confs['index_col']
            self._df = pd.read_csv(self._data_file, dtype={index: str})
        else:
            self._df = pd.read_csv(self._data_file)

        self._check_ids()
        self._intercept_dataset_by_index()
        self._check_nan()
        self._intercept_dataset_by_datetime()
        self._check_continuous()
        self._intercept_dataset_by_columns()

    def _check_optional_args(self, kwargs):
        """解析数据集加载的可选配置参数。
        """
        args_keys = kwargs.keys()
        confs = {}

        if 'date_col' in args_keys:
            confs['date_col'] = kwargs['date_col']
        else:
            confs['date_col'] = 'Date'

        if 'time_step' in args_keys:
            confs['time_step'] = int(kwargs['time_step'])
        else:
            confs['time_step'] = 3600

        if 'date_fmt' in args_keys:
            confs['date_fmt'] = kwargs['date_fmt']
        else:
            confs['date_fmt'] = "%Y/%m/%d"

        if 'start_date' in args_keys:
            confs['start_date'] = kwargs['start_date']

        if 'end_date' in args_keys:
            confs['end_date'] = kwargs['end_date']

        if 'index_col' in args_keys:
            confs['index_col'] = kwargs['index_col']

        if 'index_selected' in args_keys:
            confs['index_selected'] = kwargs['index_selected']

        return confs

    def _check_ids(self):
        """检查数据集特征和标签是否匹配。
        """
        df_data_ids = self._df.columns.to_list()

        miss_feats = [fid for fid in self._features if fid not in df_data_ids]
        miss_labels = [lid for lid in self._labels if lid not in df_data_ids]

        if miss_feats:
            raise ValueError(f"Dataset({self._data_file}) miss features: {miss_feats}")
        if miss_labels:
            raise ValueError(f"Dataset({self._data_file}) miss labels: {miss_labels}")

    def _intercept_dataset_by_index(self):
        """根据用户配置的索引截取数据集。
        """
        # 读取索引列。
        if 'index_col' in self._opt_confs.keys():
            index = self._opt_confs['index_col']
        else:
            index = None

        if 'index_selected' in self._opt_confs.keys():
            index_selected = self._opt_confs['index_selected']
        else:
            index_selected = None

        if index and index_selected:
            self._df = DatasetPreprocessor.intercept_by_cols(self._df, index,
                                                             index_selected)

    def _intercept_dataset_by_datetime(self):
        """根据用户配置的日期范围截取数据集。
        """
        # 提取时间戳并排序。
        date_idx = self._opt_confs['date_col']
        if date_idx not in self._df.columns:
            return

        # 按时间截取数据集。
        if 'start_date' in self._opt_confs.keys():
            start_date = self._opt_confs['start_date']
        else:
            start_date = None

        if 'end_date' in self._opt_confs.keys():
            end_date = self._opt_confs['end_date']
        else:
            end_date = None

        if start_date or end_date:
            self._df = DatasetPreprocessor.intercept_by_datetime(
                self._df, date_idx, self._opt_confs['date_fmt'], start_date, end_date)

    def _intercept_dataset_by_columns(self):
        """删除非特征或标签数据列(注意index列和datetime列)。
        """
        # 统计无效数据列。
        del_cols = []
        for col in self._df.columns:
            if col not in self._features and col not in self._labels:
                del_cols.append(col)

        self._df = DatasetPreprocessor.delete_by_cols(self._df, del_cols)
        self._df.reset_index()

    def _check_nan(self):
        """检查数据集中是否存在NaN, 并采用线性插值。
        """
        self._df = DatasetPreprocessor.check_nan(self._df)

    def _check_continuous(self):
        """检查数据集是否为连续时间序列(并去重), 并向后填充缺失值。
        """
        time_step = self._opt_confs['time_step']
        date_idx = self._opt_confs['date_col']
        date_fmt = self._opt_confs['date_fmt']

        self._df = DatasetPreprocessor.check_datetime_continuous(
            self._df, date_idx, date_fmt, time_step)
        self._df.set_index(date_idx, inplace=True)

    def get_features_dataset(self) -> pd.DataFrame:
        """特征数据集。
        """
        return self._df[self._features]

    def get_labels_dataset(self) -> pd.DataFrame:
        """标签数据集。
        """
        return self._df[self._labels]

    def get_dataset(self) -> pd.DataFrame:
        """返回包含特征和标签的数据集。
        """
        return self._df

    def get_loader_confs(self) -> dict:
        """获取CSV数据加载器的配置。
        """
        return self._opt_confs

    @property
    def features(self) -> list:
        """数据集特征ids。
        """
        return self._features

    @property
    def labels(self) -> list:
        """数据集标签ids。
        """
        return self._labels

    @staticmethod
    def train_test_split(df: pd.DataFrame,
                         features: list,
                         labels: list,
                         test_ratio: float,
                         is_random: bool,
                         random_seed: int = None) -> tuple:
        """将数据集拆分为训练集和测试集。

        Args
        ----
        + df(pd.DataFrame): 包含特征和标签的数据集;
        + features(list): 数据集特征IDs;
        + labels(list): 数据集标签IDs;
        + test_ratio(float): 拆分后测试集的占比;
        + isRandom(bool): 是否采用随机采样拆分数据集;
        + random_seed(int): 随机种子(相同的随机种子保证每次抽样结果相同);

        Returns
        ----
        返回拆分后的训练集和测试集(
            (train_df_features, train_df_labels),
            (test_df_features, test_df_labels))。
        """
        test_df, train_df = None, None

        # 输入检查
        if test_ratio < 0.0 or test_ratio > 1.0:
            raise ValueError(f'CsvLoader has invalid test_ratio: {test_ratio}.')

        # 拆分数据集
        if not is_random:
            test_size = round(df.shape[0] * test_ratio)
            test_size = max(test_size, 1)
            train_df = df[:-test_size]
            test_df = df[-test_size:]
        else:
            if random_seed:
                np.random.seed(random_seed)
            test_df = df.sample(frac=test_ratio)
            train_df = df.sample(frac=1.0 - test_ratio)

        # 拆分特征数据和标签数据
        train_features = train_df[features]
        train_labels = train_df[labels]
        test_features = test_df[features]
        test_labels = test_df[labels]
        return ((train_features, train_labels), (test_features, test_labels))
