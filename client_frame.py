
from abc import ABCMeta
from abc import abstractmethod
import tkinter as tk

"""
抽象クラスclient_frame

[メンバ]
無し

[メソッド]
create_widget : 各フレームに必要なパーツを作成する
"""

class client_frame(metaclass=ABCMeta):

    """
    各フレームに必要なパーツを配置する
    """
    @abstractmethod
    def create_widgets(self):
        pass