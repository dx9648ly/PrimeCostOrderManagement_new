# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : EmptyDelegate.py
# @Time  : 2021-07-05  13:55
# @Author: LongYuan
# @FUNC:    QTableWidget表格指定列不能编辑
from PyQt5 import QtCore
from PyQt5.QtWidgets import QItemDelegate, QWidget


class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        return None

