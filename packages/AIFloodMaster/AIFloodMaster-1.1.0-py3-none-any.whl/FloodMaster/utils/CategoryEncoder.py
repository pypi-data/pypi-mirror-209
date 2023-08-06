# -*- encoding: utf-8 -*-
"""
数据集类型变量编码工具。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
import category_encoders as ce
import pandas as pd
import joblib
import os
import json


class LooEncoder():
    """采用 LeaveOneOut 方法编码类别变量，从而可进行机器学习。

    由于该方法属于有监督方法，要求数据集中标签变量为非类别变量。
    同时，该编码方法可以适应不断增加的类别。

    此外，该编码方式为不唯一编码、无法逆编码，不适合标签的编码。
    """
    def __init__(self, ID: str, features: list = None):
        """初始化编码器的基本配置。

        Args
        ----
        + ID(str): 编码器ID;
        + features(list of str): 待编码的类别变量IDs(默认对所有字符型变量编码);
        """
        self._encoder = ce.LeaveOneOutEncoder(cols=features, return_df=True)
        self._id = ID
        self._fitted = False

    def fit_transform(self, features_df: pd.DataFrame,
                      label_df: pd.DataFrame) -> pd.DataFrame:
        """监督训练编码器，并对指定的类别变量编码。

        训练中采用的`features_df`的向量形状(标签数)将在编码器中固定下来，后续
        编码`transform()`中输入的`features_df`的标签数必须与此一致。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);
        + label_df(pd.DataFrame): 标签变量数据集(标签变量必须为数值类型);

        Returns
        ----
        返回类别编码后的数据集。
        """
        features_df_encoded = self._encoder.fit_transform(features_df, label_df)
        self._fitted = True
        return features_df_encoded

    def fit(self, features_df: pd.DataFrame, label_df: pd.DataFrame):
        """监督训练编码器。

        训练中采用的`features_df`的向量形状(标签数)将在编码器中固定下来，后续
        编码`transform()`中输入的`features_df`的标签数必须与此一致。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);
        + label_df(pd.DataFrame): 标签变量一维数据集(标签变量必须为数值类型);
        """
        self._encoder.fit(features_df, label_df)
        self._fitted = True

    def transform(self,
                  features_df: pd.DataFrame,
                  label_df: pd.DataFrame = None) -> pd.DataFrame:
        """通过已经训练好的编码器编码类别变量。

        通常对于训练集，需要继续提供标签数据；而对于测试集则不需要。
        编码时要求输入的`features_df`的标签数必须与训练时一致。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);
        + label_df(pd.DataFrame): 标签变量一维数据集(标签变量必须为数值类型);

        Returns
        ----
        返回编码后的数据集;若编码器未经训练, 则返回`None`。
        """
        if not self._fitted:
            return None

        df_encoded = self._encoder.transform(features_df, label_df)
        return df_encoded

    @property
    def features(self) -> list:
        """编码器编码的特征变量IDs。
        """
        return self._encoder.get_feature_names()

    def save(self, encoder_file: str):
        """将编码器保存到本地。

        Args
        ----
        + encoder_file(str): 保存文件名(.pkl文件, 完整路径);
        """
        encoder_path = os.path.dirname(encoder_file)
        if not os.path.exists(encoder_path):
            os.makedirs(encoder_path)

        joblib.dump(self._encoder, encoder_file)

    def set_encoder(self, encoder: ce.LeaveOneOutEncoder):
        """直接设置(训练好的)类别编码器。

        Args
        ----
        + encoder(LeaveOneOutEncoder): 训练好的编码器;
        """
        self._encoder = encoder
        self._fitted = True

    @staticmethod
    def load(encoder_file, ID: str):
        """从本地加载到编码器。

        Args
        ----
        + encoder_file(str): 本地编码器文件名(.pkl文件, 完整路径);
        + ID(str): 编码器ID;
        """
        encoder = LooEncoder(ID)
        encoder.set_encoder(joblib.load(encoder_file))
        return encoder


class OrdinalEncoder():
    """采用 OrdinalEncoder 方法实现类别变量的编码。

    该方法属于无监督方法，所以不需要标签数据，但是支持结合标签数据训练。
    该方法支持用户指定类别编码，从而为类别编码提供先验知识。
    该方法支持逆编码, 同时可以适应不断增加的类别。
    """
    def __init__(self, ID: str, features: list = None, mapping: list = None):
        """初始化编码器的基本配置。

        如果指定编码，则需要指定所有`features`中列出的类别变量的自定义编码；同时，
        指定每个类别变量编码时，需要指定数据集中所有类别的编码(未指定的均编码-1)。

        Args
        ----
        + ID(str): 编码器ID;
        + features(list of str): 待编码的类别变量IDs(默认对所有字符型变量编码);
        + mapping(list of dict): 自定义编码([{'col':'col_id', 'mapping':{'v1':1, 'v2:2}}]);
        """
        self._encoder = ce.OrdinalEncoder(cols=features,
                                          mapping=mapping,
                                          return_df=True)
        self._id = ID
        self._mapping = mapping
        self._features = features
        self._fitted = False

    def fit_transform(self,
                      features_df: pd.DataFrame,
                      label_df: pd.DataFrame = None) -> pd.DataFrame:
        """训练编码器，并对指定的类别变量编码。

        训练中采用的`features_df`的向量形状(标签数)将在编码器中固定下来，后续
        编码`transform()`中输入的`features_df`的标签数必须与此一致。

        标签数据'label_df'为可选配置。

        当前接口会重置编码器。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);
        + label_df(pd.DataFrame): 标签变量一维数据集(标签变量必须为数值类型);

        Returns
        ----
        返回类别编码后的数据集。
        """
        # 训练编码器。
        features_df_encoded = self._encoder.fit_transform(features_df, label_df)

        # 记录编码变量。
        self._record_encoded_features(features_df)

        # 记录编码关系。
        self._record_mapping(features_df)

        self._fitted = True
        return features_df_encoded

    def _record_encoded_features(self, features_df):
        """记录实际被编码处理的特征。
        """
        self._features = []
        features_all = self._encoder.get_feature_names()
        for f in features_all:
            if features_df[f].dtype == object:  # 而非str类型
                self._features.append(f)

    def _record_mapping(self, features_df):
        """记录编码关系。
        """
        # 统计类别变量。
        tmp_feat_dic = {}
        for f in self._features:
            categories_f = list(set(features_df[f]))
            tmp_feat_dic[f] = categories_f

        # 统计数据长度。
        size = 0
        for Id, val in tmp_feat_dic.items():
            size = max(size, len(val))

        # 重构数据集。
        for Id, val in tmp_feat_dic.items():
            if len(val) < size:
                dn = size - len(val)
                val += [val[-1] for i in range(dn)]
                tmp_feat_dic[Id] = val
        for Id in self._encoder.get_feature_names():
            if Id not in self._features:
                dic = [0 for i in range(size)]
                tmp_feat_dic[Id] = dic

        # 类型编码和记录。
        self._mapping = []
        res = self._encoder.transform(pd.DataFrame(tmp_feat_dic))
        for Id, categories in tmp_feat_dic.items():
            res_id = res[Id]
            map_id = {None: 0}
            for i in range(len(categories)):
                map_id[categories[i]] = int(res_id[i])  # 为了后期json保存
            dic_id = {}
            dic_id['col'] = Id
            dic_id['mapping'] = map_id
            self._mapping.append(dic_id)

    def fit(self, features_df: pd.DataFrame, label_df: pd.DataFrame = None):
        """训练编码器。

        训练中采用的`features_df`的向量形状(标签数)将在编码器中固定下来，后续
        编码`transform()`中输入的`features_df`的标签数必须与此一致。

        标签数据'label_df'为可选配置。

        当前接口会重置编码器。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);
        + label_df(pd.DataFrame): 标签变量一维数据集(标签变量必须为数值类型);
        """
        # 训练编码器。
        self._encoder.fit(features_df, label_df)

        # 记录编码变量。
        self._record_encoded_features(features_df)

        # 记录编码关系。
        self._record_mapping(features_df)
        self._fitted = True

    def transform(self, features_df: pd.DataFrame) -> pd.DataFrame:
        """通过已经训练好的编码器编码类别变量。

        通常对于训练集，需要继续提供标签数据；而对于测试集则不需要。
        编码时要求输入的`features_df`的标签数必须与训练时一致。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);

        Returns
        ----
        返回编码后的数据集;若编码器未经训练, 则返回`None`。
        """
        if not self._fitted:
            print(f"ERROR: CategoryEncoder({self._id}) is not fitted yet.")
            return None
        if not self._features:
            return features_df

        df_encoded = self._encoder.transform(features_df)
        return df_encoded

    def partial_fit(self, features_df: pd.DataFrame, label_df: pd.DataFrame = None):
        """增量训练编码器。

        训练中采用的`features_df`的向量形状(标签数)将在编码器中固定下来，后续
        编码`transform()`中输入的`features_df`的标签数必须与此一致。

        标签数据'label_df'为可选配置。

        Args
        ----
        + features_df(pd.DataFrame): 待编码类别变量数据集(样本数*标签数);
        + label_df(pd.DataFrame): 标签变量一维数据集(标签变量必须为数值类型);
        """
        # 提取原始映射关系并加载新增类别。
        if self._fitted and self._features:
            for feat in self._features:
                idx = self._search_categories(feat)
                mapping = self._mapping[idx]['mapping']
                categories = mapping.keys()
                max_codes = max(mapping.values())
                for Id in list(set(features_df[feat])):  # 加载新增类别
                    if Id not in categories:
                        max_codes += 1
                        mapping[Id] = max_codes
            self._encoder = ce.OrdinalEncoder(cols=self._features,
                                              mapping=self._mapping,
                                              return_df=True)

        # 编码器训练和记录。
        self._encoder.fit(features_df, label_df)

        if not self._fitted:  # 保存并防止覆盖训练结果
            self._record_encoded_features(features_df)
            self._record_mapping(features_df)
        self._fitted = True

    def _search_categories(self, feature):
        """搜索类别。
        """
        if feature not in self._features:
            return None
        for i in range(len(self._mapping)):
            if self._mapping[i]['col'] == feature:
                return i
        return None

    def inverse_transform(self, encoded_features_df: pd.DataFrame) -> pd.DataFrame:
        """将编码结果逆编码为类别。

        Args
        ----
        + encoded_features_df(pd.DataFrame): 编码后的特征数据集;

        Returns
        ----
        返回逆编码后的数据集;若编码器未经训练, 则返回`None`.
        """
        if not self._fitted:
            print(f"ERROR: CategoryEncoder({self._id}) is not fitted yet.")
        if not self._features:
            return encoded_features_df

        # 逆编码(自定义实现；ce.OrdinalEncoder无法在指定mapping的情况下逆编码)。
        # inversed_features = self._encoder.inverse_transform(encoded_features_df)
        inversed_features = {}
        for feat in encoded_features_df.columns:
            if feat not in self._features:
                inversed_features[feat] = encoded_features_df[feat]
                continue
            feat_map = self._mapping[self._search_categories(feat)]['mapping']
            inversed_map = dict(zip(feat_map.values(), feat_map.keys()))
            inversed_feat = list(
                map(lambda x: inversed_map[x], encoded_features_df[feat]))
            inversed_features[feat] = inversed_feat

        return pd.DataFrame(inversed_features)

    @property
    def features(self) -> list:
        """编码器编码的特征变量IDs。
        """
        return self._features

    def save(self, encoder_file: str, property_file: str):
        """将编码器保存到本地。

        Args
        ----
        + encoder_file(str): 保存编码器文件名(.pkl文件, 完整路径);
        + property_file(str): 保存编码器属性文件名(.json文件, 完整路径);
        """
        # 保存编码器。
        encoder_path = os.path.dirname(encoder_file)
        if not os.path.exists(encoder_path):
            os.makedirs(encoder_path)
        joblib.dump(self._encoder, encoder_file)

        # 保存编码器属性。
        property_path = os.path.dirname(property_file)
        if not os.path.exists(property_path):
            os.makedirs(property_path)
        with open(property_file, 'w', encoding='utf8') as fo:
            json.dump(
                {
                    "mapping": self._mapping,
                    "features": self._features,
                    "fitted": self._fitted
                }, fo)

    def set_encoder(self, encoder: ce.OrdinalEncoder, features: list, mapping: list,
                    fitted: bool):
        """直接设置(训练好的)类别编码器。

        Args
        ----
        + encoder(LeaveOneOutEncoder): 训练好的编码器;
        + features(list of str): 待编码的类别变量IDs(默认对所有字符型变量编码);
        + mapping(list of dict): 自定义编码;
        + fitted(bool): 是否是训练过的编码器;
        """
        self._encoder = encoder
        self._features = features
        self._mapping = mapping
        self._fitted = fitted

    @staticmethod
    def load(ID: str, encoder_file: str, property_file: str):
        """从本地加载到编码器。

        Args
        ----
        + ID(str): 编码器ID;
        + encoder_file(str): 本地编码器文件名(.pkl文件, 完整路径);
        + property_file(str): 保存编码器属性文件名(.json文件, 完整路径);
        """
        with open(property_file, 'r', encoding='utf8') as fi:
            encoder_properties = json.load(fi)
        features = encoder_properties['features']
        mapping = encoder_properties['mapping']
        fitted = encoder_properties['fitted']

        encoder = OrdinalEncoder(ID)
        encoder.set_encoder(joblib.load(encoder_file), features, mapping, fitted)
        return encoder


if __name__ == "__main__":
    data = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5, 6, 7, 8],
        'Sex': ['F', 'M', 'M', 'F', 'M', None, 'F', 'M'],
        'BloodType': ['A', 'AB', 'O', 'B', None, 'O', 'AB', 'B'],
        'Grade': ['High', 'High', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'High'],
        'Education': [
            'PhD', 'HighSchool', 'Bachelor', 'Master', 'HighSchool', 'Master', 'PhD',
            'Bachelor'
        ],
        'Income': [28300, 4500, 7500, 12500, 4200, 15000, 25000, 7200]
    })

    Income_grand_mean = data['Income'].mean()
    data['Income_grand_mean'] = [Income_grand_mean] * len(data)
    Income_group = data.groupby('Education')['Income'].mean().rename(
        'Income_level_mean').reset_index()
    data_new = pd.merge(data, Income_group)

    features = list(data_new.columns)
    features.remove('Income')
    print(data_new)

    # 编码器测试
    features_train = data_new[['Grade']]
    features_test = pd.DataFrame({'Grade': ['High', 'High', 'Medium2', 'Low2']})
    mapping = [{'col': 'Grade', 'mapping': {'High': 1, 'Low': 2, 'Medium': 3}}]
    features = ['Grade']

    encoder = OrdinalEncoder('id1')
    encoder.partial_fit(features_train)
    res = encoder.transform(features_train)
    print(res)
    res = encoder.inverse_transform(res)
    print(res)

    encoder.partial_fit(features_test)

    res = encoder.transform(features_train)
    print(res)
    res = encoder.inverse_transform(res)
    print(res)

    res = encoder.transform(features_test)
    print(res)
    res = encoder.inverse_transform(res)
    print(res)

    encoder_f = "./encoder.pkl"
    property_f = "./encoder.json"
    encoder.save(encoder_f, property_f)

    encoder2 = OrdinalEncoder.load(encoder_f, property_f, 'id2')
    res = encoder2.transform(features_test)
    print(res)
    res = encoder2.inverse_transform(res)
    print(res)
