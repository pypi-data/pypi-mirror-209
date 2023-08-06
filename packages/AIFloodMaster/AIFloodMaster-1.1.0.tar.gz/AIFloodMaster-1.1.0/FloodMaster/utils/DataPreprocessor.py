# -*- encoding: utf-8 -*-
"""
数据集前处理工具。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
import pandas as pd
import numpy as np
import datetime
from typing import Any


class DatasetPreprocessor():
    """数据集前处理工具。
    """
    @staticmethod
    def convert_to_datetime(df: pd.DataFrame,
                            date_col: str,
                            date_fmt: str,
                            is_sort: bool = False,
                            inplace: bool = False) -> pd.DataFrame:
        """将数据集中日期列转为datetime.datetime类型。

        注意, 该方法中没有对NAN等异常值的检查。如果数据转换失败, 会抛出相应异常。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + date_col(str): 数据集中日期列ID;
        + date_fmt(str): 数据集中日期格式;
        + is_sort(bool): 是否按日期列排序数据集;
        + inplace(bool): 是否更改原始数据集;

        Returns
        ----
        时间戳转换后的数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"

        df_new = df if inplace else df.copy()
        if df_new.empty:
            return df_new

        # 提取时间戳。
        def str_to_datetime(date_str):
            return datetime.datetime.strptime(date_str, date_fmt)

        is_converted = True
        if date_col in df_new.columns:
            if np.nan in df_new[date_col]:
                raise IOError("could not convert np.nan to datetime.")
            for date in df_new[date_col]:
                if isinstance(date, datetime.datetime):
                    continue
                if isinstance(date, str):
                    is_converted = False
                else:
                    raise IOError(
                        f"invalid dtype({type(date)}), only convert str to datetime.")

        if not is_converted:
            df_new[date_col] = list(map(str_to_datetime, df_new[date_col]))

        # 按时间戳排序数据集。
        if is_sort:
            df_new.sort_values(by=date_col, inplace=True)
        return df_new

    @staticmethod
    def check_nan(df: pd.DataFrame, inplace: bool = False) -> pd.DataFrame:
        """检查并替换数据集NaN。

        对于数据类型，采用线性插值；对于对象和字符串类型，采用填充插值。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + inplace(bool): 是否更改原始数据集;

        Returns
        ----
        数据检查后的数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"

        df_new = df if inplace else df.copy()
        if df_new.empty:
            return df_new

        # 数值双向线性插值(‘linear’无法处理datetime对象)。
        df_new.interpolate(method='linear', limit_direction='both', inplace=True)

        # 字符串前向插值('pad'无法处理非numeric和datetime类型的索引)。
        df_new.interpolate(method='pad', limit_direction='forward', inplace=True)

        # 再次检查NaN值并采用向后填充。
        df_new.fillna(method='bfill', inplace=True)

        # 最后替换依然存在的NAN值(全列均为NAN)。
        df_new.fillna(value=0, inplace=True)
        return df_new

    @staticmethod
    def check_datetime_continuous(df: pd.DataFrame, date_col: str, date_fmt: str,
                                  time_step: int) -> pd.DataFrame:
        """检查数据集是否为连续时间序列(并去重), 并向后填充缺失值。

        注意, 该方法会将指定的日期列转为datetime.datetime类型并排序。同时, 该方法中
        对起始时间没有规定，所以重整后的时间序列均从数据集中的第一个开始计算。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + date_col(str): 数据集中日期列ID;
        + date_fmt(str): 数据集中日期格式;
        + time_step(int): 数据集重采样时间步长(seconds):

        Returns
        ----
        数据重采样后的数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"

        df_new = df.copy()
        if df_new.empty:
            return df_new

        # 检查日期列(包括数据类型和排序状态)。
        DatasetPreprocessor.convert_to_datetime(df_new, date_col, date_fmt, True, True)

        # 统计数值类型的数据列。
        num_cols = []
        for col in df_new.columns:
            if df_new[col].dtype == int or df_new[col].dtype == float:
                num_cols.append(col)

        # 根据步长，检查时间序列连续性，并采用‘pad’模式填充。
        df_refactor = df_new[0:1]
        pre_line = df_refactor.iloc[0]
        for idx, line in df_new[1:].iterrows():
            cur_df = df_new.loc[[idx]]
            cur_date = line[date_col]
            dt = cur_date - pre_line[date_col]
            steps = int(dt.total_seconds() / time_step)

            curr_date = pre_line[date_col]
            for i in range(steps):  # 数值类型采用线性插值填充，其他类型采用向后填充
                curr_date += datetime.timedelta(seconds=time_step)  # 更新时间戳
                new_df = cur_df.copy()
                new_df[date_col] = curr_date
                alpha = (i + 1) / steps
                for col in num_cols:
                    val = pre_line[col] * (1.0 - alpha) + new_df[col] * alpha
                    new_df[col] = val
                df_refactor = pd.concat([df_refactor[:], new_df], ignore_index=True)
            pre_line = cur_df.iloc[0]  # 更新前一步时间戳

        df_new = df_refactor
        return df_new

    @staticmethod
    def intercept_by_cols(df: pd.DataFrame, index_col: str,
                          index_selected: Any) -> pd.DataFrame:
        """通过列(一般为ID)筛选数据集。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + index_col(str): 数据集列ID;
        + index_selected(Any): 数据列中筛选保留的值;

        Returns
        ----
        数据筛选后的新数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"

        df_new = pd.DataFrame()
        if index_col in df.columns:
            if index_selected:
                df_new = df[(df[index_col] == index_selected)]  # df_new 不再是 df 的视图

        return df_new

    @staticmethod
    def intercept_by_datetime(df: pd.DataFrame,
                              date_col: str,
                              date_fmt: str,
                              start_date: str = None,
                              end_date: str = None) -> pd.DataFrame:
        """根据日期时间筛选数据集。

        注意, 该方法会将指定的日期列转为datetime.datetime类型并排序。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + date_col(str): 数据集中日期列ID;
        + date_fmt(str): 数据集中日期格式;
        + start_date(str): 需要筛选的时间段的起始时间戳(格式须和`date_fmt`一致，下同);
        + end_date(str): 需要筛选的时间段的结束时间戳(不包含);

        Returns
        ----
        数据筛选后的新数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"
        df_new = df.copy()

        # 提取时间戳并排序。
        DatasetPreprocessor.convert_to_datetime(df_new, date_col, date_fmt, True, True)

        # 按时间截取数据集。
        if start_date:
            beg_date = datetime.datetime.strptime(start_date, date_fmt)
            df_new = df_new[(df_new[date_col] >= beg_date)]
        if end_date:
            stop_date = datetime.datetime.strptime(end_date, date_fmt)
            df_new = df_new[(df_new[date_col] < stop_date)]  # 不包含stop_date

        return df_new

    @staticmethod
    def delete_by_cols(df: pd.DataFrame,
                       cols_del: list,
                       inplace: bool = False) -> pd.DataFrame:
        """删除数据集中指定列。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + cols_del(list of str): 待删除的数据列Ids;
        + inplace(bool): 是否更改原始数据集;

        Returns
        ----
        数据筛选后的数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"

        df_new = df if inplace else df.copy()
        if df_new.empty:
            return df_new

        for col in df.columns:
            if col in cols_del:
                del df_new[col]

        return df_new

    @staticmethod
    def check_numeric_cols(df: pd.DataFrame, inplace: bool = False) -> pd.DataFrame:
        """将数据集中所有数值类型的列转为数值类型。

        注意，整数类型和浮点数类型将统一转为浮点数类型。另外, 要求数据集中不存在 NAN等非法数据。

        Args
        ----
        + df(pd.DataFrame): 数据集;
        + inplace(bool): 是否更改原始数据集;

        Returns
        ----
        类型重置后的数据集。
        """
        assert isinstance(df, pd.DataFrame), "requiring a pd.DataFrame as input"

        df_new = df if inplace else df.copy()
        if df_new.empty:
            return df_new

        for col in df_new.columns:
            fst_elem = df_new[col].iloc[0]
            if isinstance(fst_elem, str) and _is_num_in_str(fst_elem):
                df_new[col] = df_new[col].astype(np.float64)
        return df_new


def _is_num_in_str(str_elem):
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


if __name__ == "__main__":
    dic = {
        "a": ['a', 'ab', 'abc', np.nan],
        'b': [np.nan, 12, np.nan, 22],
        'TM': ['2022/1/1', '2022/1/2', '2022/1/4', '2022/1/3']
    }
    df = pd.DataFrame(dic)
    print(id(df))

    DatasetPreprocessor.check_nan(df, True)
    print(id(df))
    res = DatasetPreprocessor.check_datetime_continuous(df, 'TM', "%Y/%m/%d", 3 * 3600)
    print(id(res))
    res = DatasetPreprocessor.intercept_by_cols(res, 'b', 12.0)
    print(id(res))
    res = DatasetPreprocessor.intercept_by_datetime(res, 'TM', '%Y/%m/%d %H:%M:%S',
                                                    '2022/1/1 3:0:0', '2022/1/1 21:0:0')
    print(id(res))
    res = DatasetPreprocessor.delete_by_cols(res, ['a'], True)
    print(df)
    print(id(df))
    print(res)
    print(id(res))
