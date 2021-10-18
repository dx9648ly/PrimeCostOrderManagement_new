# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : EditWidget.py
# @Time  : 2021-07-05  13:58
# @Author: LongYuan
# @FUNC  : 备注修改窗口
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from CODE.mysqlCode_new import ObjectSearch
from UI.EditWidget import Ui_Dialog as uiEditWidget


class EditWidget(QWidget,uiEditWidget):
    def __init__(self,id,string):
        super(EditWidget, self).__init__()
        self.setupUi(self)

        #  设置窗口图标
        # self.setWindowIcon(QIcon("images/EditWidget.png"))

        self.plainTextEdit.setPlainText(string)
        self.id = id
        self.textValue = ''

        self.pushButton_save.clicked.connect(self.pushButton_save_fun)

    ## 提供一个编辑窗口，并把编辑好的值传递回父窗口
    def pushButton_save_fun(self):
        self.textValue = self.plainTextEdit.toPlainText()
        self.write_remarks_sql(self.plainTextEdit.toPlainText())
        self.close()
        # return self.plainTextEdit.toPlainText()

    ## 把修改完成的值写入数据库
    def write_remarks_sql(self,valuestring):
        renew_sql = f"""
                     UPDATE `原价明细总表`
                     SET `备注` = '{valuestring}'
                     WHERE `ID` = '{self.id}'
                     """

        mysql = ObjectSearch()
        # print(f"SQL语句：{renew_sql}")
        mysql.execute_sql(renew_sql)