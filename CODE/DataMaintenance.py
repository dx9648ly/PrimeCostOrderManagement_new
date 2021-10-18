# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : DataMaintenance.py
# @Time  : 2021-07-06  08:58
# @Author: LongYuan
# @FUNC  : 基础数据维护界面
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QHeaderView, QMessageBox

from CODE.OutExcel_new import OrderListExportToFile
from CODE.mysqlCode_new import ObjectSearch
from UI.DataMaintenance import Ui_Form as uiDataMaintenance



class DataMaintenanceWindow(QWidget, uiDataMaintenance):
    def __init__(self,usertype=None):
        super(DataMaintenanceWindow, self).__init__()
        self.setupUi(self)

        if usertype == 0:   # 管理员账号
            self.comboBoxItem = ['客户表', '材料表', '工序表', '包装表','产品参数_产品结构表','产品参数_长度表','产品参数_轴芯外径表',
                         '产品参数_橡胶外径表','产品参数_公差表','产品参数_振幅表','产品参数_压入方式表','产品参数_其它分类表']
        elif usertype >= 10 and usertype < 20:  # 资材账号
            self.comboBoxItem = ['客户表', '材料表', '工序表', '包装表']
        elif usertype >= 20 and usertype < 30:    # 技术部账号
            self.comboBoxItem = ['产品参数_产品结构表','产品参数_长度表','产品参数_轴芯外径表','产品参数_橡胶外径表',
                                 '产品参数_公差表','产品参数_振幅表','产品参数_压入方式表','产品参数_其它分类表']
        else:
            self.comboBoxItem = []

        self.initialization_widget()  # 初始化窗口控件

        ## 槽函数与信号的绑定
        self.comboBox.currentIndexChanged.connect(self.show_table)  #“基础数据表”下拉框
        self.pushButton_add.clicked.connect(self.pb_add)    #  "增加一行“按钮
        self.pushButton_del.clicked.connect(self.pb_del)  #  "删除一行”按钮
        self.pushButton_search.clicked.connect(self.pb_search_fun)  #  “搜索”按钮
        self.pushButton_jump.clicked.connect(self.pb_jump)  #  "跳转“按钮
        self.lineEdit_jump.returnPressed.connect(self.pb_jump)  #  定位输入框 回车后 自动滚动条自动跳转到所输入行号
        self.lineEdit_search.returnPressed.connect(self.pb_search_fun)  #  搜索输入框 回车 自动搜索


    #  初始化窗口控件
    def initialization_widget(self):
        '''
        初始化窗口控件
        :return: None
        '''
        ## 初始化【基础数据表】下拉框
        # comboBoxItem1 = ['客户表', '材料表', '工序表', '包装表','产品参数_产品结构表','产品参数_长度表','产品参数_轴芯外径表',
        #                  '产品参数_橡胶外径表','产品参数_公差表','产品参数_振幅表','产品参数_压入方式表','产品参数_其它分类表']
        self.comboBox.clear()
        self.comboBox.addItems(self.comboBoxItem)
        self.comboBox.setCurrentIndex(-1)

        self.label.hide()   # 隐藏label
        self.comboBox.hide()    # 隐藏下拉框

        ## 默认情况下，按钮【搜索、增加一行、删除一行、定位到】、搜索输入框、定位输入框 不可用
        self.pushButton_search.setEnabled(False)
        self.pushButton_add.setEnabled(False)
        self.pushButton_del.setEnabled(False)
        self.lineEdit_search.setEnabled(False)
        self.lineEdit_jump.setEnabled(False)
        self.pushButton_jump.setEnabled(False)

        ##  设置 定位到 输入框只能输入数字
        self.lineEdit_jump.setValidator(QIntValidator(0, 65535))

    #  TableView表格中显示对应数据表内容
    def show_tableView(self,tablename):
        """
        TableView表格中显示对应数据表内容
        :param tablename: 数据库中对应的表名称
        :return:
        """
        #  根据输入的参数设置下拉框的值
        self.comboBox.setCurrentText(tablename)
        #  0 显示内容，按钮【搜索、增加一行、删除一行、定位到】、搜索输入框、定位输入框 可用
        self.pushButton_search.setEnabled(True)
        self.pushButton_add.setEnabled(True)
        self.pushButton_del.setEnabled(True)
        self.lineEdit_search.setEnabled(True)
        self.lineEdit_jump.setEnabled(True)
        self.pushButton_jump.setEnabled(True)

        #  获取表的字段名称
        sql_db = ObjectSearch()
        current_table_field_name = sql_db.get_fieldName(tablename) #  获取当前表的字段名称
        # print(f"当前表【{current_table_name}】所有字段名称：\n\t{current_table_field_name}")

        #  连接数据库
        db = QSqlDatabase.addDatabase('QODBC')  #  使用ODBC方式连接mysql数据库
        db.setDatabaseName('mysql_odbc')    #  系统ODBC中连接名称
        db.open()   #  打开连接

        #  设置tableview表格填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(False)   #  水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #  水平方向，表格大小拓展到适当的尺寸
        # self.tableView.hideColumn(0)    #  隐藏ID列

        #  1、新建QSqlTableModel实例
        self.base_QSqlTableModel = QSqlTableModel()
        self.base_QSqlTableModel.setTable(tablename)   #  设置查询表的名称为下拉框选择的表
        self.base_QSqlTableModel.setEditStrategy(QSqlTableModel.OnFieldChange)  #  设置编辑策略为一改动马上提交数据库
        self.base_QSqlTableModel.select()   #  获取表的所有数据

        #  2、设置表头显示内容为数据库表的字段名称
        for x in range(len(current_table_field_name)):
            self.base_QSqlTableModel.setHeaderData(x,Qt.Horizontal,current_table_field_name[x])

        #  设置下面状态行，显示表的总行数
        while(self.base_QSqlTableModel.canFetchMore()): #  查询更多行，否则只会获取256行
            self.base_QSqlTableModel.fetchMore()
        self.label_state_info.setText(f"【{tablename}】共有【{self.base_QSqlTableModel.rowCount()}】条记录")

        self.tableView.setModel(self.base_QSqlTableModel)   #  设置tableview的数据模型

    #  TableView表格按下拉框显示内容
    def show_table(self, index):
        """
        在tableView表格控件中显示，下拉框选择的表的内容
        :param index: QComboBox下拉框当前序号
        :return:
        """
        # print(f"当前值是：{self.comboBox.itemText(index)}")
        current_table_name = self.comboBox.itemText(index)  # 下拉框当前选择的表名称

        #  0 显示内容，按钮【搜索、增加一行、删除一行、定位到】、搜索输入框、定位输入框 可用
        self.pushButton_search.setEnabled(True)
        self.pushButton_add.setEnabled(True)
        self.pushButton_del.setEnabled(True)
        self.lineEdit_search.setEnabled(True)
        self.lineEdit_jump.setEnabled(True)
        self.pushButton_jump.setEnabled(True)

        #  获取表的字段名称
        sql_db = ObjectSearch()
        current_table_field_name = sql_db.get_fieldName(current_table_name) #  获取当前表的字段名称
        # print(f"当前表【{current_table_name}】所有字段名称：\n\t{current_table_field_name}")

        #  连接数据库
        db = QSqlDatabase.addDatabase('QODBC')  #  使用ODBC方式连接mysql数据库
        db.setDatabaseName('mysql_odbc')    #  系统ODBC中连接名称
        db.open()   #  打开连接

        #  设置tableview表格填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(False)   #  水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #  水平方向，表格大小拓展到适当的尺寸
        # self.tableView.hideColumn(0)    #  隐藏ID列

        #  1、新建QSqlTableModel实例
        self.base_QSqlTableModel = QSqlTableModel()
        self.base_QSqlTableModel.setTable(current_table_name)   #  设置查询表的名称为下拉框选择的表
        self.base_QSqlTableModel.setEditStrategy(QSqlTableModel.OnFieldChange)  #  设置编辑策略为一改动马上提交数据库
        self.base_QSqlTableModel.select()   #  获取表的所有数据

        #  2、设置表头显示内容为数据库表的字段名称
        for x in range(len(current_table_field_name)):
            self.base_QSqlTableModel.setHeaderData(x,Qt.Horizontal,current_table_field_name[x])

        #  设置下面状态行，显示表的总行数
        while(self.base_QSqlTableModel.canFetchMore()): #  查询更多行，否则只会获取256行
            self.base_QSqlTableModel.fetchMore()
        self.label_state_info.setText(f"【{current_table_name}】共有【{self.base_QSqlTableModel.rowCount()}】条记录")

        self.tableView.setModel(self.base_QSqlTableModel)   #  设置tableview的数据模型

    #  增加一行 按钮函数
    def pb_add(self):
        if self.base_QSqlTableModel:
            self.base_QSqlTableModel.insertRows(self.base_QSqlTableModel.rowCount(),1)
            self.tableView.verticalScrollBar().setSliderPosition(self.base_QSqlTableModel.rowCount())

        else:
            return

    #  删除一行 按钮函数
    def pb_del(self):
        if self.base_QSqlTableModel:
            self.base_QSqlTableModel.removeRow(self.tableView.currentIndex().row())
            self.base_QSqlTableModel.select()
        else:
            return

    #  搜索 按钮函数
    def pb_search_fun(self):
        query_string = self.lineEdit_search.text()  # 搜索内容
        # temp_field = ''
        if self.comboBox.currentText() == "客户表":
            temp_field = "客户名称"
        elif self.comboBox.currentText() == "包装表":
            temp_field = "名称"
        elif self.comboBox.currentText() == "材料表":
            temp_field = "名称"
        elif self.comboBox.currentText() == "工序表":
            temp_field = "工序名称"
        elif self.comboBox.currentText() == "产品参数_产品结构表":
            temp_field = "名称"
        elif self.comboBox.currentText() == "产品参数_公差表":
            temp_field = "公差值"
        elif self.comboBox.currentText() == "产品参数_其它分类表":
            temp_field = "分类名称"
        elif self.comboBox.currentText() == "产品参数_橡胶外径表":
            temp_field = "外径值"
        elif self.comboBox.currentText() == "产品参数_压入方式表":
            temp_field = "压入方式"
        elif self.comboBox.currentText() == "产品参数_长度表":
            temp_field = "长度值"
        elif self.comboBox.currentText() == "产品参数_振幅表":
            temp_field = "振幅值"
        elif self.comboBox.currentText() == "产品参数_轴芯外径表":
            temp_field = "外径值"

        if query_string == '':
            self.base_QSqlTableModel.setFilter(f"`{temp_field}` <> ''") # 必须设置查询条件为不等于空，才能查询。原因不清楚???
            self.base_QSqlTableModel.select()
        else:
            self.base_QSqlTableModel.setFilter(f"`{temp_field}` like '%{query_string}%'")
            self.base_QSqlTableModel.select()

        while(self.base_QSqlTableModel.canFetchMore()):
            self.base_QSqlTableModel.fetchMore()
        self.label_state_info.setText(f"当前查询结果共有【{self.base_QSqlTableModel.rowCount()}】条记录")

    #  定位到 按钮函数
    def pb_jump(self):
        if self.lineEdit_jump.text() == '':
            # QMessageBox.warning(self, "警告", "行号不能为空，请重新输入！")
            # return
            current_row = 0
        else:
            current_row = int(self.lineEdit_jump.text()) - 1   #  行号
        # if current_row > self.base_QSqlTableModel.rowCount():
        #     QMessageBox.warning(self, "警告", "输入的行号不能大于最大行号，请重新输入！")

        self.tableView.verticalScrollBar().setSliderPosition(current_row)
        self.tableView.selectRow(current_row)

    #  导出查询的表信息到excel文件
    def tableExportToFile(self):
        outFile = OrderListExportToFile()

        # 获取 查询的结果 并保存到列表
        query_result_list = []
        max_row = self.tableView.model().rowCount()   # 总行数
        max_column = self.tableView.model().columnCount() # 总列数

        # 获取tableview标题
        temp_header_title = []
        for x in range(max_column):
            temp_header_title.append(self.tableView.model().headerData(x,Qt.Horizontal, Qt.DisplayRole))
        query_result_list.append(temp_header_title) # 追加标题

        for x in range(max_row):
            temp_list = []
            for y in range(max_column):
                # 访问qtableview中的表格
                index = self.tableView.model().index(x,y)
                temp_list.append(self.tableView.model().data(index))
            query_result_list.append(temp_list)

        print(f"查询结果：{len(query_result_list)}")

        outFile.writeExcel(query_result_list)   # 写入EXCEL文件

        QMessageBox.information(self, "完成", f"【{self.comboBox.currentText()}】表已经成功导出！共导出{len(query_result_list)-1}条数据！", QMessageBox.Ok)