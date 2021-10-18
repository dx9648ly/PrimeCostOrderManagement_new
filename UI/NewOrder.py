# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1131, 648)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_37 = QtWidgets.QLabel(Form)
        self.label_37.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_36.addWidget(self.label_37)
        self.lineEdit_MonthlyProduction = QtWidgets.QLineEdit(Form)
        self.lineEdit_MonthlyProduction.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_MonthlyProduction.setFont(font)
        self.lineEdit_MonthlyProduction.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_MonthlyProduction.setMaxLength(8)
        self.lineEdit_MonthlyProduction.setClearButtonEnabled(True)
        self.lineEdit_MonthlyProduction.setObjectName("lineEdit_MonthlyProduction")
        self.horizontalLayout_36.addWidget(self.lineEdit_MonthlyProduction)
        self.horizontalLayout_36.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_36, 1, 0, 1, 1)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_26.addWidget(self.label_27)
        self.lineEdit_PackingCost = QtWidgets.QLineEdit(Form)
        self.lineEdit_PackingCost.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_PackingCost.setFont(font)
        self.lineEdit_PackingCost.setObjectName("lineEdit_PackingCost")
        self.horizontalLayout_26.addWidget(self.lineEdit_PackingCost)
        self.horizontalLayout_26.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_26, 2, 2, 1, 1)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_31.addWidget(self.label_32)
        self.lineEdit_FixedFee = QtWidgets.QLineEdit(Form)
        self.lineEdit_FixedFee.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_FixedFee.setFont(font)
        self.lineEdit_FixedFee.setClearButtonEnabled(True)
        self.lineEdit_FixedFee.setObjectName("lineEdit_FixedFee")
        self.horizontalLayout_31.addWidget(self.lineEdit_FixedFee)
        self.horizontalLayout_31.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_31, 1, 1, 1, 1)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_29.addWidget(self.label_30)
        self.comboBox_customer = QtWidgets.QComboBox(Form)
        self.comboBox_customer.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_customer.setFont(font)
        self.comboBox_customer.setObjectName("comboBox_customer")
        self.horizontalLayout_29.addWidget(self.comboBox_customer)
        self.horizontalLayout_29.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_29, 0, 3, 1, 1)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_33.addWidget(self.label_34)
        self.lineEdit_Creator = QtWidgets.QLineEdit(Form)
        self.lineEdit_Creator.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_Creator.setFont(font)
        self.lineEdit_Creator.setClearButtonEnabled(True)
        self.lineEdit_Creator.setObjectName("lineEdit_Creator")
        self.horizontalLayout_33.addWidget(self.lineEdit_Creator)
        self.horizontalLayout_33.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_33, 3, 2, 1, 1)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_35.addWidget(self.label_36)
        self.lineEdit_MaterialCost = QtWidgets.QLineEdit(Form)
        self.lineEdit_MaterialCost.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_MaterialCost.setFont(font)
        self.lineEdit_MaterialCost.setObjectName("lineEdit_MaterialCost")
        self.horizontalLayout_35.addWidget(self.lineEdit_MaterialCost)
        self.horizontalLayout_35.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_35, 2, 0, 1, 1)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_38 = QtWidgets.QLabel(Form)
        self.label_38.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_37.addWidget(self.label_38)
        self.lineEdit_ManagementFee = QtWidgets.QLineEdit(Form)
        self.lineEdit_ManagementFee.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_ManagementFee.setFont(font)
        self.lineEdit_ManagementFee.setClearButtonEnabled(True)
        self.lineEdit_ManagementFee.setObjectName("lineEdit_ManagementFee")
        self.horizontalLayout_37.addWidget(self.lineEdit_ManagementFee)
        self.horizontalLayout_37.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_37, 1, 3, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_22.addWidget(self.label_20)
        self.lineEdit_CarriageFee = QtWidgets.QLineEdit(Form)
        self.lineEdit_CarriageFee.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_CarriageFee.setFont(font)
        self.lineEdit_CarriageFee.setClearButtonEnabled(True)
        self.lineEdit_CarriageFee.setObjectName("lineEdit_CarriageFee")
        self.horizontalLayout_22.addWidget(self.lineEdit_CarriageFee)
        self.horizontalLayout_22.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_22, 1, 2, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_27.addWidget(self.label_28)
        self.lineEdit_TotalCost = QtWidgets.QLineEdit(Form)
        self.lineEdit_TotalCost.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_TotalCost.setFont(font)
        self.lineEdit_TotalCost.setObjectName("lineEdit_TotalCost")
        self.horizontalLayout_27.addWidget(self.lineEdit_TotalCost)
        self.horizontalLayout_27.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_27, 2, 3, 1, 1)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_40 = QtWidgets.QLabel(Form)
        self.label_40.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_39.addWidget(self.label_40)
        self.lineEdit_ProcessCost = QtWidgets.QLineEdit(Form)
        self.lineEdit_ProcessCost.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_ProcessCost.setFont(font)
        self.lineEdit_ProcessCost.setObjectName("lineEdit_ProcessCost")
        self.horizontalLayout_39.addWidget(self.lineEdit_ProcessCost)
        self.horizontalLayout_39.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_39, 2, 1, 1, 1)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_25.addWidget(self.label_25)
        self.dateEdit_CreationDate = QtWidgets.QDateEdit(Form)
        self.dateEdit_CreationDate.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_CreationDate.setFont(font)
        self.dateEdit_CreationDate.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_CreationDate.setObjectName("dateEdit_CreationDate")
        self.horizontalLayout_25.addWidget(self.dateEdit_CreationDate)
        self.horizontalLayout_25.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_25, 3, 1, 1, 1)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_41 = QtWidgets.QLabel(Form)
        self.label_41.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_40.addWidget(self.label_41)
        self.lineEdit_PinFan = QtWidgets.QLineEdit(Form)
        self.lineEdit_PinFan.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_PinFan.setFont(font)
        self.lineEdit_PinFan.setObjectName("lineEdit_PinFan")
        self.horizontalLayout_40.addWidget(self.lineEdit_PinFan)
        self.horizontalLayout_40.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_40, 0, 2, 1, 1)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_30.addWidget(self.label_31)
        self.dateEdit_EffectiveDate = QtWidgets.QDateEdit(Form)
        self.dateEdit_EffectiveDate.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_EffectiveDate.setFont(font)
        self.dateEdit_EffectiveDate.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_EffectiveDate.setDisplayFormat("yyyy/M/d")
        self.dateEdit_EffectiveDate.setObjectName("dateEdit_EffectiveDate")
        self.horizontalLayout_30.addWidget(self.dateEdit_EffectiveDate)
        self.horizontalLayout_30.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_30, 3, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_23.addWidget(self.label_7)
        self.lineEdit_Number = QtWidgets.QLineEdit(Form)
        self.lineEdit_Number.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_Number.setFont(font)
        self.lineEdit_Number.setClearButtonEnabled(True)
        self.lineEdit_Number.setObjectName("lineEdit_Number")
        self.horizontalLayout_23.addWidget(self.lineEdit_Number)
        self.horizontalLayout_23.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_24.addWidget(self.label_24)
        self.lineEdit_Corrector = QtWidgets.QLineEdit(Form)
        self.lineEdit_Corrector.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_Corrector.setFont(font)
        self.lineEdit_Corrector.setClearButtonEnabled(True)
        self.lineEdit_Corrector.setObjectName("lineEdit_Corrector")
        self.horizontalLayout_24.addWidget(self.lineEdit_Corrector)
        self.horizontalLayout_24.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_24, 3, 3, 1, 1)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_28.addWidget(self.label_29)
        self.lineEdit_ProductCode = QtWidgets.QLineEdit(Form)
        self.lineEdit_ProductCode.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_ProductCode.setFont(font)
        self.lineEdit_ProductCode.setClearButtonEnabled(True)
        self.lineEdit_ProductCode.setObjectName("lineEdit_ProductCode")
        self.horizontalLayout_28.addWidget(self.lineEdit_ProductCode)
        self.horizontalLayout_28.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_28, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 0, 0, 1, 1)
        self.textEdit_Remarks = QtWidgets.QTextEdit(Form)
        self.textEdit_Remarks.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_Remarks.setObjectName("textEdit_Remarks")
        self.gridLayout_3.addWidget(self.textEdit_Remarks, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 4, 4, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setToolTip("")
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget_materail = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_materail.setObjectName("tableWidget_materail")
        self.tableWidget_materail.setColumnCount(0)
        self.tableWidget_materail.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_materail, 0, 0, 1, 1)
        self.frame_18 = QtWidgets.QFrame(self.tab)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_10.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 1, 11, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 0, 1, 2, 2)
        spacerItem4 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 1, 9, 1, 1)
        self.pushButton_add1 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_add1.setObjectName("pushButton_add1")
        self.gridLayout_10.addWidget(self.pushButton_add1, 0, 0, 2, 1)
        self.label_35 = QtWidgets.QLabel(self.frame_18)
        self.label_35.setObjectName("label_35")
        self.gridLayout_10.addWidget(self.label_35, 1, 12, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem5, 1, 8, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem6, 1, 7, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 1, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem8, 1, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem9, 1, 6, 1, 1)
        self.lineEdit_MaterialCount = QtWidgets.QLineEdit(self.frame_18)
        self.lineEdit_MaterialCount.setObjectName("lineEdit_MaterialCount")
        self.gridLayout_10.addWidget(self.lineEdit_MaterialCount, 1, 13, 1, 1)
        self.pushButton_delete1 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_delete1.setObjectName("pushButton_delete1")
        self.gridLayout_10.addWidget(self.pushButton_delete1, 1, 10, 1, 1)
        self.gridLayout_4.addWidget(self.frame_18, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_processing = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_processing.setObjectName("tableWidget_processing")
        self.tableWidget_processing.setColumnCount(0)
        self.tableWidget_processing.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget_processing, 0, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.tab_2)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_11.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_39 = QtWidgets.QLabel(self.frame_19)
        self.label_39.setObjectName("label_39")
        self.gridLayout_11.addWidget(self.label_39, 1, 12, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem10, 1, 2, 1, 1)
        self.lineEdit_ProcessCount = QtWidgets.QLineEdit(self.frame_19)
        self.lineEdit_ProcessCount.setObjectName("lineEdit_ProcessCount")
        self.gridLayout_11.addWidget(self.lineEdit_ProcessCount, 1, 13, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem11, 1, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem12, 1, 9, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem13, 1, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem14, 1, 4, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem15, 1, 7, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem16, 0, 1, 2, 2)
        self.pushButton_add2 = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_add2.setObjectName("pushButton_add2")
        self.gridLayout_11.addWidget(self.pushButton_add2, 0, 0, 2, 1)
        spacerItem17 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem17, 1, 5, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem18, 1, 8, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem19, 1, 11, 1, 1)
        self.pushButton_delete2 = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_delete2.setObjectName("pushButton_delete2")
        self.gridLayout_11.addWidget(self.pushButton_delete2, 1, 10, 1, 1)
        self.gridLayout_5.addWidget(self.frame_19, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidget_packing = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_packing.setObjectName("tableWidget_packing")
        self.tableWidget_packing.setColumnCount(0)
        self.tableWidget_packing.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_packing, 0, 0, 1, 1)
        self.frame_20 = QtWidgets.QFrame(self.tab_3)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_12.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem20 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem20, 1, 9, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem21, 1, 5, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem22, 0, 1, 2, 2)
        self.lineEdit_PackingCount = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_PackingCount.setObjectName("lineEdit_PackingCount")
        self.gridLayout_12.addWidget(self.lineEdit_PackingCount, 1, 13, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem23, 1, 8, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem24, 1, 4, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem25, 1, 11, 1, 1)
        self.pushButton_add3 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_add3.setObjectName("pushButton_add3")
        self.gridLayout_12.addWidget(self.pushButton_add3, 0, 0, 2, 1)
        spacerItem26 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem26, 1, 7, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem27, 1, 6, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem28, 1, 2, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.frame_20)
        self.label_42.setObjectName("label_42")
        self.gridLayout_12.addWidget(self.label_42, 1, 12, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem29, 1, 3, 1, 1)
        self.pushButton_delete3 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_delete3.setObjectName("pushButton_delete3")
        self.gridLayout_12.addWidget(self.pushButton_delete3, 1, 10, 1, 1)
        self.gridLayout_8.addWidget(self.frame_20, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_ProductCode, self.lineEdit_PinFan)
        Form.setTabOrder(self.lineEdit_PinFan, self.comboBox_customer)
        Form.setTabOrder(self.comboBox_customer, self.lineEdit_MonthlyProduction)
        Form.setTabOrder(self.lineEdit_MonthlyProduction, self.lineEdit_FixedFee)
        Form.setTabOrder(self.lineEdit_FixedFee, self.lineEdit_CarriageFee)
        Form.setTabOrder(self.lineEdit_CarriageFee, self.lineEdit_ManagementFee)
        Form.setTabOrder(self.lineEdit_ManagementFee, self.dateEdit_EffectiveDate)
        Form.setTabOrder(self.dateEdit_EffectiveDate, self.dateEdit_CreationDate)
        Form.setTabOrder(self.dateEdit_CreationDate, self.lineEdit_Creator)
        Form.setTabOrder(self.lineEdit_Creator, self.lineEdit_Corrector)
        Form.setTabOrder(self.lineEdit_Corrector, self.lineEdit_PackingCost)
        Form.setTabOrder(self.lineEdit_PackingCost, self.textEdit_Remarks)
        Form.setTabOrder(self.textEdit_Remarks, self.lineEdit_MaterialCost)
        Form.setTabOrder(self.lineEdit_MaterialCost, self.tabWidget)
        Form.setTabOrder(self.tabWidget, self.lineEdit_TotalCost)
        Form.setTabOrder(self.lineEdit_TotalCost, self.tableWidget_materail)
        Form.setTabOrder(self.tableWidget_materail, self.pushButton_add1)
        Form.setTabOrder(self.pushButton_add1, self.lineEdit_MaterialCount)
        Form.setTabOrder(self.lineEdit_MaterialCount, self.pushButton_delete1)
        Form.setTabOrder(self.pushButton_delete1, self.tableWidget_processing)
        Form.setTabOrder(self.tableWidget_processing, self.lineEdit_ProcessCount)
        Form.setTabOrder(self.lineEdit_ProcessCount, self.pushButton_add2)
        Form.setTabOrder(self.pushButton_add2, self.pushButton_delete2)
        Form.setTabOrder(self.pushButton_delete2, self.tableWidget_packing)
        Form.setTabOrder(self.tableWidget_packing, self.lineEdit_PackingCount)
        Form.setTabOrder(self.lineEdit_PackingCount, self.pushButton_add3)
        Form.setTabOrder(self.pushButton_add3, self.pushButton_delete3)
        Form.setTabOrder(self.pushButton_delete3, self.lineEdit_Number)
        Form.setTabOrder(self.lineEdit_Number, self.lineEdit_ProcessCost)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新建"))
        self.label_37.setText(_translate("Form", "月 产 量"))
        self.label_27.setText(_translate("Form", "包 装 费"))
        self.label_32.setText(_translate("Form", "固定费用"))
        self.label_30.setText(_translate("Form", "客户名称"))
        self.label_34.setText(_translate("Form", "作    成"))
        self.label_36.setText(_translate("Form", "材 料 费"))
        self.label_38.setText(_translate("Form", "管 理 费"))
        self.label_20.setText(_translate("Form", "运    费"))
        self.label_28.setText(_translate("Form", "总 金 额"))
        self.label_40.setText(_translate("Form", "加 工 费"))
        self.label_25.setText(_translate("Form", "作成日期"))
        self.label_41.setText(_translate("Form", "品    名"))
        self.label_31.setText(_translate("Form", "生效日期"))
        self.label_7.setText(_translate("Form", "序    号"))
        self.label_24.setText(_translate("Form", "整    理"))
        self.label_29.setText(_translate("Form", "成品编码"))
        self.label_33.setText(_translate("Form", " 备注 "))
        self.pushButton_add1.setText(_translate("Form", "增加一行"))
        self.label_35.setText(_translate("Form", "累计金额"))
        self.pushButton_delete1.setText(_translate("Form", "删除一行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "材料费"))
        self.label_39.setText(_translate("Form", "累计金额"))
        self.pushButton_add2.setText(_translate("Form", "增加一行"))
        self.pushButton_delete2.setText(_translate("Form", "删除一行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "加工费"))
        self.pushButton_add3.setText(_translate("Form", "增加一行"))
        self.label_42.setText(_translate("Form", "累计金额"))
        self.pushButton_delete3.setText(_translate("Form", "删除一行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "包装费"))
