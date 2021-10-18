# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement_new
# @File  : main.py
# @Time  : 2021-07-17  09:23
# @Author: LongYuan
# @FUNC  :
import socket
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

from UI.mainWindow import Ui_MainWindow
from CODE.NewOrder import NewOrderWindow
from CODE.Query import QueryWindow
from CODE.DataMaintenance import DataMaintenanceWindow


class MainWindow(QMainWindow,Ui_MainWindow):
    closeSignal = pyqtSignal(int)   # 自定义信号，当子窗口关闭时自动发送

    def __init__(self,usertype=None):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        # self.move(0, 0) # 把窗口显示在屏幕左上角

        self.currentWindow = ''
        self.userTypeValue = usertype    # 用户类型
        self.setActionEnable()  #  根据用户类型设置工具栏图标是否可用

        self.addStateBarView()  # 状态栏

    #  定义根据“用户类型”来设置状态栏图标是否可用
    def setActionEnable(self):
        if self.userTypeValue >= 10 and self.userTypeValue < 20:
            print(f"资材部账号")
            self.actFile_Save.setEnabled(False) #  保存
            self.actFile_SaveAsExcl.setEnabled(False)   # 输出
            self.actSet_Sort.setEnabled(False)  #  分类表维护
            self.actQuery_Export.setEnabled(False)  # 导出到文件
        elif self.userTypeValue >= 20 and self.userTypeValue < 30:
            print(f"技术部账号")
            self.actFile_New.setEnabled(False)  #  新建
            self.actFile_Save.setEnabled(False) #  保存
            self.actFile_SaveAsExcl.setEnabled(False)   # 输出
            self.actSet_Pack.setEnabled(False)  # 包装表维护
            self.actSet_Process.setEnabled(False)   # 加工表维护
            self.actSet_Customer.setEnabled(False)  # 客户表维护
            self.actSet_Material.setEnabled(False)  # 材料表维护
            self.actQuery_Export.setEnabled(False)  # 导出到文件
        elif self.userTypeValue >= 30 and self.userTypeValue < 40:
            print(f"品质、生产账号")
            self.actFile_New.setEnabled(False)  #  新建
            self.actFile_Save.setEnabled(False) #  保存
            self.actFile_SaveAsExcl.setEnabled(False)   # 输出
            self.actSet_Process.setEnabled(False)   # 加工表维护
            self.actSet_Customer.setEnabled(False)  # 客户表维护
            self.actSet_Material.setEnabled(False)  # 材料表维护
            self.actSet_Pack.setEnabled(False)  #  包装表维护
            self.actSet_Sort.setEnabled(False)  #  分类表维护
            self.actQuery_Export.setEnabled(False)  # 导出到文件
        else:
            print(f"全功能账号")
            if self.currentWindow == '':
                self.actFile_Save.setEnabled(False)  # 保存
                self.actFile_SaveAsExcl.setEnabled(False)  # 输出
                # self.actQuery_Export.setEnabled(False)  # 导出到文件

    ## 新建
    @pyqtSlot()
    def on_actFile_New_triggered(self):
        self.newOrder = NewOrderWindow()
        self.setCentralWidget(self.newOrder)
        self.newOrder.show()
        self.currentWindow = "NewOrderWindow"

        self.actFile_Save.setEnabled(True)  # 保存
        # self.actFile_SaveAsExcl.setEnabled(True)  # 输出

        #  信号绑定函数
        self.newOrder.signal.connect(self.setSaveFalse) # 【新建】窗口发射的信号，保存完毕后设置保存按钮不可用

    ## 查询
    @pyqtSlot()
    def on_actQuery_triggered(self):
        # print(f"用户名类型：{self.userTypeValue}")
        self.queryWindow = QueryWindow(self.userTypeValue)
        self.setCentralWidget(self.queryWindow)
        self.queryWindow.show()
        self.currentWindow = "QueryWindow"
        if self.userTypeValue < 20:
            self.actQuery_Export.setEnabled(True)  # 导出到文件
        self.queryWindow.signal_count.connect(self.viewStatusBar)   # 信号连接函数

    #  把查询结果数量显示到状态栏
    def viewStatusBar(self,str):
        self.labState.setText(str)

    ## 导出到文件
    @pyqtSlot()
    def on_actQuery_Export_triggered(self):
        if self.currentWindow == "QueryWindow":
            print(f"导出所查询的列表到文件!")
            self.queryWindow.orderListExportToFile()
            # self.actQuery_Export.setEnabled(False)  # 输出后，按钮不可用。防止重复导出
        elif self.currentWindow == "Customer" or self.currentWindow == "Material" or self.currentWindow == "Process" or self.currentWindow == "Packing" or self.currentWindow == "Sort":
            print(f"导出表到文件!")
            self.dataMaintenanceWindow.tableExportToFile()


    ## 保存
    @pyqtSlot()
    def on_actFile_Save_triggered(self):
        if self.currentWindow == "NewOrderWindow":
            print(self.newOrder.lineEdit_Number.text())
            self.newOrder.pushButtonSave()
            self.actFile_SaveAsExcl.setEnabled(True)  # 输出
        else:
            return

    ## 输出
    @pyqtSlot()
    def on_actFile_SaveAsExcl_triggered(self):
        if self.currentWindow == "NewOrderWindow":
            self.newOrder.pushbuttonOutExcel()
        else:
            return

    ## 客户表维护
    @pyqtSlot()
    def on_actSet_Customer_triggered(self):
        self.dataMaintenanceWindow = DataMaintenanceWindow(self.userTypeValue)
        self.setCentralWidget(self.dataMaintenanceWindow)
        self.dataMaintenanceWindow.show()
        self.currentWindow = "Customer"
        self.dataMaintenanceWindow.show_tableView("客户表")
        self.actQuery_Export.setEnabled(True)  # 导出到文件

    ## 材料表维护
    @pyqtSlot()
    def on_actSet_Material_triggered(self):
        self.dataMaintenanceWindow = DataMaintenanceWindow(self.userTypeValue)
        self.setCentralWidget(self.dataMaintenanceWindow)
        self.dataMaintenanceWindow.show()
        self.currentWindow = "Material"
        self.dataMaintenanceWindow.show_tableView("材料表")
        self.actQuery_Export.setEnabled(True)  # 导出到文件

    ## 工序表维护
    @pyqtSlot()
    def on_actSet_Process_triggered(self):
        self.dataMaintenanceWindow = DataMaintenanceWindow(self.userTypeValue)
        self.setCentralWidget(self.dataMaintenanceWindow)
        self.dataMaintenanceWindow.show()
        self.currentWindow = "Process"
        self.dataMaintenanceWindow.show_tableView("工序表")
        self.actQuery_Export.setEnabled(True)  # 导出到文件

    ## 包装表维护
    @pyqtSlot()
    def on_actSet_Pack_triggered(self):
        self.dataMaintenanceWindow = DataMaintenanceWindow(self.userTypeValue)
        self.setCentralWidget(self.dataMaintenanceWindow)
        self.dataMaintenanceWindow.show()
        self.currentWindow = "Packing"
        self.dataMaintenanceWindow.show_tableView("包装表")
        self.actQuery_Export.setEnabled(True)  # 导出到文件

    ## 分类表维护
    @pyqtSlot()
    def on_actSet_Sort_triggered(self):
        self.dataMaintenanceWindow = DataMaintenanceWindow(self.userTypeValue)
        self.setCentralWidget(self.dataMaintenanceWindow)
        self.dataMaintenanceWindow.show()
        self.currentWindow = "Sort"
        # self.dataMaintenanceWindow.show_tableView("分类表")
        self.dataMaintenanceWindow.label.show()   # 隐藏label
        self.dataMaintenanceWindow.comboBox.show()    # 隐藏下拉框
        self.actQuery_Export.setEnabled(True)  # 导出到文件

        ## 退出
    @pyqtSlot()
    def on_actFile_LogOff_triggered(self):
        self.close()
        self.closeSignal.emit(0)

    # 【新建原价单】执行保存后，工具栏的【保存】按钮设置为不可用
    def setSaveFalse(self):
        self.actFile_Save.setEnabled(False)

    #  状态栏
    def addStateBarView(self):
        if self.userTypeValue == 0:
            username = '管理员'
        elif self.userTypeValue >= 10 and self.userTypeValue < 20:
            username = '资材部'
        elif self.userTypeValue >= 20 and self.userTypeValue < 30:
            username = '技术部'
        elif self.userTypeValue >= 30 and self.userTypeValue < 40:
            username = '其他部门'

        self.labLoginState = QLabel()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.labLoginState.setFont(font)    # 设置字体属性
        # self.labLoginState.setAlignment(QtCore.Qt.AlignCenter)  # QtCore.Qt.AlignCenter 居中
        self.labLoginState.setText(f"当前登录账号：{username}")

        self.labState = QLabel()
        self.labState.setFont(font)    # 设置字体属性
        self.labState.setText("")

        self.labLoginIP = QLabel()
        self.labLoginIP.setFont(font)
        self.labLoginIP.setText(f"登录地址：{self.get_host_ip()}")

        # stretch 表示拉伸因子，表示组件在statebar 中占有的空间比例
        self.statusbar.addPermanentWidget(self.labLoginState, stretch=1)
        self.statusbar.addPermanentWidget(self.labState, stretch=3)
        self.statusbar.addPermanentWidget(self.labLoginIP,stretch=1)

    #  获取本机IP
    def get_host_ip(self):
        """
        查询本机IP地址
        :return: IP地址
        """
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect(('114.114.114.114',80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())