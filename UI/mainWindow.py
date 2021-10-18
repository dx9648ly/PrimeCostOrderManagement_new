# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1458, 1016)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/MainWindow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_background_image = QtWidgets.QLabel(self.centralwidget)
        self.label_background_image.setEnabled(True)
        self.label_background_image.setText("")
        self.label_background_image.setPixmap(QtGui.QPixmap(":/image/resources/Image/background1.jpg"))
        self.label_background_image.setScaledContents(True)
        self.label_background_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_background_image.setObjectName("label_background_image")
        self.gridLayout.addWidget(self.label_background_image, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1458, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("selection-background-color: rgb(0, 124, 182);\n"
"selection-color: rgb(0, 170, 127);\n"
"color: rgb(52, 104, 156);")
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_query = QtWidgets.QMenu(self.menubar)
        self.menu_query.setObjectName("menu_query")
        self.menu_set = QtWidgets.QMenu(self.menubar)
        self.menu_set.setObjectName("menu_set")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(0, 30))
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.toolBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBar.setFont(font)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("border-color: rgb(170, 170, 255);\n"
"background-color: rgb(213, 213, 213);")
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actFile_New = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/建单.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_New.setIcon(icon1)
        self.actFile_New.setObjectName("actFile_New")
        self.actQuery_Edit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/查询1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuery_Edit.setIcon(icon2)
        self.actQuery_Edit.setObjectName("actQuery_Edit")
        self.actQuery = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/查询3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuery.setIcon(icon3)
        self.actQuery.setObjectName("actQuery")
        self.actQuery_Update = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/查询2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuery_Update.setIcon(icon4)
        self.actQuery_Update.setObjectName("actQuery_Update")
        self.actSet_Customer = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/客户管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSet_Customer.setIcon(icon5)
        self.actSet_Customer.setObjectName("actSet_Customer")
        self.actSet_Material = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/材料.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSet_Material.setIcon(icon6)
        self.actSet_Material.setObjectName("actSet_Material")
        self.actSet_Process = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/加工.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSet_Process.setIcon(icon7)
        self.actSet_Process.setObjectName("actSet_Process")
        self.actSet_Pack = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/包装.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSet_Pack.setIcon(icon8)
        self.actSet_Pack.setObjectName("actSet_Pack")
        self.actFile_Save = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_Save.setIcon(icon9)
        self.actFile_Save.setObjectName("actFile_Save")
        self.actFile_SaveAsExcl = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/EXCEL.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_SaveAsExcl.setIcon(icon10)
        self.actFile_SaveAsExcl.setObjectName("actFile_SaveAsExcl")
        self.actFile_LogOff = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_LogOff.setIcon(icon11)
        self.actFile_LogOff.setObjectName("actFile_LogOff")
        self.actHelp_About = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/关于.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actHelp_About.setIcon(icon12)
        self.actHelp_About.setObjectName("actHelp_About")
        self.actSet_Sort = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/分类.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSet_Sort.setIcon(icon13)
        self.actSet_Sort.setObjectName("actSet_Sort")
        self.actQuery_Export = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/导出文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuery_Export.setIcon(icon14)
        self.actQuery_Export.setObjectName("actQuery_Export")
        self.menu_file.addAction(self.actFile_New)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actFile_Save)
        self.menu_file.addAction(self.actFile_SaveAsExcl)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actFile_LogOff)
        self.menu_query.addAction(self.actQuery)
        self.menu_query.addAction(self.actQuery_Export)
        self.menu_set.addAction(self.actSet_Customer)
        self.menu_set.addSeparator()
        self.menu_set.addAction(self.actSet_Material)
        self.menu_set.addAction(self.actSet_Process)
        self.menu_set.addAction(self.actSet_Pack)
        self.menu_set.addSeparator()
        self.menu_about.addAction(self.actHelp_About)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_query.menuAction())
        self.menubar.addAction(self.menu_set.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.toolBar.addAction(self.actFile_New)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actFile_Save)
        self.toolBar.addAction(self.actFile_SaveAsExcl)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actQuery)
        self.toolBar.addAction(self.actQuery_Export)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actSet_Customer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actSet_Material)
        self.toolBar.addAction(self.actSet_Process)
        self.toolBar.addAction(self.actSet_Pack)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actSet_Sort)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actFile_LogOff)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "永锋原价管理程序"))
        self.menu_file.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_query.setTitle(_translate("MainWindow", "查询(&Q)"))
        self.menu_set.setTitle(_translate("MainWindow", "设置(&S)"))
        self.menu_about.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actFile_New.setText(_translate("MainWindow", "新建"))
        self.actFile_New.setToolTip(_translate("MainWindow", "新建原价单"))
        self.actFile_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actQuery_Edit.setText(_translate("MainWindow", "查询修改"))
        self.actQuery_Edit.setToolTip(_translate("MainWindow", "查询及可以修改相关数据"))
        self.actQuery_Edit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actQuery.setText(_translate("MainWindow", "查询"))
        self.actQuery.setToolTip(_translate("MainWindow", "仅查询功能"))
        self.actQuery.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actQuery_Update.setText(_translate("MainWindow", "查询上传"))
        self.actQuery_Update.setToolTip(_translate("MainWindow", "查询及可上传文档"))
        self.actQuery_Update.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actSet_Customer.setText(_translate("MainWindow", "客户表维护"))
        self.actSet_Customer.setToolTip(_translate("MainWindow", "数据库客户表维护"))
        self.actSet_Material.setText(_translate("MainWindow", "材料表维护"))
        self.actSet_Material.setToolTip(_translate("MainWindow", "数据库材料表维护"))
        self.actSet_Process.setText(_translate("MainWindow", "加工表维护"))
        self.actSet_Process.setToolTip(_translate("MainWindow", "数据库加工表维护"))
        self.actSet_Pack.setText(_translate("MainWindow", "包装表维护"))
        self.actSet_Pack.setToolTip(_translate("MainWindow", "数据库包装表维护"))
        self.actFile_Save.setText(_translate("MainWindow", "保存"))
        self.actFile_Save.setToolTip(_translate("MainWindow", "保存到数据库"))
        self.actFile_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actFile_SaveAsExcl.setText(_translate("MainWindow", "输出"))
        self.actFile_SaveAsExcl.setToolTip(_translate("MainWindow", "输出为Excel文件"))
        self.actFile_SaveAsExcl.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actFile_LogOff.setText(_translate("MainWindow", "注销"))
        self.actFile_LogOff.setToolTip(_translate("MainWindow", "注销登录并返回登录界面"))
        self.actFile_LogOff.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actHelp_About.setText(_translate("MainWindow", "关于"))
        self.actHelp_About.setToolTip(_translate("MainWindow", "关于"))
        self.actSet_Sort.setText(_translate("MainWindow", "分类表维护"))
        self.actSet_Sort.setToolTip(_translate("MainWindow", "数据库分类表维护_包含多个表"))
        self.actQuery_Export.setText(_translate("MainWindow", "导出到文件"))
        self.actQuery_Export.setToolTip(_translate("MainWindow", "导出查询的原价单数据到文件"))
import UI.image_resources_rc
import UI.main_resources_rc
