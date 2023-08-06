# 保存当前目录到系统搜索路径，防止在外部调用包内模块时，包内模块间调用异常。
import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

from LstmPredictor import LstmPredictor