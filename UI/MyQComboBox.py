# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : MyQComboBox.py
# @Time  : 2021-07-09  17:03
# @Author: LongYuan
# @FUNC  : 自定义QComboBox 下拉框控件，主要功能为：响应回车键
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QComboBox


class MyQComboBox(QComboBox):
    # 定义信号
    _signal = pyqtSignal()

    def __init__(self):
        super(MyQComboBox, self).__init__()

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(e)

        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return: #  按下回车键 发射信号,Key_Enter是数字键盘上的回车
            self._signal.emit()



