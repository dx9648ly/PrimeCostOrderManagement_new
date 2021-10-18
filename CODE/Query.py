# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : Query.py
# @Time  : 2021-07-05  13:52
# @Author: LongYuan
# @FUNC  : 查询窗口界面
import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView, QTableView, QCompleter, \
    QApplication

from CODE.OutExcel_new import OrderListExportToFile
from UI.Query import Ui_Form as uiQuery
from CODE.mysqlCode_new import ObjectSearch
from CODE.DataDisplay_new import DataDisplayWindow


class QueryWindow(QWidget, uiQuery):
    #  自定义信号
    signal_count = pyqtSignal(str)

    def __init__(self,usertype=None):
        super(QueryWindow, self).__init__()
        self.setupUi(self)

        self.usertype = usertype

        self.default_widget_show_all_data()  # 设置表格默认显示数据库所有记录

        self.comboBox_Customer.setEditable(True)  # 设置(客户名称)下拉框可以编辑
        self.comboBox_Product.setEditable(True)  # 设置（成品编码）下拉框可以编辑
        self.comboBox_Pinfan.setEditable(True)  # 设置（品番）下拉框可以编辑

        self.init_comboBox()    #  初始化下拉框

        #  信号连接槽函数
        self.tableWidget.doubleClicked.connect(self.tableWidget_doubleClicked)  # 重新定义双击事件
        self.comboBox_Product.currentIndexChanged.connect(self.finishedProductCodeQuery)  # 成品编码下拉框查询
        self.btn_query.clicked.connect(self.search)  # 查询界面中的查询按钮
        self.comboBox_Product._signal.connect(self.keyFunc) # 设置成品编码 按回车键查询

    #  成品编码下拉框 回车按键事件链接函数
    def keyFunc(self):
        query = self.comboBox_Product.currentText()  # 获取下拉框中所选中的值
        select_DB = ObjectSearch()
        items_list = select_DB.get_fpc()  # 获取所有成品编码
        select_DB.close()  # 关闭数据库连接
        if query not in items_list:
            return
        print(f"ComboBox当前选中值：{query}")
        self.DataDisplayWindow = DataDisplayWindow(self.usertype)  # 实例化数据显示窗口
        self.DataDisplayWindow.show()
        self.DataDisplayWindow.query_and_show("成品编码",query)  # 调用数据显示窗口中的方法来显示数据

    #  查询窗口——查询按钮的函数
    def search(self):
        self.tableWidget.clearContents()    #  查询前先清空表格所有内容
        # count_condition = 0  # 查询的条件数量
        condition_list = [] #  查询条件的列表
        # search_str = ""
        #########################################
        #  1、判断 7 个checkBox（客户名称、品名、生效日期、分类、规格、重要性、材质）是否勾选,
        #  如果勾选，则把对应的文本框中内容增加到search_str字符串中
        if self.checkBox_customer.isChecked():
            temp_customer = self.comboBox_Customer.currentText()  # （客户名称）的值
            temp_customer_all = f" 客户名称 = '{temp_customer}' "  # MySql 查询条件字符串
            condition_list.append(temp_customer_all)    # 把查询条件追加到列表中

        if self.checkBox_Pinfan.isChecked():
            temp_product = self.comboBox_Pinfan.currentText()  # （品名）的输入值
            temp_product_all = f"品名 LIKE '%{temp_product}%' "  # MySql 查询条件字符串
            condition_list.append(temp_product_all)  # 把查询条件追加到列表中

        if self.checkBox_tackEffectDate.isChecked():
            temp_date_start = self.dateEdit_start.date().toString(Qt.ISODate)
            temp_date_end = self.dateEdit_end.date().toString(Qt.ISODate)
            temp_tackEffectDate = f"(生效日期 >= '{temp_date_start}' AND 生效日期 <= '{temp_date_end}') "  # MySql 查询条件字符串
            condition_list.append(temp_tackEffectDate)  # 把查询条件追加到列表中

        if self.checkBox_productMix.isChecked():
            temp_productMix = self.comboBox_productMix.currentText()  # （产品结构）的输入值
            temp_productMix_all = f"产品结构 = '{temp_productMix}' "  # MySql 查询条件字符串
            condition_list.append(temp_productMix_all)  # 把查询条件追加到列表中

        if self.checkBox_lenght.isChecked():
            temp_lenght = self.comboBox_lenght.currentText()  # （重要性）的输入值
            temp_lenght_all = f"长度 = '{temp_lenght}' "  # MySql 查询条件字符串
            condition_list.append(temp_lenght_all)  # 把查询条件追加到列表中

        if self.checkBox_ShaftOuterDiameter.isChecked():
            temp_ShaftOuterDiameter = self.comboBox_ShaftOuterDiameter.currentText()  # （规格）的输入值
            temp_ShaftOuterDiameter_all = f"轴芯外径 = '{temp_ShaftOuterDiameter}' "  # MySql 查询条件字符串
            condition_list.append(temp_ShaftOuterDiameter_all)  # 把查询条件追加到列表中

        if self.checkBox_RubberOuterDiameter.isChecked():
            temp_RubberOuterDiameter = self.comboBox_RubberOuterDiameter.currentText()  #  (材质)的输入值
            temp_RubberOuterDiameter_all = f"橡胶外径 = '{temp_RubberOuterDiameter}' "  # MySql 查询条件字符串
            condition_list.append(temp_RubberOuterDiameter_all)  # 把查询条件追加到列表中

        if self.checkBox_commonDifference.isChecked():
            temp_commonDifference = self.comboBox_commonDifference.currentText()  #  (材质)的输入值
            temp_commonDifference_all = f"公差 = '{temp_commonDifference}' "  # MySql 查询条件字符串
            condition_list.append(temp_commonDifference_all)  # 把查询条件追加到列表中

        if self.checkBox_amplitude.isChecked():
            temp_amplitude = self.comboBox_amplitude.currentText()  # (材质)的输入值
            temp_amplitude_all = f"振幅 = '{temp_amplitude}' "  # MySql 查询条件字符串
            condition_list.append(temp_amplitude_all)  # 把查询条件追加到列表中

        if self.checkBox_laserInSpection.isChecked():
            temp_laserInSpection = self.comboBox_laserInSpection.currentText()  # (材质)的输入值
            temp_laserInSpection_all = f"激光 = '{temp_laserInSpection}' "  # MySql 查询条件字符串
            condition_list.append(temp_laserInSpection_all)  # 把查询条件追加到列表中

        if self.checkBox_polish.isChecked():
            temp_polish = self.comboBox_polish.currentText()  # (材质)的输入值
            temp_polish_all = f"研磨 = '{temp_polish}' "  # MySql 查询条件字符串
            condition_list.append(temp_polish_all)  # 把查询条件追加到列表中

        if self.checkBox_pressInMode.isChecked():
            temp_pressInMode = self.comboBox_pressInMode.currentText()  # (材质)的输入值
            temp_pressInMode_all = f"压入方式 = '{temp_pressInMode}' "  # MySql 查询条件字符串
            condition_list.append(temp_pressInMode_all)  # 把查询条件追加到列表中

        if self.checkBox_otherCategories.isChecked():
            temp_otherCategories = self.comboBox_otherCategories.currentText()  # (材质)的输入值
            temp_otherCategories_all = f"其它分类 = '{temp_otherCategories}' "  # MySql 查询条件字符串
            condition_list.append(temp_otherCategories_all)  # 把查询条件追加到列表中


        sql_db = ObjectSearch()
        if len(condition_list) == 0:
            # QMessageBox.warning(self, "警告", "没有选中任何查询条件！")
            # return
            search_str = ''
        elif len(condition_list) == 1:
            search_str = condition_list[0]
            print(f"最终的查询条件：{search_str}")
        else:
            search_str = ' AND '.join(condition_list)
            print(f"最终的查询条件：{search_str}")

        result = sql_db.get_price_new(search_str)
        # print(result)
        print("结果数量为：{}".format(len(result)))
        # self.statusbar.showMessage(f"共{len(result)}条记录", 10000)

        self.signal_count.emit(f"查询结果：{len(result)}条") # 发射信号(结果数量)


        if len(result) <= 0:
            QMessageBox.about(self, "提示", "数据库中不存在相关的记录！请重新输入查询条件！")


        #####################################
        #  2、把查询结果显示到tablewidget表格控件中
        #  2.1 初始化表格
        #  2.1.1 设置表格标题
        pricetitle = sql_db.get_fieldName("`原价明细总表_new`")  # 获取 primeprice 表的标题
        self.tableWidget.setColumnCount(len(pricetitle))  # 设置表格的列数量
        self.tableWidget.setHorizontalHeaderLabels(pricetitle)
        #  2.1.2 显示前先清空表格数据
        self.tableWidget.setRowCount(0)  # 设置表格的行为0
        self.tableWidget.clearContents()  # 清空所有内容
        #  2.2 把结果显示到表格中
        self.tableWidget.setRowCount(len(result))  # 设置表格的行数量为 查询结果的长度
        for x in range(len(result)):
            for y in range(len(result[x])):
                if result[x][y] is None:
                    temp_result = ""
                else:
                    temp_result = format(result[x][y])
                temp_item = QTableWidgetItem(temp_result)
                if y == 26: #  判断第19列（备注）水平不居中，其余水平和垂直都居中
                    temp_item.setTextAlignment(Qt.AlignVCenter)
                else:
                    temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget.setItem(x, y, temp_item)

        #  2.3 把表格进行设置
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中，整行选中
        self.tableWidget.resizeColumnsToContents()  # 设置列宽高按照内容自适应
        self.tableWidget.resizeRowsToContents()  # 设置行宽和高按照内容自适应
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableWidget.setAlternatingRowColors(True)    #  隔行变色


        #  2.4 通过鼠标滚轮定位，快速定位到表格的第1行
        self.tableWidget.verticalScrollBar().setSliderPosition(0)

        #  关闭数据库链接
        sql_db.close()

    #  初始化查询窗口，默认显示前20条数据
    def default_widget_show_all_data(self):
        select_db = ObjectSearch()
        # result = select_db.get_price1()
        result = select_db.get_price1("`ID` < 21")  #  默认只查询前20条记录
        # print(result)
        print("结果数量为：{}".format(len(result)))
        # self.statusbar.showMessage(f"共{len(result)}条记录", 10000)
        if len(result) <= 0:
            QMessageBox.about(self, "提示", "数据库为空！")

        self.signal_count.emit(f"查询结果：{len(result)}条") #  把查询的结果作为信号发送的内容

        #  2、把查询结果显示到tablewidget表格控件中
        #  2.1 初始化表格
        #  2.1.1 设置表格标题
        pricetitle = select_db.get_fieldName("`原价明细总表_new`")  # 获取 primeprice 表的标题
        # print(f"表格的列数量：{len(pricetitle)}")
        self.tableWidget.setColumnCount(len(pricetitle))  # 设置表格的列数量
        self.tableWidget.setHorizontalHeaderLabels(pricetitle)
        #  2.1.2 显示前先清空表格数据
        self.tableWidget.setRowCount(0)  # 设置表格的行为0
        self.tableWidget.clearContents()  # 清空所有内容
        #  2.2 把结果显示到表格中
        self.tableWidget.verticalHeader().setVisible(False)  # 不显示表格的垂直标题，即不显示行号
        self.tableWidget.setRowCount(len(result))  # 设置表格的行数量为 查询结果的长度
        for x in range(len(result)):
            for y in range(len(result[x])):
                if result[x][y] is None:
                    temp_result = ""
                else:
                    temp_result = format(result[x][y])
                temp_item = QTableWidgetItem(temp_result)
                if y == 26: #  判断第19列（备注）水平不居中，其余水平和垂直都居中
                    temp_item.setTextAlignment(Qt.AlignVCenter)
                else:
                    temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget.setItem(x, y, temp_item)

        #  2.3 把表格进行设置
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中，整行选中
        self.tableWidget.resizeColumnsToContents()  # 设置列宽高按照内容自适应
        self.tableWidget.resizeRowsToContents()  # 设置行宽和高按照内容自适应
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableWidget.setAlternatingRowColors(True)    #  隔行变色

        #  关闭数据库链接
        select_db.close()


    #  使用成品编码下拉框查询
    def finishedProductCodeQuery(self):
        query = self.comboBox_Product.currentText()  # 获取下拉框中所选中的值
        select_DB = ObjectSearch()
        items_list = select_DB.get_fpc()  # 获取所有成品编码
        select_DB.close()  # 关闭数据库连接
        if query not in items_list:
            return
        print(f"ComboBox当前选中值：{query}")
        self.DataDisplayWindow = DataDisplayWindow(self.usertype)  # 实例化数据显示窗口
        self.DataDisplayWindow.show()
        self.DataDisplayWindow.query_and_show("成品编码",query)  # 调用数据显示窗口中的方法来显示数据
        # self.setFocus() # 设置焦点在【成品编码】


    #  初始化下拉框
    def init_comboBox(self):
        select_DB = ObjectSearch()
        # 成品编码
        items_list_Product = select_DB.get_fpc()  # 获取所有成品编码
        # self.comboBox_Product.clear()   # 添加前清空下拉框选项列表
        self.comboBox_Product.addItems(items_list_Product)  # 给下拉框添加下拉值
        self.comboBox_Product.setCurrentIndex(-1)  # 把下拉框默认值设值为空
        ## 增加自动补全
        self.completer_Product = QCompleter(items_list_Product)
        self.completer_Product.setFilterMode(Qt.MatchContains)
        self.completer_Product.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_Product.setCompleter(self.completer_Product)

        # 客户名称
        items_list_Customer = select_DB.get_field_value('原价明细总表_new', '客户名称')  # 获取所有的客户名称
        self.comboBox_Customer.clear()   # 添加前清空下拉框选项列表
        self.comboBox_Customer.addItems(items_list_Customer)  # 给下拉框添加下拉值
        self.comboBox_Customer.setCurrentIndex(-1)  # 把下拉框默认值设值为空
        ## 增加自动补全
        self.completer_Customer = QCompleter(items_list_Customer)
        self.completer_Customer.setFilterMode(Qt.MatchContains)
        self.completer_Customer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_Customer.setCompleter(self.completer_Customer)

        # 品名
        items_list_Pinfan = select_DB.get_field_value('原价明细总表_new', '品名')  # 获取所有的品名
        self.comboBox_Pinfan.clear()   # 添加前清空下拉框选项列表
        self.comboBox_Pinfan.addItems(items_list_Pinfan)  # 给下拉框添加下拉值
        self.comboBox_Pinfan.setCurrentIndex(-1)  # 把下拉框默认值设值为空
        ## 增加自动补全
        self.completer_Pinfan = QCompleter(items_list_Pinfan)
        self.completer_Pinfan.setFilterMode(Qt.MatchContains)
        self.completer_Pinfan.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_Pinfan.setCompleter(self.completer_Pinfan)

        # 产品结构
        items_list_productMix = select_DB.get_field_value('产品参数_产品结构表', '名称')  # 获取所有的分类
        self.comboBox_productMix.clear()   # 添加前清空下拉框选项列表
        self.comboBox_productMix.addItems(items_list_productMix)  # 给下拉框添加下拉值

        # 长度
        items_list_lenght = select_DB.get_field_value('产品参数_长度表', '长度值')  # 获取所有的重要性
        self.comboBox_lenght.clear()   # 添加前清空下拉框选项列表
        self.comboBox_lenght.addItems(items_list_lenght)  # 给下拉框添加下拉值

        # 轴芯外径
        items_list_ShaftOuterDiameter = select_DB.get_field_value('产品参数_轴芯外径表', '外径值')  # 获取所有的规格
        self.comboBox_ShaftOuterDiameter.clear()   # 添加前清空下拉框选项列表
        self.comboBox_ShaftOuterDiameter.addItems(items_list_ShaftOuterDiameter)  # 给下拉框添加下拉值

        # 橡胶外径
        items_list_RubberOuterDiameter = select_DB.get_field_value('产品参数_橡胶外径表', '外径值')  # 获取所有的材质
        self.comboBox_RubberOuterDiameter.clear()   # 添加前清空下拉框选项列表
        self.comboBox_RubberOuterDiameter.addItems(items_list_RubberOuterDiameter)  # 给下拉框添加下拉值

        # 公差
        items_list_commonDifference = select_DB.get_field_value('产品参数_公差表', '公差值')  # 获取所有的材质
        self.comboBox_commonDifference.clear()   # 添加前清空下拉框选项列表
        self.comboBox_commonDifference.addItems(items_list_commonDifference)  # 给下拉框添加下拉值

        # 振幅
        items_list_amplitude = select_DB.get_field_value('产品参数_振幅表', '振幅值')  # 获取所有的材质
        self.comboBox_amplitude.clear()   # 添加前清空下拉框选项列表
        self.comboBox_amplitude.addItems(items_list_amplitude)  # 给下拉框添加下拉值

        # 激光
        items_list_laserInSpection = ['是','否']
        self.comboBox_laserInSpection.clear()   # 添加前清空下拉框选项列表
        self.comboBox_laserInSpection.addItems(items_list_laserInSpection)

        # 研磨
        items_list_polish = ['是','否']
        self.comboBox_polish.clear()   # 添加前清空下拉框选项列表
        self.comboBox_polish.addItems(items_list_polish)

        # 压入方式
        items_list_pressInMode = select_DB.get_field_value('产品参数_压入方式表', '压入方式')  # 获取所有的材质
        self.comboBox_pressInMode.clear()   # 添加前清空下拉框选项列表
        self.comboBox_pressInMode.addItems(items_list_pressInMode)  # 给下拉框添加下拉值

        # 其它分类
        items_list_otherCategories = select_DB.get_field_value('产品参数_其它分类表', '分类名称')  # 获取所有的材质
        self.comboBox_otherCategories.clear()   # 添加前清空下拉框选项列表
        self.comboBox_otherCategories.addItems(items_list_otherCategories)  # 给下拉框添加下拉值

        select_DB.close()  # 关闭数据库连接


    #  重新定义双击事件的方法,使用鼠标双击来弹出新窗口进行浏览和数据修改
    def tableWidget_doubleClicked(self):
        curow = self.tableWidget.currentRow()
        current_Row_productCod = self.tableWidget.item(curow, 1).text()
        # print("鼠标点击所在行成品编码是：" + str(current_Row_productCod))
        # print("双击鼠标！")
        self.DataDisplayWindow = DataDisplayWindow(self.usertype)
        self.DataDisplayWindow.show()
        self.DataDisplayWindow.query_and_show("成品编码",current_Row_productCod)
        self.DataDisplayWindow.signal.connect(self.search)  # 显示原价单详细的窗口关闭时，执行一次默认查询


    #  导出查询的原价单——总表信息到excel文件
    def orderListExportToFile(self):
        outFile = OrderListExportToFile()

        query_result_list = []  # 查询结果列表
        sql_db = ObjectSearch()
        price_title = sql_db.get_fieldName("`原价明细总表_new`")  # 获取 原价总表的标题
        query_result_list.append(price_title)

        # 获取 查询的结果 并保存到列表
        max_row = self.tableWidget.rowCount()   # 总行数
        max_column = self.tableWidget.columnCount() # 总列数
        for x in range(max_row):
            temp_list = []
            for y in range(max_column):
                temp_list.append(self.tableWidget.item(x,y).text())
            query_result_list.append(temp_list)

        print(f"查询结果：{len(query_result_list)}")

        outFile.writeExcel(query_result_list)   # 写入EXCEL文件

        QMessageBox.information(self, "完成", f"原价表单已经导出成功！共导出{len(query_result_list)-1}条数据！", QMessageBox.Ok)

        sql_db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QueryWindow()
    win.show()
    sys.exit(app.exec())