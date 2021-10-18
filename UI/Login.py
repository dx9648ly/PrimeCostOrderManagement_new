# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resources/ICO/Login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(0, -10, 101, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/image/resources/Image/logo.png"))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 501, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(190, 220, 100, 30))
        self.btn_login.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_login.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(150, 105, 187, 91))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    border: 0px solid;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_user = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_user.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_user.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_user.setFont(font)
        self.comboBox_user.setObjectName("comboBox_user")
        self.verticalLayout.addWidget(self.comboBox_user)
        self.lineEdit_pw = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pw.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_pw.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_pw.setFont(font)
        self.lineEdit_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pw.setObjectName("lineEdit_pw")
        self.verticalLayout.addWidget(self.lineEdit_pw)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_pw, self.btn_login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label_2.setText(_translate("Form", "永锋原价管理程序"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.comboBox_user.setPlaceholderText(_translate("Form", "账号"))
        self.lineEdit_pw.setPlaceholderText(_translate("Form", "密码"))
import UI.image_resources_rc
import UI.main_resources_rc