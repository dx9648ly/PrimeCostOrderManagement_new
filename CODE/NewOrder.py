# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : NewOrder.py
# @Time  : 2021-07-06  08:53
# @Author: LongYuan
# @FUNC  : 新建原价订单
import decimal
import winreg

from PyQt5.QtCore import Qt, QDate, pyqtSignal, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QCompleter, QMessageBox, QComboBox, QHeaderView, \
    QAbstractItemView

from CODE.EmptyDelegate import EmptyDelegate
from CODE.OutExcel_new import OutExcel
from CODE.mysqlCode_new import ObjectSearch
from UI.NewOrder import Ui_Form as uiNewOrder

class NewOrderWindow(QWidget, uiNewOrder):
    signal = pyqtSignal()

    def __init__(self):
        super(NewOrderWindow, self).__init__()
        self.setupUi(self)

        #  设置窗口图标
        # self.setWindowIcon(QIcon("images/NewOrder.png"))

        self.initialize()   #  初始化变量及控件
        self.init_form()  # 初始化窗口
        # self.funLinkSignal()  # 将按钮的信号与函数进行链接
        ##----按钮信号与函数绑定
        self.pushButton_add1.clicked.connect(self.add_line_material)  # 材料费表格-增加一行
        self.pushButton_add2.clicked.connect(self.add_line_processing)  # 加工费表格-增加一行
        self.pushButton_add3.clicked.connect(self.add_line_packing)  # 包装费表格-增加一行
        self.pushButton_delete1.clicked.connect(self.delete_line_material)  # 材料费表格——删除一行
        self.pushButton_delete2.clicked.connect(self.delete_line_processing)   # 加工费表格——删除一行
        self.pushButton_delete3.clicked.connect(self.delete_line_packing)   # 包装费表格——删除一行

    ## 初始化变量和控件
    def initialize(self):
        self.initComboBox()  # 初始化QComboBox下拉框

        self.prime_price_list = []  # 保存原价总表数据的列表
        self.prime_price_count = 0  # 总金额
        self.material_cost_list = []  # 保存材料表的数据的列表
        self.materialCount = 0  # 材料总金额
        self.processing_cost_list = []  # 保存加工表的数据的列表
        self.processingCount = 0  # 加工总金额
        self.packing_cost_list = []  # 保存包装表的数据的列表
        self.packingCount = 0  # 包装总金额

        self.setComboBoxCustomer()  #  初始化客户下拉框

    ##----与保存有关的函数-Start----#########################################################
    #  保存按钮的函数
    def pushButtonSave(self):
        material_data = self.collectMaterial()  # 收集材料表的数据
        if material_data == -1:
            QMessageBox.information(self,"提示","材料表格为空，请填写完数据后，再保存！",QMessageBox.Ok)
            return
        elif material_data == -2:
            QMessageBox.information(self,"提示","材料表格数据输入不完整，请输入完整后再保存！",QMessageBox.Ok)
            return

        temp_processing = self.processingFillingSet()  # 计算加工费的金额及填写计算方式
        if temp_processing == -1:
            QMessageBox.information(self,"提示","加工费表格为空，请填写完数据后，再保存！",QMessageBox.Ok)
            return
        elif temp_processing == -2:
            QMessageBox.information(self,"提示","加工表格数据输入不完整，请重新输入",QMessageBox.Ok)
            return
        self.processing_cost_list = self.collectProcessing()  # 收集加工表的数据

        temp_packing = self.packingFillingSet()  # 计算包装费的金额及填写计算方式
        if temp_packing == -1:
            QMessageBox.information(self,"提示","包装费表格为空，请填写完数据后，再保存！",QMessageBox.Ok)
            return
        elif temp_packing == -2:
            QMessageBox.information(self,"提示","包装表格数据输入不完整，请重新输入",QMessageBox.Ok)
            return
        self.packing_cost_list = self.collectPacking()  # 收集包装表的数据

        self.set_count()  # 计算累计金额并填写到相应的文本框

        prime_price = self.collectPrice()  # 收集总表的数据
        if prime_price == "成品编码":
            QMessageBox.information(self,"提示","在数据库中存在相同的【成品编码】 或【成品编码】为空！",QMessageBox.Ok)
            return
        elif prime_price == "客户名称":
            QMessageBox.information(self,"提示","【客户名称】为空！",QMessageBox.Ok)
            return
        elif prime_price == "品名":
            QMessageBox.information(self,"提示","【品名】为空！",QMessageBox.Ok)
            return

        handle_data = self.handleData()  # 数据处理函数
        if handle_data == -1:
            QMessageBox.information(self,"提示","主表数据不完整，请检查后再保存！",QMessageBox.Ok)
            return

        sql_db = ObjectSearch()
        write_result = sql_db.executeInsertIDback("`原价明细总表_new`", tuple(self.prime_price_list))  # 把总价表数据写入数据库
        print(f"总表写入的结果是：{write_result}")
        if write_result is False:
            print(f"总表写入数据库出错，退出！")
            QMessageBox.information(self,"提示","总表写入数据库出错，退出！",QMessageBox.Ok)
            return
        material_cost_list = []
        for x in range(len(self.material_cost_list)):  # 把材料表数据列表中的子列表转换成子元组，后面写入数据库必须是这样的格式
            material_cost_list.append(tuple(self.material_cost_list[x]))
        # material_cost_list = tuple(material_cost_list)  # 列表转换成元组
        # print(f"转换后的材料表：{material_cost_list}")
        mysql_db = ObjectSearch()
        mysql_db.insertItemsMaterial(material_cost_list)

        sql_db = ObjectSearch()
        processing_cost_list = []
        for x in range(len(self.processing_cost_list)):
            processing_cost_list.append(tuple(self.processing_cost_list[x]))
        # print(f"转换后的加工表：{processing_cost_list}")
        sql_db.insertItemsProcessing(processing_cost_list)

        sql_db = ObjectSearch()
        packing_cost_list = []
        for x in range(len(self.packing_cost_list)):
            packing_cost_list.append(tuple(self.packing_cost_list[x]))
        # packing_cost_list = tuple(packing_cost_list)    # 列表转换成元组
        # print(f"转换后的包装表：{packing_cost_list}")
        sql_db.insertItemsPacking(packing_cost_list)

        self.about("数据已经成功写入数据库！")

        self.signal.emit()

        self.setObjectEnable(False) # 保存完毕后，设置窗口控件不可用

    #  处理收集到的数据，使他和数据库的格式一致
    def handleData(self):
        #  处理总表的数据
        if len(self.prime_price_list) != 27:
            print("主表数据不完整，请检查后再保存！")
            return -1
        else:
            self.prime_price_list[18] = self.materialCount  # 把材料总金额放入总表的列表
            self.prime_price_list[19] = self.processingCount  # 把加工总金额放入总表的列表
            self.prime_price_list[20] = self.packingCount  # 把包装总金额放入总表的列表
        print(f"总表的值：{self.prime_price_list}")

        sum = 0
        print(f"总表的值：{self.prime_price_list}\n")
        for x in range(15, 21):
            if self.prime_price_list[x] == '':
                continue
            sum = sum + decimal.Decimal(self.prime_price_list[x]).quantize(decimal.Decimal('0.000'))
        self.lineEdit_TotalCost.setText(str(decimal.Decimal(sum).quantize(decimal.Decimal('0.000'))))
        self.prime_price_list[21] = str(decimal.Decimal(sum).quantize(decimal.Decimal('0.000')))  # 把总金额放入总表的列表

        if self.prime_price_list[14] != '': # 如果月产量不为空，则把数据类型转换成int
            self.prime_price_list[14] = int(self.prime_price_list[14])  # 把月产量转换成int
        else:   # 为空则赋0
            self.prime_price_list[14] = '0'

        print(f"处理后-总表的数据：{self.prime_price_list}")

        ####################
        productCode = self.prime_price_list[1]  # 成品编码
        productName = self.prime_price_list[3]  # 品名
        ####################
        ###材料费###
        if len(self.material_cost_list) < 1:
            self.about("材料表数据为空，请重新输入！")
            self.setObjectEnable(True)  # 保存后，相应的按钮可用
            # self.pushButton_save.setEnabled(True)  # 保存按钮不可用
            # self.pushButton_out.setEnabled(False)  # 保存后，输出EXCEL按钮可用
            return

        for x in range(len(self.material_cost_list)):
            del self.material_cost_list[x][1]  # 删除列表中材料类型字段
            self.material_cost_list[x].insert(1, productCode)  # 把成品编码插入列表中
            self.material_cost_list[x].insert(2, productName)  # 把品名插入列表中
            for y in range(len(self.material_cost_list[x])):  # 把*号替换成空字符
                if self.material_cost_list[x][y] == '*':
                    self.material_cost_list[x][y] = None
        # print(f"处理后-材料表的数据：{self.material_cost_list}")
        ########################
        ###加工费###
        if len(self.processing_cost_list) < 1:
            self.about("加工表数据为空，请重新输入！")
            self.setObjectEnable(True)  # 保存后，相应的按钮可用
            # self.pushButton_save.setEnabled(True)  # 保存按钮不可用
            # self.pushButton_out.setEnabled(False)  # 保存后，输出EXCEL按钮可用
            return

        for x in range(len(self.processing_cost_list)):
            del self.processing_cost_list[x][1]  # 删除列表中工序类型字段
            self.processing_cost_list[x].insert(1, productCode)  # 把成品编码插入列表中
            self.processing_cost_list[x].insert(2, productName)  # 把品名插入列表中
            for y in range(len(self.processing_cost_list[x])):  # 把*号替换成空字符
                if self.processing_cost_list[x][y] == '*':
                    self.processing_cost_list[x][y] = None
        # print(f"第2次处理后-加工表的数据：{self.processing_cost_list}")
        ########################
        ###包装费###
        if len(self.packing_cost_list) < 1:
            self.about("包装表数据为空，请重新输入！")
            self.setObjectEnable(True)  # 保存后，相应的按钮可用
            # self.pushButton_save.setEnabled(True)  # 保存按钮不可用
            # self.pushButton_out.setEnabled(False)  # 保存后，输出EXCEL按钮可用
            return

        for x in range(len(self.packing_cost_list)):
            del self.packing_cost_list[x][1]  # 删除列表中包装类型字段
            self.packing_cost_list[x].insert(1, productCode)  # 把成品编码插入列表中
            self.packing_cost_list[x].insert(2, productName)  # 把品名插入列表中
            for y in range(len(self.packing_cost_list[x])):  # 把*号替换成空字符
                if self.packing_cost_list[x][y] == '*':
                    self.packing_cost_list[x][y] = None
        # print(f"处理后-包装表的数据：{self.packing_cost_list}")

    #  计算表格的累计金额并在填写到总表相应的lineEdit
    def set_count(self):
        #######################################
        #  材料费
        material_count = 0  # 材料费表格的总金额
        for x in range(self.tableWidget_materail.rowCount()):
            material_count = material_count + decimal.Decimal(self.tableWidget_materail.item(x, 10).text()).quantize(
                decimal.Decimal("0.000"))

        #  把金额显示到材料费表格中，累计金额的 LineEdit 中
        temp_str1 = str(decimal.Decimal(material_count).quantize(decimal.Decimal("0.000")))
        self.lineEdit_MaterialCost.setText(temp_str1)
        self.lineEdit_MaterialCount.setText(temp_str1)
        self.materialCount = temp_str1
        ######################################
        #  加工费
        processing_count = 0
        for x in range(self.tableWidget_processing.rowCount()):
            processing_count = processing_count + decimal.Decimal(
                self.tableWidget_processing.item(x, 9).text()).quantize(
                decimal.Decimal("0.000"))

        #  把金额显示到加工费表格中，累计金额的 LineEdit 中
        temp_str2 = str(decimal.Decimal(processing_count).quantize(decimal.Decimal("0.000")))
        self.lineEdit_ProcessCount.setText(temp_str2)
        self.lineEdit_ProcessCost.setText(temp_str2)
        self.processingCount = temp_str2
        ##########################################
        #  包装费
        packing_count = 0
        for x in range(self.tableWidget_packing.rowCount()):
            packing_count = packing_count + decimal.Decimal(self.tableWidget_packing.item(x, 9).text()).quantize(
                decimal.Decimal("0.000"))

        #  把金额显示到包装费表格中，累计金额的 LineEdit 中
        temp_str3 = str(decimal.Decimal(packing_count).quantize(decimal.Decimal("0.000")))
        self.lineEdit_PackingCount.setText(temp_str3)
        self.lineEdit_PackingCost.setText(temp_str3)
        self.packingCount = temp_str3

    #  收集材料表的数据
    def collectMaterial(self):
        rowCount = self.tableWidget_materail.rowCount()
        columnCount = self.tableWidget_materail.columnCount()
        if rowCount == 0:   # 如果表格总行数为0，表明没有输入任何数据，返回-1值，并退出
            return -1

        temp_count = []
        for x in range(rowCount):
            temp_list = []
            for y in range(columnCount):
                if y == 1:
                    try:
                        one_value = self.tableWidget_materail.cellWidget(x, 1).currentText()
                        temp_list.append(f'{one_value}')
                    except AttributeError:
                        print(f"材料表格数据不完整，请填写完整！")
                        temp_count.clear()
                        return -2
                elif y == 2:
                    try:
                        two_value = self.tableWidget_materail.cellWidget(x, 2).currentText()
                        temp_list.append(f'{two_value}')
                    except AttributeError:
                        print(f"材料表格数据不完整，请填写完整！")
                        temp_count.clear()
                        return -2
                else:
                    try:
                        temp_list.append(self.tableWidget_materail.item(x, y).text())
                    except AttributeError:
                        print(f"材料表格数据不完整，请填写完整！")
                        temp_count.clear()
                        return -2
            temp_count.append(temp_list)

        self.material_cost_list.clear() # 清空列表
        self.material_cost_list = temp_count

        # print(f"材料表的所有值：{temp_count}")
        return

    #  收集加工表的数据
    def collectProcessing(self):
        self.processing_cost_list.clear() # 清空列表
        rowCount = self.tableWidget_processing.rowCount()
        columnCount = self.tableWidget_processing.columnCount()
        if rowCount == 0:   # 如果表格总行数为0，表明没有输入任何数据，返回-1值，并退出
            return -1

        temp_count = []
        for x in range(rowCount):
            temp_list = []
            for y in range(columnCount):
                if y == 1:
                    one_value = self.tableWidget_processing.cellWidget(x, 1).currentText()
                    # print(f"第一个下拉框值：{one_value}")
                    temp_list.append(f"{one_value}")
                elif y == 2:
                    two_value = self.tableWidget_processing.cellWidget(x, 2).currentText()
                    # print(f"第二个下拉框值：{two_value}")
                    temp_list.append(f"{two_value}")
                else:
                    temp_list.append(self.tableWidget_processing.item(x, y).text())
            temp_count.append(temp_list)

        # print(f"第1次收集的加工表的所有值：{temp_count}")
        return temp_count

    #  收集包装表的数据
    def collectPacking(self):
        self.packing_cost_list.clear() # 清空列表
        rowCount = self.tableWidget_packing.rowCount()
        columnCount = self.tableWidget_packing.columnCount()
        if rowCount == 0:   # 如果表格总行数为0，表明没有输入任何数据，返回-1值，并退出
            return -1

        temp_count = []
        for x in range(rowCount):
            temp_list = []
            for y in range(columnCount):
                if y == 1:
                    one_value = self.tableWidget_packing.cellWidget(x, 1).currentText()
                    temp_list.append(f'{one_value}')
                elif y == 2:
                    two_value = self.tableWidget_packing.cellWidget(x, 2).currentText()
                    temp_list.append(f'{two_value}')
                else:
                    temp_list.append(self.tableWidget_packing.item(x, y).text())
            temp_count.append(temp_list)

        # print(f"包装表的所有值：{temp_count}")
        return temp_count

    #  收集总表输入的数据
    def collectPrice(self):
        sql_db = ObjectSearch() # 连接数据库
        priceSummary_list = []  # 保存原价总表数据的列表

        priceSummary_list.append(self.lineEdit_Number.text())  # 序号

        temp_product_code = sql_db.get_fpc()  # 获取所有的已经存在的成品编码
        # print(f"数据库中成品编码：{temp1}")
        if self.lineEdit_ProductCode.text() == '':
            print(f"【成品编码】为空！")
            return "成品编码"
        else:
            if self.lineEdit_ProductCode.text() not in temp_product_code:
                priceSummary_list.append(self.lineEdit_ProductCode.text())  # 成品编码
                # print(f"成品编码：【{self.lineEdit_ProductCode.text()}】")
            else:
                print(f"在数据库中存在相同的【成品编码】 ！")
                # self.about("在数据库中存在相同的【成品编码】 ！")
                return "成品编码"

        if self.comboBox_customer.currentIndex() == -1:
            print(f"【客户名称】为空！")
            return "客户名称"
        else:
            priceSummary_list.append(self.comboBox_customer.currentText())  # 客户名称

        if self.lineEdit_PinFan.text() == '':
            print(f"【品名】为空！")
            return "品名"
        else:
            priceSummary_list.append(self.lineEdit_PinFan.text())  # 品名

        #  追加10个空字符串，这个是分类数据，建立原价单时不需要
        priceSummary_list.append('')    #4
        priceSummary_list.append('')    #5
        priceSummary_list.append('')    #6
        priceSummary_list.append('')    #7
        priceSummary_list.append('')    #8
        priceSummary_list.append('')    #9
        priceSummary_list.append('')    #10
        priceSummary_list.append('')    #11
        priceSummary_list.append('')    #12
        priceSummary_list.append('')    #13

        priceSummary_list.append(self.lineEdit_MonthlyProduction.text())  # 月产量
        if self.lineEdit_FixedFee.text() == '':
            priceSummary_list.append(0)
        else:
            priceSummary_list.append(self.lineEdit_FixedFee.text())  # 固定费用
        if self.lineEdit_CarriageFee.text() == '':
            priceSummary_list.append(0)
        else:
            priceSummary_list.append(self.lineEdit_CarriageFee.text())  # 运费
        if self.lineEdit_ManagementFee.text() == '':
            priceSummary_list.append(0)
        else:
            priceSummary_list.append(self.lineEdit_ManagementFee.text())  # 管理费
        priceSummary_list.append('')  #   #  材料总金额——必须要等相关数据项输入后，才能自动计算出来
        priceSummary_list.append('')  #   #  加工总金额——必须要等相关数据项输入后，才能自动计算出来
        priceSummary_list.append('')  #   #  包装总金额——必须要等相关数据项输入后，才能自动计算出来
        priceSummary_list.append('')  #   #  总金额——必须要等相关数据项输入后，才能自动计算出来
        priceSummary_list.append(self.dateEdit_EffectiveDate.date().toString(Qt.ISODate))  # 生效日期
        priceSummary_list.append(self.dateEdit_CreationDate.date().toString(Qt.ISODate))  # 作成日期

        if self.lineEdit_Creator.text() is None:
            priceSummary_list.append('')
        else:
            priceSummary_list.append(self.lineEdit_Creator.text())  # 作成

        if self.lineEdit_Corrector.text() is None:
            priceSummary_list.append('')
        else:
            priceSummary_list.append(self.lineEdit_Corrector.text())  # 整理

        if self.textEdit_Remarks.toPlainText() is None:
            priceSummary_list.append(None)
        else:
            priceSummary_list.append(self.textEdit_Remarks.toPlainText())  # 备注

        # print(f"收集到的——总表的值1：{priceSummary_list}")
        self.prime_price_list = priceSummary_list
        # print(f"收集到的——总表的值2：{self.prime_price_list}")
        # return priceSummary_list

    ######保存-End##############################################################################

    ######输出EXCEL-Start########################################################################
    def pushbuttonOutExcel(self):
        print(f"总表的数据：{self.prime_price_list}")
        for x in range(len(self.prime_price_list)):  # 处理列表中的None，转换成''
            if self.prime_price_list[x] is None:
                self.prime_price_list[x] = ''

        print(f"材料表的数据：{self.material_cost_list}")
        for x in range(len(self.material_cost_list)):  # 处理列表中的None,转换成''
            for y in range(len(self.material_cost_list[x])):
                if self.material_cost_list[x][y] is None:
                    self.material_cost_list[x][y] = ''

        print(f"加工表的数据：{self.processing_cost_list}")
        for x in range(len(self.processing_cost_list)):  # 处理列表中的None,转换成''
            for y in range(len(self.processing_cost_list[x])):
                if self.processing_cost_list[x][y] is None:
                    self.processing_cost_list[x][y] = ''

        print(f"包装表的数据：{self.packing_cost_list}")
        for x in range(len(self.packing_cost_list)):  # 处理列表中的None,转换成''
            for y in range(len(self.packing_cost_list[x])):
                if self.packing_cost_list[x][y] is None:
                    self.packing_cost_list[x][y] = ''

        out_name = f"{self.prime_price_list[1]}.xlsx"
        # print(out_name)
        #  获取桌面的路径
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        temp_str = winreg.QueryValueEx(key, 'Desktop')[0]
        # print(f"桌面路径：{temp_str}")
        # temp_str = os.getcwd()
        file_path_name = f"{temp_str}\{out_name}"
        excel_Object = OutExcel(file_path_name)
        excel_Object.output_excel(file_path_name, self.prime_price_list, self.material_cost_list,
                                  self.processing_cost_list, self.packing_cost_list)
    ######输出Excel-End##########################################################################

    ####材料费表格################################################################################
    # 增加一行-材料费
    def add_line_material(self):
        temp_row_count = self.tableWidget_materail.rowCount()
        if temp_row_count != 0: # 判断数据是否完全填写完成，避免不选择数据，直接多次增加一行
            if self.tableWidget_materail.cellWidget(temp_row_count - 1, 1).currentText() == '' or\
                    self.tableWidget_materail.cellWidget(temp_row_count - 1, 2).currentText() == '':
                QMessageBox.warning(self,"警告","请填写完数据后，再添加一行！")
                return

        select_db = ObjectSearch()
        comboBoxItem0 = select_db.getFieldValue("材料表", "材料类型")  # 获取材料表中，材料类型字段的值（去掉重复）
        select_db.close()
        self.comboBox_Type0.clear()
        self.comboBox_Type0.addItems(comboBoxItem0)  # 把材料类型字段的值做为下拉框的选项添加
        self.comboBox_Type0.setCurrentIndex(-1)

        currentRowCount = self.tableWidget_materail.rowCount()  # 增加行前，表格的总行数
        # print(f"增加行前材料表格的总行数：{currentRowCount}")
        self.tableWidget_materail.insertRow(currentRowCount)  # 增加一行
        latestRowCount = self.tableWidget_materail.rowCount()  # 增加后的总行数
        # print(f"增加一行后材料表格的总行数：{latestRowCount}")

        temp_item0 = QTableWidgetItem(str(latestRowCount))
        temp_item0.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
        self.tableWidget_materail.setItem(latestRowCount - 1, 0, temp_item0)  # 添加序号
        self.tableWidget_materail.setCellWidget(latestRowCount - 1, 1, self.comboBox_Type0)  # 在增加的行的0列添加下拉框

        # print(f"当前最大行：{self.tableWidget_materail.rowCount()}")

        self.comboBox_Type0.activated[str].connect(self.getMaterialNumber)  # 当下拉框选择时，发射信号给 getMaterialNumber方法
        self.initComboBox()  # 初始化QComboBox下拉框控件

    #  槽函数（当第0列的下拉框选择时，发射的信号与此函数链接）
    def getMaterialNumber(self, text):
        select_db = ObjectSearch()
        comboBoxItem1 = select_db.getFieldValue1("材料表", "料号", f" 材料类型 = '{text}'")
        # print(comboBoxItem1)
        self.comboBox_Type1.clear()
        self.comboBox_Type1.addItems(comboBoxItem1)
        self.comboBox_Type1.setCurrentIndex(-1)

        #  设置下拉框自动补全
        self.completer = QCompleter(comboBoxItem1)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_Type1.setCompleter(self.completer)

        latestRowCount = self.tableWidget_materail.rowCount()  # 增加后的总行数
        self.tableWidget_materail.setCellWidget(latestRowCount - 1, 2, self.comboBox_Type1)  # 在增加的行的2列添加下拉框
        self.comboBox_Type1.activated[str].connect(self.fillingTable)

        select_db.close()

    #  槽函数 用下拉框选取的值，查询数据库中的数据并填入表格
    def fillingTable(self, text):
        select_db = ObjectSearch()
        sql_select = f"""
        SELECT `名称`,`供应商`,`单价`,`用量`,`每模用量`,`每模出数`,`切割个数` 
        FROM `材料表`
        WHERE `料号` = '{text}'
        """
        result_sql_select = select_db.search(sql_select)  # 查询的结果
        # print(result_sql_select[0])
        convert_result = []
        for x in range(len(result_sql_select[0])):
            if isinstance(result_sql_select[0][x], decimal.Decimal):
                temp_str = str(decimal.Decimal(result_sql_select[0][x]).quantize(decimal.Decimal('0.000')))
                convert_result.append(temp_str)
            elif isinstance(result_sql_select[0][x], int):
                temp_str1 = str(result_sql_select[0][x])
                convert_result.append(temp_str1)
            elif result_sql_select[0][x] is None:
                convert_result.append("*")  # 把值为None的字段替换成'*'，方便显示
            else:
                convert_result.append(result_sql_select[0][x])

        # print(f"转换后列表值：{convert_result}")

        current_row = self.tableWidget_materail.currentRow()  # 当前所处于表格的的行数

        # table_db_column = [2, 3, 4, 5, 6, 7, 8]  # 表格中需要写入的列
        table_db_column = [3, 4, 5, 6, 7, 8, 9]  # 表格中需要写入的列

        for x in table_db_column:
            item = QTableWidgetItem(convert_result[x - 3])
            # print(result_sql_select[0][x-2])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
            self.tableWidget_materail.setItem(current_row, x, item)  # 写入表格

        # print(f"表格的列娄是：{self.tableWidget_materail.columnCount()}")
        # print(f"表格的行数是：{self.tableWidget_materail.rowCount()}")

        row_value_list = []  # 单元格一行中每列的值,不包括序号
        zero_value = self.tableWidget_materail.cellWidget(current_row, 1).currentText()  # 0列中下拉框的值
        one_value = self.tableWidget_materail.cellWidget(current_row, 2).currentText()  # 1列中下拉框的值

        row_value_list.append(zero_value)
        row_value_list.append(one_value)
        for x in range(len(convert_result)):  # 把2列到8列的值追加到列表
            # if convert_result[x] is None:
            #     row_value_list.append("")
            # else:
            row_value_list.append(convert_result[x])

        if row_value_list[6] == '*':  # 判断没有每模用量、每模出数、切割个数的情况下，计算金额 6是每模用量
            temp_four = decimal.Decimal(row_value_list[4]).quantize(decimal.Decimal('0.000'))  # 把单价的类型转换成decimal
            temp_five = decimal.Decimal(row_value_list[5]).quantize(decimal.Decimal('0.000'))  # 把用量的类型转换成decimal
            #  计算金额，单价 X 用量
            temp_value = str(decimal.Decimal(temp_four * temp_five).quantize(decimal.Decimal('0.000')))

            tempitem = QTableWidgetItem(temp_value)
            tempitem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
            self.tableWidget_materail.setItem(current_row, 10, tempitem)  # 写入表格
            row_value_list.append(str(decimal.Decimal(temp_four * temp_five).quantize(decimal.Decimal('0.000'))))
            # print(temp_value)
        else:
            temp_four = decimal.Decimal(row_value_list[4]).quantize(decimal.Decimal('0.000'))  # 把单价的类型转换成decimal
            temp_five = decimal.Decimal(row_value_list[5]).quantize(decimal.Decimal('0.000'))  # 把用量的类型转换成decimal
            temp_six = decimal.Decimal(row_value_list[6]).quantize(decimal.Decimal('0.000'))  # 把每模用量的类型转换成decimal
            temp_seven = decimal.Decimal(row_value_list[7]).quantize(decimal.Decimal('0.000'))  # 把每模出数的类型转换成decimal
            temp_eight = decimal.Decimal(row_value_list[8]).quantize(decimal.Decimal('0.000'))  # 把切割个数的类型转换成decimal
            #  计算金额，单价 X 用量
            # temp_value = decimal.Decimal(temp_four * temp_five * temp_six / temp_seven / temp_eight).quantize(
            #     decimal.Decimal('0.000'))
            tempitem = QTableWidgetItem(str(
                decimal.Decimal(temp_four * temp_five * temp_six / temp_seven / temp_eight).quantize(
                    decimal.Decimal('0.000'))))
            tempitem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
            self.tableWidget_materail.setItem(current_row, 10, tempitem)  # 写入表格
            row_value_list.append(str(
                decimal.Decimal(temp_four * temp_five * temp_six / temp_seven / temp_eight).quantize(
                    decimal.Decimal('0.000'))))
            # print(temp_value)
        # print(f"材料表第{current_row}行的值为：{row_value_list}")

        select_db.close()

    #  删除一行-材料费
    def delete_line_material(self):
        if len(self.tableWidget_materail.selectedItems()) == 0:
            QMessageBox.about(self,'提示',"没有选中任何行！")
            print(f'没有选中任何行！')
            return
        else:
            print(f'当前选中是第【{self.tableWidget_materail.selectedItems()[0].row()}】行！')

            current_select_line = self.tableWidget_materail.selectedItems()[0].row()

            print(f'删除前共有【{self.tableWidget_materail.rowCount()}】行！')
            self.tableWidget_materail.removeRow(current_select_line)
            print(f'删除【后】共有【{self.tableWidget_materail.rowCount()}】行！')

        ##  删除后序号会出现错误，重新把表格中的序号做处理
        for x in range(self.tableWidget_materail.rowCount()):
            temp_item  = QTableWidgetItem(str(x+1))
            temp_item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tableWidget_materail.setItem(x,0,temp_item)


    ####加工费####################################################################################
    #  增加一行-加工费
    def add_line_processing(self):
        temp_row_count = self.tableWidget_processing.rowCount()
        if temp_row_count != 0: # 判断数据是否完全填写完成，避免不选择数据，直接多次增加一行
            if self.tableWidget_processing.cellWidget(temp_row_count - 1, 1).currentText() == '' or\
                    self.tableWidget_processing.cellWidget(temp_row_count - 1, 2).currentText() == '':
                QMessageBox.warning(self,"警告","请填写完数据后，再添加一行！")
                return

        select_db = ObjectSearch()
        comboBoxItem2 = select_db.getFieldValue("工序表", "工序类型")  # 获取工序表中，工序类型字段的值（去掉重复）
        # print(f"工序类型的值：{comboBoxItem2}")
        select_db.close()
        self.comboBox_Type2.clear()
        self.comboBox_Type2.addItems(comboBoxItem2)  # 把加工工序类型字段的值做为下拉框的选项添加
        self.comboBox_Type2.setCurrentIndex(-1)
        rowCount = self.tableWidget_processing.rowCount()  # 增加行前，表格的总行数
        self.tableWidget_processing.insertRow(rowCount)  # 增加一行
        latestRowCount = self.tableWidget_processing.rowCount()  # 增加后的总行数
        temp_item0 = QTableWidgetItem(chr(latestRowCount + 96))
        temp_item0.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
        self.tableWidget_processing.setItem(latestRowCount - 1, 0, temp_item0)  # 添加序号
        self.tableWidget_processing.setCellWidget(latestRowCount - 1, 1, self.comboBox_Type2)  # 在增加的行的0列添加下拉框

        self.comboBox_Type2.activated[str].connect(self.getProcessingNumber)  # 当下拉框选择时，发射信号给 getMaterialNumber方法
        self.initComboBox()  # 初始化QComboBox下拉框控件

    #  槽函数（当第1列的下拉框选择时，发射的信号与此函数链接）
    def getProcessingNumber(self, text):
        select_db = ObjectSearch()
        comboBoxItem3 = select_db.getFieldValue1("工序表", "工序名称", f" 工序类型 = '{text}'")
        select_db.close()
        # print(comboBoxItem1)
        self.comboBox_Type3.clear()
        self.comboBox_Type3.addItems(comboBoxItem3)
        self.comboBox_Type3.setCurrentIndex(-1)

        #  设置下拉框自动补全
        self.completer = QCompleter(comboBoxItem3)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_Type3.setCompleter(self.completer)

        latestRowCount = self.tableWidget_processing.rowCount()  # 增加后的总行数
        self.tableWidget_processing.setCellWidget(latestRowCount - 1, 2, self.comboBox_Type3)  # 在增加的行的0列添加下拉框
        self.comboBox_Type3.activated[str].connect(self.fillingTableProcessing)

    #  槽函数fillingTableProcessing,连接0列的下拉框 activated信号.用下拉框选取的值，查询数据库中的数据并填入表格
    def fillingTableProcessing(self, text):
        select_db = ObjectSearch()
        sql_select = f"""SELECT `工序代码`,`工程单价`,`工数`
        FROM `工序表`
        WHERE `工序名称` = '{text}'
        """
        result_sql_select = select_db.search(sql_select)  # 查询的结果
        select_db.close()
        # print(f"查询的结果：{result_sql_select[0]}")
        convert_result = []
        for x in range(len(result_sql_select[0])):
            if isinstance(result_sql_select[0][x], decimal.Decimal):
                temp_str = str(decimal.Decimal(result_sql_select[0][x]).quantize(decimal.Decimal('0.000')))
                convert_result.append(temp_str)
            elif isinstance(result_sql_select[0][x], int):
                temp_str1 = str(result_sql_select[0][x])
                convert_result.append(temp_str1)
            elif result_sql_select[0][x] is None:
                convert_result.append("*")  # 把值为None的字段替换成'*'，方便显示
            else:
                convert_result.append(result_sql_select[0][x])

        # print(f"转换后列表值：{convert_result}")

        current_row = self.tableWidget_processing.currentRow()  # 当前所处于表格的的行数

        # table_db_column = [3, 4, 5]  # 表格中需要写入的列

        for x in range(len(convert_result)):  # 循环写入表格
            item = QTableWidgetItem(convert_result[x])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
            self.tableWidget_processing.setItem(current_row, x + 3, item)  # 写入表格

        #  因为，数据库不包含切割数、用量两个数据，所以这两列暂时使用'*'代替
        temp_item = QTableWidgetItem('*')  # 一个实例只能使用一次
        temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
        self.tableWidget_processing.setItem(current_row, 6, temp_item)  # 第7列，切割数
        temp_item1 = QTableWidgetItem('*')
        temp_item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
        self.tableWidget_processing.setItem(current_row, 7, temp_item1)  # 第8列，用量

    #  计算加工费的金额及填写计算方式
    def processingFillingSet(self):
        #  1、确定加工费表格的总行数、总列数
        rowCount = self.tableWidget_processing.rowCount()  # 表格的总行数
        columnCount = self.tableWidget_processing.columnCount()  # 表格的总列数
        if rowCount == 0:   # 如果表格总行数为0，表明没有输入任何数据，返回-1值，并退出
            return -1
        #  2、循环读取表格的值、并填写 计算方式的单元格7
        processing_list = []  # 保存整个表格的值
        for x in range(rowCount):
            temp_list = []  # 临时存储表格每行的值
            for y in range(3, columnCount - 2):  # 最后两列不读取，一个是计算方式，一个是金额
                try:
                    temp_list.append(self.tableWidget_processing.item(x, y).text())
                except AttributeError:
                    print(f"加工表格数据输入不完整，请重新输入")
                    processing_list.clear()
                    return -2
            processing_list.append(temp_list)
        # print(f"整个表格的值：{processing_list}")

        #  3、根据表格的值填写 计算方式与金额
        for x in range(rowCount):
            if processing_list[x][3] == '*':
                temp_item = QTableWidgetItem(f"{processing_list[x][1]}/{processing_list[x][2]}")  # 计算方式
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_processing.setItem(x, 8, temp_item)  # 填写计算方式单元格
                temp_1 = decimal.Decimal(processing_list[x][1]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_2 = decimal.Decimal(processing_list[x][2]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_8 = str(decimal.Decimal(temp_1 / temp_2).quantize(decimal.Decimal('0.000')))  # 计算单行金额
                temp_item1 = QTableWidgetItem(temp_8)
                temp_item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_processing.setItem(x, 9, temp_item1)  # 填写计算方式单元格

            else:
                temp_str = f"{processing_list[x][1]}/{processing_list[x][2]}/{processing_list[x][3]}X{processing_list[x][4]}"  # 计算方式
                temp_item = QTableWidgetItem(temp_str)  # 计算方式
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_processing.setItem(x, 8, temp_item)  # 填写计算方式单元格
                temp_1 = decimal.Decimal(processing_list[x][1]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_2 = decimal.Decimal(processing_list[x][2]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_3 = decimal.Decimal(processing_list[x][3]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_4 = decimal.Decimal(processing_list[x][4]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_8 = str(
                    decimal.Decimal(temp_1 / temp_2 / temp_3 * temp_4).quantize(decimal.Decimal('0.000')))  # 计算单行金额
                temp_item2 = QTableWidgetItem(temp_8)
                temp_item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_processing.setItem(x, 9, temp_item2)  # 填写计算方式单元格

    #  删除一行-加工费
    def delete_line_processing(self):
        if len(self.tableWidget_processing.selectedItems()) == 0:
            QMessageBox.about(self,'提示',"没有选中任何行！")
            print(f'没有选中任何行！')
            return
        else:
            # print(f'当前选中是第【{self.tableWidget_processing.selectedItems()[0].row()}】行！')

            current_select_line = self.tableWidget_processing.selectedItems()[0].row()

            # print(f'删除前共有【{self.tableWidget_processing.rowCount()}】行！')
            self.tableWidget_processing.removeRow(current_select_line)
            # print(f'删除【后】共有【{self.tableWidget_processing.rowCount()}】行！')

        ##  删除后序号会出现错误，重新把表格中的序号做处理
        for x in range(self.tableWidget_processing.rowCount()):
            temp_item  = QTableWidgetItem(chr(x + 97))
            temp_item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tableWidget_processing.setItem(x,0,temp_item)

    ####包装费####################################################################################
    #  增加一行-包装费
    def add_line_packing(self):
        temp_row_count = self.tableWidget_packing.rowCount()
        if temp_row_count != 0:  # 判断数据是否完全填写完成，避免不选择数据，直接多次增加一行
            if self.tableWidget_packing.cellWidget(temp_row_count - 1, 1).currentText() == '' or \
                    self.tableWidget_packing.cellWidget(temp_row_count - 1, 2).currentText() == '':
                QMessageBox.warning(self, "警告", "请填写完数据后，再添加一行！")
                return

        select_db = ObjectSearch()
        comboBoxItem3 = select_db.getFieldValue("包装表", "材料类型")  # 获取包装表中，材料类型字段的值（去掉重复）
        # print(f"工序类型的值：{comboBoxItem2}")
        select_db.close()
        self.comboBox_Type4.clear()
        self.comboBox_Type4.addItems(comboBoxItem3)  # 把加工工序类型字段的值做为下拉框的选项添加
        self.comboBox_Type4.setCurrentIndex(-1)
        rowCount = self.tableWidget_packing.rowCount()  # 增加行前，表格的总行数
        self.tableWidget_packing.insertRow(rowCount)  # 增加一行
        latestRowCount = self.tableWidget_packing.rowCount()  # 增加后的总行数

        temp_item0 = QTableWidgetItem(chr(latestRowCount + 64))
        temp_item0.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
        self.tableWidget_packing.setItem(latestRowCount - 1, 0, temp_item0)  # 添加序号

        self.tableWidget_packing.setCellWidget(latestRowCount - 1, 1, self.comboBox_Type4)  # 在增加的行的1列添加下拉框

        self.comboBox_Type4.activated[str].connect(self.getPackingNumber)  # 当下拉框选择时，发射信号给 getPackingNumber方法
        self.initComboBox()  # 初始化QComboBox下拉框控件

    #  槽函数，与增加一行按钮连接
    def getPackingNumber(self, text):
        select_db = ObjectSearch()
        comboBoxItem3 = select_db.getFieldValue1("包装表", "包材编码", f" 材料类型 = '{text}'")
        self.comboBox_Type5.clear()
        self.comboBox_Type5.addItems(comboBoxItem3)
        self.comboBox_Type5.setCurrentIndex(-1)

        #  设置下拉框自动补全
        self.completer = QCompleter(comboBoxItem3)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_Type5.setCompleter(self.completer)

        latestRowCount = self.tableWidget_packing.rowCount()  # 增加后的总行数
        self.tableWidget_packing.setCellWidget(latestRowCount - 1, 2, self.comboBox_Type5)  # 在增加的行的0列添加下拉框
        self.comboBox_Type5.activated[str].connect(self.fillingTablePacking)

        select_db.close()

    #  槽函数getPackingNumber(),连接0列的下拉框 activated信号.用下拉框选取的值，查询数据库中的数据并填入表格
    def fillingTablePacking(self, text):
        select_db = ObjectSearch()
        sql_select = f"""SELECT `名称`,`单价`,`用量`,`包装数量`,`回收次数`
        FROM `包装表`
        WHERE `包材编码` = '{text}'
        """
        result_sql_select = select_db.search(sql_select)  # 查询的结果
        # print(f"查询的结果：{result_sql_select[0]}")
        convert_result = []
        for x in range(len(result_sql_select[0])):
            if isinstance(result_sql_select[0][x], decimal.Decimal):
                temp_str = str(decimal.Decimal(result_sql_select[0][x]).quantize(decimal.Decimal('0.000')))
                convert_result.append(temp_str)
            elif isinstance(result_sql_select[0][x], int):
                temp_str1 = str(result_sql_select[0][x])
                convert_result.append(temp_str1)
            elif result_sql_select[0][x] is None:
                convert_result.append("*")  # 把值为None的字段替换成'*'，方便显示
            else:
                convert_result.append(result_sql_select[0][x])

        # print(f"转换后列表值：{convert_result}")

        current_row = self.tableWidget_packing.currentRow()  # 当前所处于表格的的行数

        table_db_column = [3, 4, 5, 6, 7]  # 表格中需要写入的列

        for x in table_db_column:  # 循环写入表格
            item = QTableWidgetItem(convert_result[x - 3])
            # print(result_sql_select[0][x-2])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
            self.tableWidget_packing.setItem(current_row, x, item)  # 写入表格

        select_db.close()

    #  计算包装费的金额及填写计算方式
    def packingFillingSet(self):
        #  1、确定加工费表格的总行数、总列数
        rowCount = self.tableWidget_packing.rowCount()  # 表格的总行数
        columnCount = self.tableWidget_packing.columnCount()  # 表格的总列数
        if rowCount == 0:   # 如果表格总行数为0，表明没有输入任何数据，返回-1值，并退出
            return -1
        #  2、循环读取表格的值、并填写 计算方式的单元格7
        packking_list = []  # 保存整个表格的值
        for x in range(rowCount):
            temp_list = []  # 临时存储表格每行的值
            for y in range(3, columnCount - 2):  # 最后两列不读取，一个是计算方式，一个是金额
                try:
                    temp_list.append(self.tableWidget_packing.item(x, y).text())
                    packking_list.append(temp_list)
                except AttributeError:
                    print(f"包装表格数据输入不完整，请重新输入")
                    packking_list.clear()
                    return -2
        # print(f"整个表格的值：{processing_list}")

        #  3、根据表格的值填写 计算方式与金额
        for x in range(rowCount):
            if packking_list[x][4] == '*':
                temp_item = QTableWidgetItem(
                    f"{packking_list[x][1]}X{packking_list[x][2]}/{packking_list[x][3]}")  # 计算方式
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_packing.setItem(x, 8, temp_item)  # 填写计算方式单元格
                temp_1 = decimal.Decimal(packking_list[x][1]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_2 = decimal.Decimal(packking_list[x][2]).quantize(decimal.Decimal('0.000'))  # 把用量转换成decimal类型
                temp_3 = decimal.Decimal(packking_list[x][3]).quantize(decimal.Decimal('0.000'))  # 把包装数转换成decimal类型
                temp_8 = str(decimal.Decimal(temp_1 * temp_2 / temp_3).quantize(decimal.Decimal('0.000')))  # 计算单行金额
                temp_item1 = QTableWidgetItem(temp_8)
                temp_item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_packing.setItem(x, 9, temp_item1)  # 填写计算方式单元格

            else:
                temp_str = f"{packking_list[x][1]}X{packking_list[x][2]}/{packking_list[x][3]}/{packking_list[x][4]}"  # 计算方式
                temp_item = QTableWidgetItem(temp_str)  # 计算方式
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_packing.setItem(x, 8, temp_item)  # 填写计算方式单元格
                temp_1 = decimal.Decimal(packking_list[x][1]).quantize(decimal.Decimal('0.000'))  # 把单价转换成decimal类型
                temp_2 = decimal.Decimal(packking_list[x][2]).quantize(decimal.Decimal('0.000'))  # 把用量转换成decimal类型
                temp_3 = decimal.Decimal(packking_list[x][3]).quantize(decimal.Decimal('0.000'))  # 把包装数转换成decimal类型
                temp_4 = decimal.Decimal(packking_list[x][4]).quantize(decimal.Decimal('0.000'))  # 把回收转换成decimal类型
                temp_8 = str(
                    decimal.Decimal(temp_1 * temp_2 / temp_3 / temp_4).quantize(decimal.Decimal('0.000')))  # 计算单行金额
                temp_item2 = QTableWidgetItem(temp_8)
                temp_item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_packing.setItem(x, 9, temp_item2)  # 填写计算方式单元格

    #  删除一行-包装费
    def delete_line_packing(self):
        if len(self.tableWidget_packing.selectedItems()) == 0:
            QMessageBox.about(self,'提示',"没有选中任何行！")
            print(f'没有选中任何行！')
            return
        else:
            # print(f'当前选中是第【{self.tableWidget_packing.selectedItems()[0].row()}】行！')

            current_select_line = self.tableWidget_packing.selectedItems()[0].row()

            # print(f'删除前共有【{self.tableWidget_packing.rowCount()}】行！')
            self.tableWidget_packing.removeRow(current_select_line)
            # print(f'删除【后】共有【{self.tableWidget_packing.rowCount()}】行！')

        ##  删除后序号会出现错误，重新把表格中的序号做处理
        for x in range(self.tableWidget_packing.rowCount()):
            temp_item  = QTableWidgetItem(chr(x + 65))
            temp_item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tableWidget_packing.setItem(x,0,temp_item)

    #########################################################################################################
    #  初始化QComboBox下拉框
    def initComboBox(self):
        self.comboBox_Type0 = QComboBox()  # 新建一个QComboBox控件，材料表0列
        self.comboBox_Type1 = QComboBox()  # 新建一个QComboBox控件，材料表1列
        self.comboBox_Type1.setEditable(True)  # 设置下拉框允许编辑，以备后面设置自动补全功能
        self.comboBox_Type2 = QComboBox()  # 新建一个QComboBox控件，加工表0列
        self.comboBox_Type3 = QComboBox()  # 新建一个QComboBox控件，加工表1列
        self.comboBox_Type3.setEditable(True)  # 设置下拉框允许编辑，以备后面设置自动补全功能
        self.comboBox_Type4 = QComboBox()  # 新建一个QComboBox控件，包装表0列
        self.comboBox_Type5 = QComboBox()  # 新建一个QComboBox控件，包装表1列
        self.comboBox_Type5.setEditable(True)  # 设置下拉框允许编辑，以备后面设置自动补全功能

    #  关于对话框
    def about(self, aboutstr):
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', aboutstr)
        msgBox.exec()

    #  设置客户下拉框
    def setComboBoxCustomer(self):
        sql_db = ObjectSearch()
        customer_query = """
            SELECT `客户名称` FROM `客户表`
        """
        comboBoxItems_customer = []
        temp3 = sql_db.search(customer_query)
        for x in range(len(temp3)): #  把客户名称查询结果从嵌套元组转换成非嵌套列表
            for y in range(len(temp3[x])):
                comboBoxItems_customer.append(temp3[x][y])
        # print(f"客户名称：{comboBoxItems_customer}")

        #  客户名称下拉框
        self.comboBox_customer.setEditable(True)
        self.comboBox_customer.clear()
        self.comboBox_customer.addItems(comboBoxItems_customer)
        self.comboBox_customer.setCurrentIndex(-1)
        #  设置下拉框自动补全
        self.completer = QCompleter(comboBoxItems_customer) #  实例化自动补全控件
        self.completer.setFilterMode(Qt.MatchContains)  #  设置过滤模式
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_customer.setCompleter(self.completer)

    #  初始化界面
    def init_form(self):
        # self.pushButton_new.setEnabled(False)  # 新建按钮

        #  读取数据库的ID（序号）的最大数，加1后填入序号
        #  目的是保持新建的单据，序号一定顺序下来最大数
        sql_db = ObjectSearch()
        temp1 = sql_db.get_id() #  查询最大序号
        temp2 = max(temp1) + 1  #  最大序号+1 为新的序号，以保证新建单据的序号是最新的
        self.lineEdit_Number.setText(str(temp2))
        self.lineEdit_Number.setEnabled(False)  # 序号
        self.lineEdit_MaterialCost.setEnabled(False)  # 材料总金额
        self.lineEdit_ProcessCost.setEnabled(False)  # 加工总金额
        self.lineEdit_PackingCost.setEnabled(False)  # 包装总金额
        self.lineEdit_TotalCost.setEnabled(False)  # 总金额
        self.dateEdit_CreationDate.setEnabled(False)  # 作成日期
        self.dateEdit_CreationDate.setDate(QDate.currentDate())  # 设置作成日期为当前日期
        self.dateEdit_EffectiveDate.setDate(QDate.currentDate())  # 设置生效日期为当前日期
        self.lineEdit_MaterialCount.setEnabled(False)  # 材料表的累计金额
        self.lineEdit_ProcessCount.setEnabled(False)  # 加工表的累计金额
        self.lineEdit_PackingCount.setEnabled(False)  # 包装表的累计金额

        self.pushButton_delete1.setEnabled(False)  # 删除一行
        self.pushButton_delete2.setEnabled(False)  # 删除一行
        self.pushButton_delete3.setEnabled(False)  # 删除一行

        # self.pushButton_out.setEnabled(False)  # 输出EXCEL 按钮不可用

        # 对【固定费用】、【运费】、【管理费】的输入做限制
        ## 使用正则表达式,浮点验证器不生效
        re = QRegExp('^[0-9]+(.[0-9]{3})?$')  # 正则:限制浮点数输入 只能输入3位小数的正实数
        re_validato = QRegExpValidator(re, self)  # 实例化正则验证器
        self.lineEdit_FixedFee.setValidator(re_validato)
        self.lineEdit_CarriageFee.setValidator(re_validato)
        self.lineEdit_ManagementFee.setValidator(re_validato)

        #  材料费表格
        self.tableWidget_materail.setColumnCount(11)
        self.tableWidget_materail.setHorizontalHeaderLabels(
            ['序号', '材料类型', '物料编码', '   名称  ', '   供应商 ', '单价(HKD)', '   用量  ',
             '每模用量', '每模出数', '切割个数', '金额(HKD)'])
        # 使用函数horizontalHeager()设置表格为自适应的伸缩模式，即可根据窗口大小来改变网格大小
        self.tableWidget_materail.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 将行和列的宽度、高度设置为与所显示内容的宽度、高度相匹配
        self.tableWidget_materail.resizeColumnsToContents()
        # 设置列不能更改
        self.tableWidget_materail.setItemDelegateForColumn(10, EmptyDelegate(self)) #  金额列，，由程序自动计算
        self.tableWidget_materail.setItemDelegateForColumn(0, EmptyDelegate(self))  #  序号
        self.tableWidget_materail.setItemDelegateForColumn(2, EmptyDelegate(self))  #  料号为下拉框，还是可以更改
        self.tableWidget_materail.setItemDelegateForColumn(3, EmptyDelegate(self))  #  名称
        self.tableWidget_materail.setItemDelegateForColumn(4, EmptyDelegate(self))  #  供应商

        # 隐藏列标题
        self.tableWidget_materail.verticalHeader().setVisible(False)
        # 设置表头不塌陷
        self.tableWidget_materail.horizontalHeader().setHighlightSections(False)
        # 设置表格按行选中，默认是按单元格选中
        self.tableWidget_materail.setSelectionBehavior(QAbstractItemView.SelectRows)

        # # 允许右键产生子菜单
        # self.tableWidget_materail.setContextMenuPolicy(Qt.CustomContextMenu)
        # # 右键菜单
        # self.tableWidget_materail.customContextMenuRequested.connect(self.generateMenuMaterial)

        #  立即刷新表格
        self.tableWidget_materail.repaint()

        #  打印表格的最大行值
        # print(f"material表格的最大行是：{self.tableWidget_materail.rowCount()}")

        #  加工费表格
        self.tableWidget_processing.setColumnCount(10)
        self.tableWidget_processing.setHorizontalHeaderLabels(
            ['序号', '工序类型', '工序名称', '工序代码', '工程单价(HKD)', '工数(PCS/H)', '切割数', '用量', '计算方式', '金额(HKD)'])
        # 使用函数horizontalHeager()设置表格为自适应的伸缩模式，即可根据窗口大小来改变网格大小
        self.tableWidget_processing.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 将行和列的宽度、高度设置为与所显示内容的宽度、高度相匹配
        self.tableWidget_processing.resizeColumnsToContents()
        # 隐藏列标题
        self.tableWidget_processing.verticalHeader().setVisible(False)
        # 设置列不能更改
        self.tableWidget_processing.setItemDelegateForColumn(9, EmptyDelegate(self))    #  金额列，，由程序自动计算
        self.tableWidget_processing.setItemDelegateForColumn(0, EmptyDelegate(self))    #  序号
        self.tableWidget_processing.setItemDelegateForColumn(3, EmptyDelegate(self))    #  工序代码
        # 设置表格按行选中，默认是按单元格选中
        self.tableWidget_processing.setSelectionBehavior(QAbstractItemView.SelectRows)

        #  包装费表格
        self.tableWidget_packing.setColumnCount(10)
        self.tableWidget_packing.setHorizontalHeaderLabels(
            ['序号', '材料类型', '物料编码', '包装名称', '单价(HKD)', '用量', '包装数', '回收否', '计算方式', '金额(HKD)'])
        # 使用函数horizontalHeager()设置表格为自适应的伸缩模式，即可根据窗口大小来改变网格大小
        self.tableWidget_packing.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 将行和列的宽度、高度设置为与所显示内容的宽度、高度相匹配
        self.tableWidget_packing.resizeColumnsToContents()
        # 隐藏列标题
        self.tableWidget_packing.verticalHeader().setVisible(False)
        # 设置列不能更改
        self.tableWidget_packing.setItemDelegateForColumn(9, EmptyDelegate(self))   #  金额列，，由程序自动计算
        self.tableWidget_packing.setItemDelegateForColumn(0, EmptyDelegate(self))   #  序号
        self.tableWidget_packing.setItemDelegateForColumn(3, EmptyDelegate(self))   #  包装名称
        # 设置表格按行选中，默认是按单元格选中
        self.tableWidget_packing.setSelectionBehavior(QAbstractItemView.SelectRows)

        sql_db.close()


    #  对建单界面的控件设置不可用
    def setObjectEnable(self, status):
        self.lineEdit_ProductCode.setEnabled(status)  # 成品编码
        self.comboBox_customer.setEnabled(status)  # 客户名称
        self.lineEdit_PinFan.setEnabled(status)  # 品名

        self.lineEdit_MonthlyProduction.setEnabled(status)  # 月产量
        self.lineEdit_FixedFee.setEnabled(status)  # 固定费用
        self.lineEdit_CarriageFee.setEnabled(status)  # 运费
        self.lineEdit_ManagementFee.setEnabled(status)  # 管理费
        self.lineEdit_MaterialCost.setEnabled(status)  # 材料总金额
        self.lineEdit_ProcessCost.setEnabled(status)  # 加工总金额
        self.lineEdit_PackingCost.setEnabled(status)  # 包装总金额
        self.lineEdit_TotalCost.setEnabled(status)  # 总金额

        self.dateEdit_EffectiveDate.setEnabled(status)  # 生效日期
        self.dateEdit_CreationDate.setEnabled(status)  # 作成日期
        self.lineEdit_Creator.setEnabled(status)  # 作成
        self.lineEdit_Corrector.setEnabled(status)  # 整理
        self.textEdit_Remarks.setEnabled(status)  # 备注

        self.pushButton_add1.setEnabled(status)  # 材料表-增加一行
        self.pushButton_add2.setEnabled(status)  # 加工表-增加一行
        self.pushButton_add3.setEnabled(status)  # 包装表-增加一行

    ##  清空表格
    def clearWindow(self):
        # for x in range(self.tableWidget_materail.rowCount(),-1,-1):
        #     self.tableWidget_materail.removeRow(x)
        self.tableWidget_materail.setRowCount(0)    #  设置材料费表格行为0
        self.tableWidget_materail.clearContents()   #  清空材料费除标题外的所有内容
        self.tableWidget_processing.setRowCount(0)
        self.tableWidget_processing.clearContents()
        self.tableWidget_packing.setRowCount(0)
        self.tableWidget_packing.clearContents()

        self.initialize()   #  初始化控件及变量

        #  读取数据库的ID（序号）的最大数，加1后填入序号
        #  目的是保持新建的单据，序号一定顺序下来最大数
        sql_db = ObjectSearch()
        temp1 = sql_db.get_id()
        sql_db.close()
        temp2 = max(temp1) + 1
        self.lineEdit_Number.setText(str(temp2))
        self.lineEdit_Number.setEnabled(False)  # 序号

        self.lineEdit_ProductCode.clear()  # 成品编码
        self.comboBox_customer.setCurrentIndex(-1)  # 客户名称
        self.lineEdit_PinFan.clear()  # 品名
        self.lineEdit_MonthlyProduction.clear()  # 月产量
        self.lineEdit_FixedFee.clear()  # 固定费用
        self.lineEdit_CarriageFee.clear()  # 运费
        self.lineEdit_ManagementFee.clear()  # 管理费
        self.lineEdit_MaterialCost.clear()  # 材料总金额
        self.lineEdit_ProcessCost.clear()  # 加工总金额
        self.lineEdit_PackingCost.clear()  # 包装总金额
        self.lineEdit_TotalCost.clear()  # 总金额
        self.lineEdit_Creator.clear()  # 作成
        self.lineEdit_Corrector.clear()  # 整理
        self.textEdit_Remarks.clear()  # 备注

        #  设置输入控件可用
        self.initComboBox()
        self.setComboBoxCustomer()
        self.lineEdit_ProductCode.setEnabled(True)   # 成品编码框
        self.comboBox_customer.setEnabled(True)  # 客户名称
        self.lineEdit_PinFan.setEnabled(True)  # 品名
        self.lineEdit_MonthlyProduction.setEnabled(True)  # 月产量
        self.lineEdit_FixedFee.setEnabled(True)  # 固定费用
        self.lineEdit_CarriageFee.setEnabled(True)  # 运费
        self.lineEdit_ManagementFee.setEnabled(True)  # 管理费
        self.dateEdit_EffectiveDate.setDate(QDate.currentDate())  # 设置生效日期为当前日期
        self.dateEdit_CreationDate.setDate(QDate.currentDate())  # 设置作成日期为当前日期
        self.lineEdit_Creator.setEnabled(True)  # 作成
        self.lineEdit_Corrector.setEnabled(True)  # 整理
        self.textEdit_Remarks.setEnabled(True)  # 备注
        self.pushButton_add1.setEnabled(True)   # 材料费——增加一行
        self.pushButton_add2.setEnabled(True)  # 加工费——增加一行
        self.pushButton_add3.setEnabled(True)   # 包装费——增加一行
        self.pushButton_save.setEnabled(True)   #  保存
