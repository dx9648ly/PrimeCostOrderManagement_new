# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 321)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/编辑.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 20, 241, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(130, 270, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "编辑"))
        self.pushButton_save.setText(_translate("Dialog", "确定"))
import UI.main_resources_rc
