# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : ProductImageDisplay.py
# @Time  : 2021-07-21  11:50
# @Author: LongYuan
# @FUNC  : 产品图片显示
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QTransform
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication

from UI.ProductImageDisplay import Ui_MainWindow


class ProductImageDisplayWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,imageUrl = None):
        super(ProductImageDisplayWindow, self).__init__()
        self.setupUi(self)

        self.imageLabel = QLabel()  # 定义一个QLabel 来显示图片
        self.imageLabel.setScaledContents(True) # 允许QLabel缩放它的内容充满整个可用的空间
        self.setCentralWidget(self.imageLabel)

        # self.imageUrl = imageUrl   # 把传入的图片地址赋给 self.image

        self.image = QImage()   # 定义QImage
        if self.image.load(imageUrl):   # 如果载入图片，则
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片
            self.resize(self.image.width(), self.image.height())  # 重设大小


    '''图片放大(倍数可设)'''
    @pyqtSlot()
    def on_action_enlarge_triggered(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.scale(2,2)        # PyQt4,PyQt5中已废弃
        transform.scale(1.2, 1.2)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    '''图片缩小(倍数可设)'''
    @pyqtSlot()
    def on_action_shrink_triggered(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.scale(2,2)        # PyQt4,PyQt5中已废弃
        transform.scale(0.8, 0.8)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    '''图片顺旋(角度可设)'''
    @pyqtSlot()
    def on_action_corotation_triggered(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.rotate(90)        # PyQt4,PyQt5中已废弃
        transform.rotate(90)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    '''图片逆旋(角度可设)'''
    @pyqtSlot()
    def on_action_inversion_triggered(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.rotate(90)        # PyQt4,PyQt5中已废弃
        transform.rotate(-90)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    ## 退出
    @pyqtSlot()
    def on_action_exit_triggered(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ProductImageDisplayWindow()
    win.show()
    sys.exit(app.exec())