# -*- encoding: utf-8 -*-
"""
基于 tf2 的 LSTM 自定义时序数据预报模型。

LSTM 模型未考虑输入时序数据的时间间隔，所以要求在数据前处理中保证所有数据集采用相同的时间间隔。
LSTM 模型支持单维单步预报、单维多步预报、多维单步预报、多维多步预报。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from __future__ import annotations
from predictor import ABCPredictor
from FloodMaster.utils import StdScaler, OrdinalEncoder

import os
import json
import numpy as np
import pandas as pd

from tensorflow.python.keras import models, layers, callbacks
from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.metrics import mean_absolute_error, mean_squared_error


class LstmPredictor(ABCPredictor):
    """
    基于 tf2 的 LSTM 自定义时序数据预报模型。

    基于 tf2 的 lstm 模型支持多次的增量训练，即同模型多次调用 `fit()` 接口。因此，
    模型支持在线持续学习。
    """

    def __init__(self, ID: str):
        """
        初始化模型，定义数据集特征和标签。
        Args
        ----
        + ID(str): 模型ID(要求ID唯一);
        """
        self._id = ID
        self._model = None
        self._history = None
        self._confs = {'features': [], 'labels': []}

        x_encoder_id, y_encoder_id = self._get_encoder_ids()
        self._x_encoder = OrdinalEncoder(x_encoder_id)
        self._y_encoder = OrdinalEncoder(y_encoder_id)

        x_scaler_id, y_scaler_id = self._get_scaler_ids()
        self._x_scaler = StdScaler(x_scaler_id)
        self._y_scaler = StdScaler(y_scaler_id)

    def _get_encoder_ids(self):
        """获取模型编码器ID。

        Returns
        ----
        返回标签和特征编码器ID。
        """
        x_encoder_id = f"{self._id}-encoder-feature"
        y_encoder_id = f"{self._id}-encoder-label"
        return x_encoder_id, y_encoder_id

    def _get_scaler_ids(self):
        """获取模型缩放器ID。

        Returns
        ----
        返回标签和特征缩放器ID。
        """
        x_scaler_id = f"{self._id}-scaler-feature"
        y_scaler_id = f"{self._id}-scaler-label"
        return x_scaler_id, y_scaler_id

    def compile(self, confs: dict):
        self._model = models.Sequential()

        # 解析自定义网络配置
        self._confs.update(self._parse_nn_settings(confs))

        # 第一层LSTM网络
        n_past = self._confs['n_past']  # time steps, 采用前n_past步作预报
        n_features = len(self.features)
        lstm_units = self._confs['lstm_units']
        dropout_rate = self._confs['dropout_rate']
        self._model.add(
            layers.LSTM(
                units=lstm_units,
                input_shape=(n_past, n_features),
                return_sequences=True,
                # stateful=True,
                # batch_input_shape=(32, n_past, n_features),
                activation=self._confs['lstm_activation']))
        self._model.add(layers.Dropout(rate=dropout_rate))

        # 中间层LSTM网络
        layper_depth = self._confs['lstm_depth']
        for i in range(1, layper_depth - 1):
            self._model.add(layers.LSTM(units=lstm_units, return_sequences=True))
            self._model.add(layers.Dropout(rate=dropout_rate))

        # 最后一层LSTM网络
        self._model.add(layers.LSTM(units=lstm_units, return_sequences=False))
        self._model.add(layers.Dropout(rate=dropout_rate))

        # 输出层Dense网络
        n_labels = len(self.labels)
        n_forecast = self._confs['n_forecast']  # forecast steps, 预报未来n_forecast步
        dense_units = n_labels * n_forecast  # 重构输出层输出
        self._model.add(layers.Dense(units=dense_units))

        # 激活网络
        self._model.compile(loss=self._confs['loss'],
                            optimizer=self._confs['optimizer'],
                            metrics=self._confs['metrics'])

    def _parse_nn_settings(self, confs):
        """解析神经网络结构自定义配置。
        """
        confs_nn = {}
        confs_keys = confs.keys()

        # 必须配置的参数
        if not isinstance(confs['features'], list):  # 特征IDs
            confs_nn['features'] = []
        else:
            confs_nn['features'] = confs['features']

        if not isinstance(confs['labels'], list):  # 标签IDs
            confs_nn['labels'] = []
        else:
            confs_nn['labels'] = confs['labels']

        # 带有默认配置的参数(可选配置)
        if 'n_past' in confs_keys and self.is_float_integer(confs['n_past']):
            confs_nn['n_past'] = int(confs['n_past'])  # 滑动窗口大小
        else:
            confs_nn['n_past'] = 1

        if 'n_forecast' in confs_keys and self.is_float_integer(confs['n_forecast']):
            confs_nn['n_forecast'] = int(confs['n_forecast'])  # 预报窗口大小
        else:
            confs_nn['n_forecast'] = 1

        if 'save_path' in confs_keys:
            confs_nn['save_path'] = str(confs['save_path'])  # 模型训练结果保存路径
        else:
            confs_nn['save_path'] = os.getcwd()

        if 'lstm_units' in confs_keys and self.is_float_integer(confs['lstm_units']):
            confs_nn['lstm_units'] = int(confs['lstm_units'])  # lstm 层中并列单元数量
        else:
            confs_nn['lstm_units'] = 50

        if 'lstm_activation' in confs_keys and isinstance(confs['lstm_activation'],
                                                          str):
            confs_nn['lstm_activation'] = confs['lstm_activation']
        else:
            confs_nn['lstm_activation'] = 'tanh'  # lstm 层中的激活函数

        if 'lstm_depth' in confs_keys and self.is_float_integer(confs['lstm_depth']):
            confs_nn['lstm_depth'] = int(confs['lstm_depth'])
        else:
            confs_nn['lstm_depth'] = 2  # 中间 lstm 层数（采用相同units）

        if 'dropout_rate' in confs_keys and self.is_float_integer(
                confs['dropout_rate']):
            confs_nn['dropout_rate'] = confs['dropout_rate']
        else:
            confs_nn['dropout_rate'] = 0.2  # dropout 层丢失率

        if 'loss' in confs_keys and isinstance(confs['loss'], str):
            confs_nn['loss'] = confs['loss']  # 损失函数
        else:
            confs_nn['loss'] = 'mse'

        if 'optimizer' in confs_keys and isinstance(confs['optimizer'], str):
            confs_nn['optimizer'] = confs['optimizer']
        else:
            confs_nn['optimizer'] = 'adam'  # 训练优化器，控制梯度裁剪

        if 'metrics' in confs_keys and isinstance(confs['metrics'], list):
            confs_nn['metrics'] = confs['metrics']
        else:
            confs_nn['metrics'] = ['accuracy']  # 训练评估模式，不用于权重更新

        return confs_nn

    @staticmethod
    def is_float_integer(var) -> bool:
        """检查变量是否是一个整数或浮点数。
        """
        isInteger = np.issubdtype(type(var), np.integer)
        isFloat = np.issubdtype(type(var), np.floating)
        return isInteger or isFloat

    def fit(self, train_x: np.array, train_y: np.array, confs: dict):
        # 检查输入参数格式。
        if not isinstance(train_x, np.ndarray) or not isinstance(train_y, np.ndarray):
            raise IOError("LstmPredictor.fit() requires `numpy.ndarray`")

        # 判断模型是否配置完成。
        if not self._model:
            raise RuntimeError(f"LstmPredictor({self._id}): not initialized.")

        # 解析拟合配置。
        self._confs.update(self._parse_fitting_settings(confs))

        # 标准化数据集并生成符合预报器配置的训练集。
        x_samples, y_samples = self._create_train_samples(train_x, train_y)

        # 配置提前结束配置，防止过拟合。
        earlystop = callbacks.EarlyStopping(monitor='val_accuracy',
                                            min_delta=0.0001,
                                            patience=2)

        # 执行训练
        self._history = self._model.fit(
            x_samples,
            y_samples,
            # shuffle=False,
            epochs=self._confs['epochs'],
            batch_size=self._confs['batch_size'],
            validation_split=self._confs['validation_split'],
            callbacks=[earlystop],
            verbose=self._confs['verbose'])
        return self._history

    def get_fit_history(self) -> dict:
        """获取模型训练过程中的准确率和损失过程。

        该方法返回模型最近一次训练过程中训练集和验证集上的准确率和损失过程。
        如果模型未经过训练，则模型返回 `None`。

        Returns
        ----
        模型训练过程，包括训练集上的准确率 'accuracy'，损失 'loss';
        验证集上的准确率 'val_accuracy'，损失 'val_loss'。
        相应的值是各项指标单值的列表。
        """
        if self._history is not None:
            return self._history.history
        else:
            return None

    def _parse_fitting_settings(self, confs):
        """解析模型训练自定义配置。
        """
        confs_fit = {}
        confs_keys = confs.keys() if confs else []

        # 带有默认配置的参数(可选配置)
        if 'epochs' in confs_keys and self.is_float_integer(confs['epochs']):
            confs_fit['epochs'] = int(confs['epochs'])  # 训练次数
        else:
            confs_fit['epochs'] = 10

        if 'batch_size' in confs_keys and self.is_float_integer(confs['batch_size']):
            confs_fit['batch_size'] = int(confs['batch_size'])
        else:
            confs_fit['batch_size'] = 32  # 训练批次大小

        if 'time_step' in confs_keys and self.is_float_integer(confs['time_step']):
            confs_fit['time_step'] = confs['time_step']  # 数据集的时间步长(seconds)
        else:
            confs_fit['time_step'] = 3600

        if 'validation_split' in confs_keys and self.is_float_integer(
                confs['validation_split']):
            confs_fit['validation_split'] = confs['validation_split']
        else:
            confs_fit['validation_split'] = 0.2  # 数据集中拆分验证集的比例

        if 'verbose' in confs_keys and self.is_float_integer(confs['verbose']):
            confs_fit['verbose'] = int(confs['verbose'])
        else:
            confs_fit['verbose'] = 0  # 训练过程中日志输出等级(0为不输出日志)

        return confs_fit

    def _parse_numpy_to_pandas(self, array, columns):
        """将numpy数组转为pandas数据。

        由于 数值数据和字符串数据共存于一个数组中, 可能导致全部为字符串类型。
        这会导致数据集编码异常。

        同时，这也说明整数类型和浮点数类型可能无法区分。

        另外, 要求数据集中不存在 NAN等非法数据, 以及每组数据的类型排列一致。
        """
        df = pd.DataFrame(array, columns=columns)
        for col in df.columns:
            fst_elem = df[col].iloc[0]
            if isinstance(fst_elem, str) and self._is_num_in_str(fst_elem):
                df[col] = df[col].astype(np.float64)
        return df

    def _is_num_in_str(self, str_elem):
        """判断字符串是否为数值类型(包括整数、浮点数、负数)。
        """
        if str_elem[0] == '-':  # 负数
            str_elem = str_elem[1:]
        if str_elem.isdigit():  # 整数
            return True
        str_arr = str_elem.split('.')  # 浮点数
        if len(str_arr) > 2:
            return False
        for s in str_arr:
            if not s.isdigit():
                return False
        return True

    def _create_train_samples(self, train_x, train_y):
        """根据数据集生成训练样本集。
        """
        # 重构数据集。
        train_x_df = self._parse_numpy_to_pandas(train_x, self.features)
        train_y_df = self._parse_numpy_to_pandas(train_y, self.labels)

        # 训练分类器。
        self._y_encoder.partial_fit(train_y_df)
        self._x_encoder.partial_fit(train_x_df)
        train_y_encoded = self._y_encoder.transform(train_y_df)
        train_x_encoded = self._x_encoder.transform(train_x_df)

        # 训练缩放器。
        self._x_scaler.partial_fit(train_x_encoded)
        self._y_scaler.partial_fit(train_y_encoded)
        train_x_scaled = self._x_scaler.transform(train_x_encoded)
        train_y_scaled = self._y_scaler.transform(train_y_encoded)

        # 根据预报步长重构标签数据集，但同时不修改confs['labels'](即模型内部维护对应关系)。
        # 注意，这里的‘滑动步长stride’和‘采样步长sampling_rate’均为1。
        n_forecast = self._confs['n_forecast']
        train_y_refactor = []
        for i in range(n_forecast, train_y_scaled.shape[0]):
            y = train_y_scaled[i - n_forecast]
            for j in range(1, n_forecast):
                y = np.append(y, train_y_scaled[i + j - n_forecast])
            train_y_refactor.append(y)
        train_y_refactor = np.array(train_y_refactor)

        # 生成样本集。
        x_size = train_x_scaled.shape[0]
        y_size = train_y_refactor.shape[0]
        size = min(x_size, y_size)
        x_samples, y_samples = self._generate_samples(train_x_scaled[:size],
                                                      train_y_refactor[:size], True)
        return x_samples, y_samples

    def _generate_samples(self, x_dataset, y_dataset, isFitting):
        """根据时间步数生成符合lstm输入形状的样本集。
        """
        # 检查数据集长度。
        x_shape = x_dataset.shape
        y_shape = y_dataset.shape
        if x_shape[0] != y_shape[0]:
            raise ValueError(
                f"LstmPredictor({self._id}): x, y data sizes doesnt match.")

        # 检查数据集特征属性。
        n_features = len(self._confs['features'])
        n_past = self._confs['n_past']
        if x_shape[1] != n_features:
            raise ValueError(
                f"LstmPredictor({self._id}): data doesnt match features properties.")
        if x_shape[0] < n_past:
            raise ValueError(f"LstmPredictor({self._id}): to few feature data.")

        # 检查数据集标签属性。
        n_forecast = self._confs['n_forecast']
        n_labels = len(self._confs['labels'])
        if not isFitting and y_shape[1] != n_labels:
            raise ValueError(
                f"LstmPredictor({self._id}): data doesnt match label properties.")
        if isFitting and y_shape[1] != n_labels * n_forecast:
            raise ValueError(
                f"LstmPredictor({self._id}): data doesnt match label properties.")
        if isFitting and y_shape[0] < n_forecast:
            raise ValueError(f"LstmPredictor({self._id}): to few label data.")

        # 提取数据集。
        if x_shape[0] == n_past:
            x_samples = x_dataset.reshape(-1, n_past, n_features)
            y_samples = y_dataset.reshape(-1, n_labels)
            return x_samples, y_samples

        size = x_shape[0] - n_past
        samples = TimeseriesGenerator(x_dataset,
                                      y_dataset,
                                      length=n_past,
                                      batch_size=size)
        x_samples, y_samples = samples[0][0], samples[0][1]
        return x_samples, y_samples

    def predict(self, pred_x: np.array) -> np.array:
        # 检查输入数据集格式。
        if not isinstance(pred_x, np.ndarray):
            raise IOError("LstmPredictor.predict() requires `numpy.ndarray`")

        # 生成预报数据集。
        x_samples = self._create_pred_samples(pred_x)

        # 执行预报。
        pred_y = self._model.predict(x_samples) if self._model else None

        # 提取预报结果。
        n_forecast = self._confs['n_forecast']
        n_labels = len(self.labels)
        pred_y_extract = pred_y[:, 0:n_labels]
        if n_forecast > 1:
            pred_y_extend = pred_y[-1, (-n_forecast + 1) * n_labels:]
            pred_y_extract = np.append(pred_y_extract, pred_y_extend)
        pred_y_extract = pred_y_extract.reshape(-1, n_labels)

        # 预报结果还原。
        pred_y_inverse = self._inverse_prediction(pred_y_extract)
        return pred_y_inverse

    def _create_pred_samples(self, pred_x):
        """生成预报样本集。
        """
        # 编码数据集。
        pred_x_df = self._parse_numpy_to_pandas(pred_x, self.features)
        pred_x_encoded = self._x_encoder.transform(pred_x_df)

        # 标准化数据集。
        pred_x_scaled = self._x_scaler.transform(pred_x_encoded)
        pred_y_scaled = np.ones([pred_x_scaled.shape[0], len(self.labels)])

        # 生成样本集
        x_samples, _ = self._generate_samples(pred_x_scaled, pred_y_scaled, False)
        return x_samples

    def _inverse_prediction(self, pred_y):
        """将模拟结果逆标准化恢复到实际值。
        """
        # 逆标准化。
        pred_y_1 = self._y_scaler.inverse_transform(pred_y)
        if pred_y_1 is None:
            raise RuntimeError(
                f"LstmPredictor({self._id}): model not loaded or fitted.")

        # 逆编码。
        pred_y_df = pd.DataFrame(pred_y_1, columns=self.labels)
        pred_y_2 = self._y_encoder.inverse_transform(pred_y_df).to_numpy()
        if pred_y_2 is None:
            raise RuntimeError(
                f"LstmPredictor({self._id}): model not loaded or fitted.")
        return pred_y_2

    def evaluate(self, test_x: np.array, test_y: np.array) -> dict:
        # 检查输入参数格式。
        if not isinstance(test_x, np.ndarray) or not isinstance(test_y, np.ndarray):
            raise IOError("LstmPredictor.evaluate() requires `numpy.ndarray`")

        # 执行预报。
        pred_y = self.predict(test_x)
        if pred_y is None:
            raise RuntimeError(f"LstmPredictor({self._id}): prediction error.")

        # 进行评估。
        scores = {}
        n_past = self._confs['n_past']
        n_forecast = self._confs['n_forecast']
        for i in range(len(self.labels)):
            label_id = self._confs['labels'][i]
            test_y_i = test_y[n_past:, i]  # 实测结果剔除前期无用结果
            if n_forecast < 2:
                pred_y_i = pred_y[:, i]
            else:
                pred_y_i = pred_y[:-n_forecast + 1, i]  # 剔除提前预报结果
            mae = mean_absolute_error(test_y_i, pred_y_i)
            mse = mean_squared_error(test_y_i, pred_y_i)
            scores[label_id] = {'mae': mae, 'mse': mse}
        return scores

    def get_model_confs(self) -> dict:
        """获取模型配置。
        注意，模型在不同阶段的配置属性可能不同。

        Returns
        ----
        返回模型配置。
        """
        return self._confs

    def save(self):
        save_path = self._confs['save_path']
        # 保存模型。
        self._model.save(self._get_model_file(save_path))
        # 保存编码器。
        x_id, y_id = self._get_encoder_ids()
        self._x_encoder.save(*self._get_encoder_file(save_path, x_id))
        self._y_encoder.save(*self._get_encoder_file(save_path, y_id))
        # 保存定标器。
        x_id, y_id = self._get_scaler_ids()
        self._x_scaler.save(*self._get_scaler_file(save_path, x_id))
        self._y_scaler.save(*self._get_scaler_file(save_path, y_id))
        # 保存模型配置属性。
        with open(self._get_confs_file(save_path), 'w', encoding='utf8') as fo:
            json.dump(self._confs, fo)

    def reset(self, **kwargs):
        self._model = kwargs['model']
        self._x_encoder = kwargs['x_encoder']
        self._y_encoder = kwargs['y_encoder']
        self._x_scaler = kwargs['x_scaler']
        self._y_scaler = kwargs['y_scaler']
        self._confs = kwargs['confs']

    @staticmethod
    def load(ID: str, load_path: str) -> LstmPredictor:
        lstm = LstmPredictor(ID)
        # 加载模型。
        model = models.load_model(lstm._get_model_file(load_path))
        # 加载编码器。
        x_id, y_id = lstm._get_encoder_ids()
        x_encoder = OrdinalEncoder.load(x_id, *lstm._get_encoder_file(load_path, x_id))
        y_encoder = OrdinalEncoder.load(y_id, *lstm._get_encoder_file(load_path, y_id))
        # 加载定标器。
        x_id, y_id = lstm._get_scaler_ids()
        x_scaler = StdScaler.load(x_id, *lstm._get_scaler_file(load_path, x_id))
        y_scaler = StdScaler.load(y_id, *lstm._get_scaler_file(load_path, y_id))
        # 加载模型配置属性。
        with open(lstm._get_confs_file(load_path), 'r', encoding='utf8') as fi:
            confs = json.load(fi)
        # 配置模型
        lstm.reset(model=model,
                   x_encoder=x_encoder,
                   y_encoder=y_encoder,
                   x_scaler=x_scaler,
                   y_scaler=y_scaler,
                   confs=confs)
        return lstm

    def _get_model_file(self, parent_dir):
        """配置模型保存和加载文件。
        """
        model_path = os.path.join(parent_dir, self._id)
        if not os.path.exists(model_path):
            os.makedirs(model_path)

        model_file = os.path.join(model_path, f'GR-LSTM-{self._id}-model.h5')
        return model_file

    def _get_scaler_file(self, parent_dir, scaler_id):
        """配置定标器保存和加载文件。
        """
        model_path = os.path.join(parent_dir, self._id)
        if not os.path.exists(model_path):
            os.makedirs(model_path)

        scaler_file = os.path.join(model_path, f'GR-LSTM-{scaler_id}-scaler.pkl')
        property_file = os.path.join(model_path,
                                     f'GR-LSTM-{scaler_id}-scaler-property.json')
        return scaler_file, property_file

    def _get_encoder_file(self, parent_dir, encoder_id):
        """配置编码器保存和加载文件。
        """
        model_path = os.path.join(parent_dir, self._id)
        if not os.path.exists(model_path):
            os.makedirs(model_path)

        encoder_file = os.path.join(model_path, f'GR-LSTM-{encoder_id}-encoder.pkl')
        property_file = os.path.join(model_path,
                                     f'GR-LSTM-{encoder_id}-encoder-property.json')
        return encoder_file, property_file

    def _get_confs_file(self, parent_dir):
        """配置自定义配置保存和加载文件。
        """
        confs_path = os.path.join(parent_dir, self._id)
        if not os.path.exists(confs_path):
            os.makedirs(confs_path)

        confs_file = os.path.join(confs_path, f'GR-LSTM-{self._id}-confs.json')
        return confs_file

    def summary(self):
        if self._model:
            self._model.summary()

    @property
    def features(self):
        return self._confs['features']

    @property
    def labels(self):
        return self._confs['labels']
