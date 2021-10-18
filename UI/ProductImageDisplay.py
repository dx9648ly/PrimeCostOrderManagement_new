# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductImageDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/产品图片显示.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_enlarge = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/放大.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_enlarge.setIcon(icon1)
        self.action_enlarge.setObjectName("action_enlarge")
        self.action_shrink = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/缩小.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_shrink.setIcon(icon2)
        self.action_shrink.setObjectName("action_shrink")
        self.action_inversion = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/左旋.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_inversion.setIcon(icon3)
        self.action_inversion.setObjectName("action_inversion")
        self.action_corotation = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/右旋.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_corotation.setIcon(icon4)
        self.action_corotation.setObjectName("action_corotation")
        self.action_exit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon5)
        self.action_exit.setObjectName("action_exit")
        self.toolBar.addAction(self.action_enlarge)
        self.toolBar.addAction(self.action_shrink)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_inversion)
        self.toolBar.addAction(self.action_corotation)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "产品图片展示"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_enlarge.setText(_translate("MainWindow", "放大"))
        self.action_enlarge.setToolTip(_translate("MainWindow", "放大图片"))
        self.action_enlarge.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.action_shrink.setText(_translate("MainWindow", "缩小"))
        self.action_shrink.setToolTip(_translate("MainWindow", "缩小图片"))
        self.action_shrink.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_inversion.setText(_translate("MainWindow", "逆旋"))
        self.action_inversion.setToolTip(_translate("MainWindow", "逆旋"))
        self.action_inversion.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.action_corotation.setText(_translate("MainWindow", "顺旋"))
        self.action_corotation.setToolTip(_translate("MainWindow", "正旋"))
        self.action_corotation.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_exit.setToolTip(_translate("MainWindow", "退出"))
import UI.main_resources_rc
