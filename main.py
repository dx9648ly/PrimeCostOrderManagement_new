# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : main.py
# @Time  : 2021-07-05  13:32
# @Author: LongYuan
# @FUNC  : 程序的登录界面
import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from CODE.MainWindow import MainWindow
from CODE.mysqlCode_new import ObjectSearch
from UI.Login import Ui_Form as uiLogin

class LoginWindow(QWidget, uiLogin):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        #  对QLineEdit 使用校验器
        # self.lineEdit_user.setMaxLength(16)  # 不超过16位输入
        self.lineEdit_pw.setMaxLength(32)  # 不超过32位输入

        self.initComboBox() # 初始化账号输入下拉框
        self.lineEdit_pw.setFocus() #  设置当前焦点为密码框

        self.btn_login.clicked.connect(self.btnLoginFunction)
        self.comboBox_user.currentIndexChanged.connect(self.lineEdit_pw.setFocus)   # 账号选择完跳到密码输入框
        self.lineEdit_pw.returnPressed.connect(self.btnLoginFunction)  # 密码输入完毕回车登录

    ## 登录按钮
    def btnLoginFunction(self):
        sql = ObjectSearch()
        user_index = self.comboBox_user.currentIndex()  # 账号comboBox的当前序号
        # username = ''   # 账号
        if user_index == 0:
            username = 'admin'
        elif user_index == 1:
            username = 'zc'
        elif user_index == 2:
            username = 'js'
        elif user_index == 3:
            username = 'other'
        # else:
        #     sql.close()
        #     return

        user_value = sql.getFieldValue2(f"`用户表_new`", f"`用户名`='{username}'")
        print(f'数据库记录:{user_value}')
        if user_value == []:
            print(f"账户不存在！")
            QMessageBox.warning(self, '警告', '账号不存在！请重新输入！')
            self.comboBox_user.setCurrentIndex(1)
            self.lineEdit_pw.clear()
            self.comboBox_user.setFocus()
        else:
            if user_value[1] == self.lineEdit_pw.text():
                print(f"登录成功")
                # QMessageBox.information(self,'提示','登录成功！')
                self.lineEdit_pw.clear()
                self.mainWindow = MainWindow(user_value[2])  # 实例化程序主界面窗口
                self.mainWindow.show()
                self.mainWindow.closeSignal.connect(self.showLogin)  # 主程序界面信号连接函数
                self.hide()  # 隐藏登录窗口
            else:
                print("密码错误！")
                QMessageBox.warning(self, '警告', '密码不正确！')
                self.lineEdit_pw.clear()

        sql.close()

    ## 当主程序界面窗口关闭时，登录窗口显示
    def showLogin(self,value):
        if value == 0:
            self.show()
            # self.mainWindow = MainWindow()  # 实例化程序主界面窗口

    ## 初始化账号下拉框
    def initComboBox(self):
        comboBoxItem = ['管理员','资材部','技术部','查询']
        self.comboBox_user.clear()
        self.comboBox_user.addItems(comboBoxItem)
        self.comboBox_user.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())