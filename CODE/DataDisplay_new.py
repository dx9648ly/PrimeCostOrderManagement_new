# -*- coding:utf-8 -*-
# project: PrimeCostOrderManagement
# @File  : DataDisplay.py
# @Time  : 2021-07-05  14:18
# @Author: LongYuan
# @FUNC  :
import os
import shutil
import winreg

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QHeaderView, QWidget, QTableWidget, QComboBox

from CODE.EditWidget import EditWidget
from CODE.EmptyDelegate import EmptyDelegate
from CODE.OutExcel_new import OutExcel
from CODE.mysqlCode_new import ObjectSearch
# from CODE.ProductImageDisplay import ProductImageDisplayWindow
from UI.DataDisplay_1 import Ui_Form as uiDataDisplay


class DataDisplayWindow(QWidget, uiDataDisplay):
    signal = pyqtSignal()

    def __init__(self,usertype = None):
        super(DataDisplayWindow, self).__init__()
        self.setupUi(self)

        self.ID = ''    #  当前显示的ID
        self.pushButton_view_document.setEnabled(False) #  默认设置“查看文档”不可用
        self.btn_productImage.hide()    #  默认状态下【产品图片】按钮不显示
        self.btn_viewYuanJia.hide()     #  默认状态下【显示原价】按钮不显示

        #  初始化表格
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使列表自适应宽度

        #  把按钮与槽函数连接
        self.tableWidget_1.itemChanged.connect(self.table_update_price) # 总表——单元格修改后自动触发动作
        self.tableWidget_2.itemChanged.connect(self.table_update_material)    # 材料表——单元格修改后自动触发动作
        self.tableWidget_3.itemChanged.connect(self.table_update_processing)    # 加工表——单元格修改后自动触发动作
        self.tableWidget_4.itemChanged.connect(self.table_update_packing)    # 包装表——单元格修改后自动触发动作
        self.tableWidget_1.cellDoubleClicked.connect(self.edit_widget_fun)    # 总表——备注单元格双击触发动作
        self.pushButton_output_excel.clicked.connect(self.output_excel) #  生成文档按钮
        self.pushButton_view_document.clicked.connect(self.view_document)   #  查看文档按钮
        self.pushButton_update_image.clicked.connect(self.update_image) #  上传图片按钮
        self.pushButton_update_document.clicked.connect(self.update_document)   #  上传文档按钮
        self.btn_productImage.clicked.connect(self.productImageDisplay) #  产品图片按钮
        self.btn_updateYuanJia.clicked.connect(self.update_yuanjia) # 上传原价按钮
        self.btn_viewYuanJia.clicked.connect(self.yuanjiaDisplay)   #  显示原价按钮

        self.tableWidget_1.currentCellChanged.connect(self.tableWidget_1_currentCellChanged_func)   # 单元格改变信号
        self.tableWidget_1.cellDoubleClicked.connect(self.tableWidget_1_cellDoubleClicked_func)     #  单元格双击信号

        # if usertype is None:
        #     self.usertype = 0
        # else:
        self.usertype = usertype


    #  查询并显示数据
    def query_and_show(self, tableName, str):
        # finished_product_code = ""  # 成品编码
        ################################
        #   1、显示总表表相关数据
        search_db = ObjectSearch()  # 实例化数据库查询类
        if tableName == "ID":
            self.ID = str
            search_result_old = list(search_db.get_price1(f" ID = {str}"))  # 按ID在数据库中查询原价总表数据
            finished_product_code = search_db.id_to_productionNumber(int(str))  # 通过ID号获取成品编码
            self.finished_product_code = finished_product_code
        else:
            search_result_old = list(search_db.get_price1(f"成品编码 = '{str}'"))  # 按成品编码在数据库中查询原价总表数据
            finished_product_code = str
            # select_sql_where = f" 成品编码 = '{str}' "  # 查询条件
        # print(f"成品编码 = '{finished_product_code}'")
        # print(f"总表数据：\t{search_result_old}")
        # print("列表长度：" + format(len(search_result_old)))
        search_result_new = []  # 把None替换成“”空字符的数据列表
        for x in range(len(search_result_old[0])):  # 把总表数据列表中的None 转变成“”
            if search_result_old[0][x] is None:
                search_result_new.append("")
            else:
                search_result_new.append(search_result_old[0][x])

        #       1.1 把总表中标题作为tablewidget_1的标题
        material_head_title = search_db.get_fieldName("`原价明细总表_new`")  # 总表字段名称
        self.tableWidget_1.setColumnCount(len(material_head_title))  # 表格的字段数量
        self.tableWidget_1.setHorizontalHeaderLabels(material_head_title)  # 设置表格标题

        #       1.2 清空表格的数据
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.clearContents()
        # print("当前表格2的行数：%s"%self.tableWidget_2.rowCount())
        #       1.3 根据查找到总表的数据来设定表格的行
        self.tableWidget_1.setRowCount(1)  # 设置最大行数为1
        self.tableWidget_1.verticalHeader().setVisible(False)  # 不显示表格的垂直标题，即不显示行号
        #       1.4 把数据显示到表格
        for x in range(len(search_result_new)-1):
            if search_result_new[x] is None:
                temp_item = QTableWidgetItem("*")  # 如果值为None，则使用“*”代替
            else:
                temp_item = QTableWidgetItem(format(search_result_new[x]))  # 把值转换成表格型后赋值
            temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
            self.tableWidget_1.setItem(0, x, temp_item)  # 按行、列循环写入表格

        temp20 = QTableWidgetItem(format(search_result_new[-1]))    # 把备注的值作为一个单元格item
        temp20.setTextAlignment(Qt.AlignVCenter)
        self.tableWidget_1.setItem(0,26,temp20)

        # 使用函数horizontalHeager()设置表格为自适应的伸缩模式，即可根据窗口大小来改变网格大小
        # self.tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # self.tableWidget_1.setColumnWidth(0, 20)  # 设置 序号 宽度为20
        # self.tableWidget_1.setColumnWidth(4, 30)  # 设置 分类 的宽度为30
        # self.tableWidget_1.setColumnWidth(5, 30)  # 设置 规格 的宽度为30
        # self.tableWidget_1.setColumnWidth(6, 30)  # 设置第 重要性 的宽度为30
        # self.tableWidget_1.setColumnWidth(19, 3000)  # 设置 备注 的宽度为300

        # 设置 序号 不能更改
        self.tableWidget_1.setItemDelegateForColumn(0, EmptyDelegate(self))
        self.tableWidget_1.setItemDelegateForColumn(1, EmptyDelegate(self))

        self.tableWidget_1.setColumnWidth(0, 50)  # 设置第0列的宽度为50


        # 设置 列按内容自动设置列宽
        for x in range(0, 27):
            self.tableWidget_1.horizontalHeader().setSectionResizeMode(x, QHeaderView.ResizeToContents)
        # self.tableWidget_1.horizontalHeader().setSectionResizeMode(26, QHeaderView.ResizeToContents)
        # self.tableWidget_1.setRowHeight(0,50)


        # 将行和列的宽度、高度设置为与所显示内容的宽度、高度相匹配
        # self.tableWidget_1.resizeColumnsToContents()
        self.tableWidget_1.resizeRowsToContents()

        #####################################################################################################
        #   2、显示材料表相关数据
        select_sql_where_material = f" 成品编码 = '{finished_product_code}' "  # 查询条件
        material_list = search_db.get_price2("`材料费`", select_sql_where_material)  # 获取材料表的相关数据
        # print(f"材料表的数据：{material_list}")

        #       2.1 把材料表中标题作为tablewidget的标题
        material_head_title = search_db.get_fieldName("`材料费`")  # 材料费字段名称
        self.tableWidget_2.setColumnCount(len(material_head_title))  # 表格的字段数量
        self.tableWidget_2.setHorizontalHeaderLabels(material_head_title)  # 设置表格标题

        #       2.2 清空表格的数据
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()
        # print("当前表格2的行数：%s"%self.tableWidget_2.rowCount())
        #       2.3 根据查找到材料表的数据来设定表格的行
        self.tableWidget_2.setRowCount(len(material_list))  # 设置最大行数为列表的长度
        self.tableWidget_2.verticalHeader().setVisible(False)  # 不显示表格的垂直标题，即不显示行号
        #       2.4 把数据显示到表格
        for x in range(len(material_list)):
            for y in range(len(material_list[x])):
                if material_list[x][y] is None:
                    temp_item = QTableWidgetItem("*")  # 如果值为None，则使用“”代替
                else:
                    temp_item = QTableWidgetItem(format(material_list[x][y]))  # 把值转换成表格型后赋值
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_2.setItem(x, y, temp_item)  # 按行、列循环写入表格

        self.tableWidget_2.setColumnWidth(0, 50)  # 设置第0列的宽度为100
        # self.tableWidget_2.setColumnWidth(4, 100)  # 设置第4列的宽度为100
        # self.tableWidget_2.setColumnWidth(5, 100)  # 设置第5列的宽度为100
        # self.tableWidget_2.setColumnWidth(6, 100)  # 设置第6列的宽度为100
        # self.tableWidget_2.setColumnWidth(7, 120)  # 设置第7列的宽度为100

        # 设置序号、成品编码、品名不能更改
        self.tableWidget_2.setItemDelegateForColumn(0, EmptyDelegate(self))
        self.tableWidget_2.setItemDelegateForColumn(1, EmptyDelegate(self))
        self.tableWidget_2.setItemDelegateForColumn(2, EmptyDelegate(self))

        # 设置 列按内容自动设置列宽
        for x in range(8, len(material_head_title) - 1):
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(x, QHeaderView.ResizeToContents)

        self.tableWidget_2.setColumnHidden(1,True)  #  隐藏成品编码列
        self.tableWidget_2.setColumnHidden(2,True)  #  隐藏品名列
        self.tableWidget_2.setAlternatingRowColors(True)    #  隔行变色


        ########################
        #   3、显示加工表相关数据
        select_sql_where_processing = f" 成品编码 = '{finished_product_code}' ORDER BY `成品编码`, `序号` "  # 查询条件
        processing_list = search_db.get_price2("`加工费`", select_sql_where_processing)  # 获取加工表的相关数据
        # print("加工数据的数量：%s"%len(procedure_list))

        #       3.1 把加工表中标题作为tablewidget的标题
        processing_head_title = search_db.get_fieldName("`加工费`")  # 加工费字段名称
        self.tableWidget_3.setColumnCount(len(processing_head_title))  # 表格的字段数量
        self.tableWidget_3.setHorizontalHeaderLabels(processing_head_title)  # 设置表格标题

        #       3.2 清空表格原来的数据
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(0)
        # print("当前表格3的行数：%s"%self.tableWidget_3.rowCount())

        #       3.3 根据查找到加工表的数据来设定表格的行
        self.tableWidget_3.setRowCount(len(processing_list))  # 设置最大行数为列表的长度
        self.tableWidget_3.verticalHeader().setVisible(False)  # 不显示表格的垂直标题，即不显示行号
        #       3.4 把数据显示到表格
        for x in range(len(processing_list)):
            for y in range(len(processing_list[x])):
                if processing_list[x][y] is None:
                    temp_item = QTableWidgetItem("*")  # 如果值为None，则使用“”代替
                else:
                    temp_item = QTableWidgetItem(format(processing_list[x][y]))  # 把值转换成表格型后赋值
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_3.setItem(x, y, temp_item)  # 按行、列循环写入表格
        self.tableWidget_3.setColumnWidth(0, 50)  # 设置第0列的宽度为100
        # self.tableWidget_3.setColumnWidth(9, 200)  # 设置第9列的宽度为200

        # 设置序号、成品编码、品名不能更改
        self.tableWidget_3.setItemDelegateForColumn(0, EmptyDelegate(self))
        self.tableWidget_3.setItemDelegateForColumn(1, EmptyDelegate(self))
        self.tableWidget_3.setItemDelegateForColumn(2, EmptyDelegate(self))

        self.tableWidget_3.setColumnHidden(1,True)  #  隐藏成品编码列
        self.tableWidget_3.setColumnHidden(2,True)  #  隐藏品名列
        self.tableWidget_3.setColumnHidden(4,True)  #  隐藏工序代码列
        self.tableWidget_3.setAlternatingRowColors(True)    #  隔行变色

        ################################
        #   4、显示包装表相关数据
        select_sql_where_packing = f" 成品编码 = '{finished_product_code}' "  # 查询条件
        packing_list = search_db.get_price2("`包装费`", select_sql_where_packing)  # 获取包装表的相关数据
        # print(packing_list)

        #       4.1 把包装表中标题作为tablewidget的标题
        packing_head_title = search_db.get_fieldName("`包装费`")  # 包装费字段名称
        # print(packing_head_title)
        self.tableWidget_4.setColumnCount(len(packing_head_title))  # 表格的字段数量
        self.tableWidget_4.setHorizontalHeaderLabels(packing_head_title)  # 设置表格标题

        #       4.2 清空表格原来的数据
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.clearContents()
        # print("写入数据前表格4的行数：%s"%self.tableWidget_4.rowCount())

        #       4.3 根据查找到包装表的数据来设定表格的行
        self.tableWidget_4.setRowCount(len(packing_list))  # 设置最大行数为列表的长度
        self.tableWidget_4.verticalHeader().setVisible(False)  # 不显示表格的垂直标题，即不显示行号
        #       4.4 把数据显示到表格
        for x in range(len(packing_list)):
            for y in range(len(packing_list[x])):
                if packing_list[x][y] is None:
                    temp_item = QTableWidgetItem("*")  # 如果值为None，则使用“”代替
                else:
                    temp_item = QTableWidgetItem(format(packing_list[x][y]))  # 把值转换成表格型后赋值
                temp_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置垂直和水平居中
                self.tableWidget_4.setItem(x, y, temp_item)  # 按行、列循环写入表格
        self.tableWidget_4.setColumnWidth(0, 50)  # 设置第1列的宽度为100
        self.tableWidget_4.setAlternatingRowColors(True)    #  隔行变色

        # 设置序号、成品编码、品名不能更改
        self.tableWidget_4.setItemDelegateForColumn(0, EmptyDelegate(self))
        self.tableWidget_4.setItemDelegateForColumn(1, EmptyDelegate(self))
        self.tableWidget_4.setItemDelegateForColumn(2, EmptyDelegate(self))

        self.tableWidget_4.setColumnHidden(1,True)  #  隐藏成品编码列
        self.tableWidget_4.setColumnHidden(2,True)  #  隐藏品名列
        self.tableWidget_4.setColumnHidden(3,True)  #  隐藏料号列

        ################################
        #  5.1 查询，单据的文件信息。如果有保存图片，或PDF，单击相应的按钮可以打开；如果数据库文件表中没有相关的信息，单击相应按钮
        #       会提示是否上传相应的文件。如果上传，则会把文件复制到服务器相应的目录。
        # print(f"成品编码={finished_product_code}")
        query_criteria_image = f"成品编码 ='{finished_product_code}' AND 类型 = '图片'"
        query_criteria_document = f"成品编码 ='{finished_product_code}' AND 类型 = '文档'"
        query_criteria_yuanjia = f"成品编码 ='{finished_product_code}' AND 类型 = '原价'"
        temp_image = search_db.get_price2("文件资料表",query_criteria_image)  #  根据成品编码，查询文件资料表中是否存在对应的图片信息
        temp_document = search_db.get_price2("文件资料表",query_criteria_document)  #  根据成品编码，查询文件资料表中是否存在对应的文档信息
        temp_yuanjia = search_db.get_price2("文件资料表",query_criteria_yuanjia)  #  根据成品编码，查询文件资料表中是否存在对应的原价文档信息

        if len(temp_image) == 0:
            print(f"该产品没有保存任何图片！")
        elif len(temp_image) == 1:
            # print(f"文件信息：{temp_image}")
            self.image_path = temp_image[0][3]   #  获取图片的文件名及路径
            self.btn_productImage.show()    # 如果数据库中存在图片记录，则【产品图片】按钮显示

        if len(temp_document) == 0:
            print(f"该产品没有保存任何文档！")
        else:
            # print(f"文件信息：{temp_document}")
            self.pushButton_view_document.setEnabled(True)  #  有文档资料，按钮可用

        if len(temp_yuanjia) == 0:
            print(f"该产品没有保存任何原价文档！")
        elif len(temp_yuanjia) == 1:
            # print(f"文件信息：{temp_yuanjia}")
            self.yuanjia_path = temp_yuanjia[0][3]   #  获取图片的文件名及路径
            self.btn_viewYuanJia.show()    # 如果数据库中存在图片记录，则【显示原价】按钮显示

        # 判断账号为查询账号就不显示价格相关的信息
        # if self.usertype >= 30 and self.usertype < 40:


        search_db.close()  # 关闭数据库链接

        self.settingWidgetAvailable(self.usertype)

    #  产品图片——按钮
    def productImageDisplay(self):
        # self.productImageDisplay = ProductImageDisplayWindow(self.image_path)
        # self.productImageDisplay.show()
        os.startfile(self.image_path)   #  调用系统程序打开图片

    #  显示原价——按钮
    def yuanjiaDisplay(self):
        os.startfile(self.yuanjia_path) #  调用系统程序打开原价文档

    #  上传图片——函数
    def update_image(self):
        storage_path = f"\\\\192.168.20.4\\共享文件\\资材部\\原价程序文件"
        finished_product_code = self.tableWidget_1.item(0,1).text() #  获取当前显示的成品编码
        full_path = f"{storage_path}\\{finished_product_code}"
        search_db = ObjectSearch()  # 实例化数据库查询类
        query_criteria_image = f"成品编码 ='{finished_product_code}' AND 类型 = '图片'"
        temp_image = search_db.get_price2("文件资料表",query_criteria_image)  #  根据成品编码，查询文件资料表中是否存在对应的图片信息
        if len(temp_image) == 0:
            if not os.path.exists(full_path):
                os.mkdir(full_path)
                if not os.path.exists(full_path):
                    QMessageBox.warning(self,"警告","文件夹建立失败，请确认是否有权限！")
                    return
            update_file = self.slot_btn_chooseMutiFile("JPEG 图片 (*.jpg;*.jpeg);;PNG 图片 (*.png);;All Files (*)")
            if update_file is None:
                return
            update_file_full = f"\\\\192.168.20.4\\\\共享文件\\\\资材部\\\\原价程序文件\\\\{finished_product_code}\\\\{os.path.basename(update_file)}"
            # print(f"完整的路径和文件名：'{update_file_full}'")
            shutil.copy(update_file,full_path)
            if not os.path.exists(update_file_full):
                QMessageBox.warning(self,"警告", "文件上传失败，请确认是否有权限！")
                return
            update_sql = f"""
                INSERT INTO `文件资料表` (`成品编码`,`类型`,`存储路径`) 
                VALUES ('{finished_product_code}','图片','\\\\{update_file_full}')
            """
            search_db.writeSqlTable(update_sql)
            QMessageBox.about(self,"提示","图片上传成功!")

        else:
            temp1 = QMessageBox.question(self,"警告","数据库中已经有图片记录，是否更新？",QMessageBox.Yes|QMessageBox.No)
            if temp1 == QMessageBox.Yes:
                update_file = self.slot_btn_chooseMutiFile()
                if update_file is None:
                    return
                update_file_full = f"\\\\192.168.20.4\\\\共享文件\\\\资材部\\\\原价程序文件\\\\{finished_product_code}\\\\{os.path.basename(update_file)}"
                shutil.copy(update_file,full_path)
                if not os.path.exists(update_file_full):
                    QMessageBox.warning(self,"警告", "文件上传失败，请确认是否有权限！")
                    return
                update_sql = f"""
                    UPDATE `文件资料表`
                    SET `存储路径` = '\\\\{update_file_full}'
                    WHERE `成品编码` = '{finished_product_code}' AND `类型`='图片'
                """
                search_db.writeSqlTable(update_sql)
                search_db.close()  # 关闭数据库链接
                QMessageBox.about(self, "提示", "图片更新成功!")
            elif temp1 == QMessageBox.No:
                return

    #  上传文档——函数
    def update_document(self):
        storage_path = f"\\\\192.168.20.4\\共享文件\\资材部\\原价程序文件"
        finished_product_code = self.tableWidget_1.item(0,1).text() #  获取当前显示的成品编码
        full_path = f"{storage_path}\\{finished_product_code}"
        search_db = ObjectSearch()  # 实例化数据库查询类
        query_criteria_document = f"成品编码 ='{finished_product_code}' AND 类型 = '文档'"
        temp_document = search_db.get_price2("文件资料表",query_criteria_document)  #  根据成品编码，查询文件资料表中是否存在对应的文档信息
        # print(f"值：{temp_document}")
        # print(f"数据库表中记录数量：{len(temp_document)}")
        if len(temp_document) == 0:
            if not os.path.exists(full_path):
                os.mkdir(full_path)
                if not os.path.exists(full_path):
                    QMessageBox.warning(self,"警告","文件夹建立失败，请确认是否有权限！")
                    return
            update_file = self.slot_btn_chooseMutiFile("PDF Files (*.pdf);;Excel Files (*.xlsx;*.xls);;All Files (*)")
            if update_file is None:
                return
            update_file_full = f"\\\\192.168.20.4\\\\共享文件\\\\资材部\\\\原价程序文件\\\\{finished_product_code}\\\\{os.path.basename(update_file)}"
            # print(f"完整的路径和文件名：'{update_file_full}'")
            shutil.copy(update_file,full_path)
            if not os.path.exists(update_file_full):
                QMessageBox.warning(self,"警告", "文件上传失败，请确认是否有权限！")
                return
            update_sql = f"""
                INSERT INTO `文件资料表` (`成品编码`,`类型`,`存储路径`) 
                VALUES ('{finished_product_code}','文档','\\\\{update_file_full}')
            """
            search_db.writeSqlTable(update_sql)
            QMessageBox.about(self,"提示","文档上传成功!")
        else:
            temp1 = QMessageBox.question(self,"警告","数据库中已经有文档记录，是否更新？",QMessageBox.Yes|QMessageBox.No)
            if temp1 == QMessageBox.Yes:
                update_file = self.slot_btn_chooseMutiFile()
                if update_file is None:
                    return
                update_file_full = f"\\\\192.168.20.4\\\\共享文件\\\\资材部\\\\原价程序文件\\\\{finished_product_code}\\\\{os.path.basename(update_file)}"
                shutil.copy(update_file,full_path)
                if not os.path.exists(update_file_full):
                    QMessageBox.warning("警告", "文件上传失败，请确认是否有权限！")
                    return
                update_sql = f"""
                    UPDATE `文件资料表`
                    SET `存储路径` = '\\\\{update_file_full}'
                    WHERE `成品编码` = '{finished_product_code}' AND `类型`='文档'
                """
                search_db.writeSqlTable(update_sql)
                search_db.close()  # 关闭数据库链接
                QMessageBox.about(self, "提示", "文档上传成功!")
            elif temp1 == QMessageBox.No:
                return

    #  上传原价——函数
    def update_yuanjia(self):
        storage_path = f"\\\\192.168.20.4\\共享文件\\资材部\\原价程序文件"
        finished_product_code = self.tableWidget_1.item(0,1).text() #  获取当前显示的成品编码
        full_path = f"{storage_path}\\{finished_product_code}"
        search_db = ObjectSearch()  # 实例化数据库查询类
        query_criteria_image = f"成品编码 ='{finished_product_code}' AND 类型 = '原价'"
        temp_image = search_db.get_price2("文件资料表",query_criteria_image)  #  根据成品编码，查询文件资料表中是否存在对应的原价文件存储信息
        if len(temp_image) == 0:
            if not os.path.exists(full_path):
                os.mkdir(full_path)
                if not os.path.exists(full_path):
                    QMessageBox.warning(self,"警告","文件夹建立失败，请确认是否有权限！")
                    return
            update_file = self.slot_btn_chooseMutiFile("PDF Files (*.pdf);;Excel Files (*.xlsx;*.xls);;All Files (*)")
            if update_file is None:
                return
            update_file_full = f"\\\\192.168.20.4\\\\共享文件\\\\资材部\\\\原价程序文件\\\\{finished_product_code}\\\\{os.path.basename(update_file)}"
            # print(f"完整的路径和文件名：'{update_file_full}'")
            shutil.copy(update_file,full_path)
            if not os.path.exists(update_file_full):
                QMessageBox.warning(self,"警告", "文件上传失败，请确认是否有权限！")
                return
            update_sql = f"""
                INSERT INTO `文件资料表` (`成品编码`,`类型`,`存储路径`) 
                VALUES ('{finished_product_code}','原价','\\\\{update_file_full}')
            """
            search_db.writeSqlTable(update_sql)
            QMessageBox.about(self,"提示","原价文件上传成功!")

        else:
            temp1 = QMessageBox.question(self,"警告","数据库中已经有原价文件记录，是否更新？",QMessageBox.Yes|QMessageBox.No)
            if temp1 == QMessageBox.Yes:
                update_file = self.slot_btn_chooseMutiFile()
                if update_file is None:
                    return
                update_file_full = f"\\\\192.168.20.4\\\\共享文件\\\\资材部\\\\原价程序文件\\\\{finished_product_code}\\\\{os.path.basename(update_file)}"
                shutil.copy(update_file,full_path)
                if not os.path.exists(update_file_full):
                    QMessageBox.warning(self,"警告", "文件上传失败，请确认是否有权限！")
                    return
                update_sql = f"""
                    UPDATE `文件资料表`
                    SET `存储路径` = '\\\\{update_file_full}'
                    WHERE `成品编码` = '{finished_product_code}' AND `类型`='原价'
                """
                search_db.writeSqlTable(update_sql)
                search_db.close()  # 关闭数据库链接
                QMessageBox.about(self, "提示", "原价文件信息更新成功!")
            elif temp1 == QMessageBox.No:
                return

    #  打开文件对话框
    def slot_btn_chooseMutiFile(self,choice_file_type):
        # fileName_choose, filetype = QFileDialog.getOpenFileName(self,"文件选择",os.getcwd(),
        #                    "All Files (*);;PDF Files (*.pdf);;Excel Files (*.xlsx);;Excel 97-2003 Files (*.xls)")
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,"文件选择",os.getcwd(),choice_file_type)
        if fileName_choose == "":
            print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        # print(fileName_choose)
        # print("文件筛选器类型: ", filetype)

        return fileName_choose

    #  查看文档——函数
    def view_document(self):
        finished_product_code = self.tableWidget_1.item(0,1).text() #  获取当前显示的成品编码
        # print(f"当前显示的成品编码：{finished_product_code}")
        search_db = ObjectSearch()  # 实例化数据库查询类
        # finished_product_code = search_db.id_to_productionNumber(int(self.ID))  # 通过ID号获取成品编码
        query_criteria_document = f"成品编码 ='{finished_product_code}' AND 类型 = '文档'"
        temp_document = search_db.get_price2("文件资料表",query_criteria_document)  #  根据成品编码，查询文件资料表中是否存在对应的文档信息
        search_db.close()  # 关闭数据库链接
        if len(temp_document) != 0:
            document_path = temp_document[0][3]
            (filepath, tempfilename) = os.path.split(document_path)
            # (filename, extension) = os.path.splitext(tempfilename)
            # print(f"文件路径：{filepath}")
            if os.path.exists(filepath):    #  判断文件夹是否存在
                os.startfile(filepath)  #  打开文件夹

    #  主表 双击单元格 信号 函数
    def tableWidget_1_cellDoubleClicked_func(self, row, column):
        select_DB = ObjectSearch()

        if column == 2:
            if self.usertype >= 20 and self.usertype < 30:  # 技术部账号
                return
            items_list_customer = select_DB.get_field_value('原价明细总表_new', '客户名称')  # 获取所有的客户名称
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值
            # print(old_value)
            # 在单元格中添加一个QComboBox下拉框
            com_customer = QComboBox()
            com_customer.addItems(items_list_customer)
            # com_customer.setCurrentIndex(-1)
            com_customer.setCurrentText(old_value)   # 设置当前项为原来的值
            self.tableWidget_1.setCellWidget(row, column, com_customer)

        elif column == 4:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_productMix = select_DB.get_field_value('产品参数_产品结构表', '名称')  # 获取所有的分类
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_productMix = QComboBox()
            # com_productMix.setStyleSheet('QComboBox{margin:3px}')
            com_productMix.addItems(items_list_productMix)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_productMix.setCurrentIndex(-1)
            else:
                com_productMix.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_productMix)

        elif column == 5:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_lenght = select_DB.get_field_value('产品参数_长度表', '长度值')  # 获取所有的重要性
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_lenght = QComboBox()
            com_lenght.addItems(items_list_lenght)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_lenght.setCurrentIndex(-1)
            else:
                com_lenght.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_lenght)

        elif column == 6:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_ShaftOuterDiameter = select_DB.get_field_value('产品参数_轴芯外径表', '外径值')  # 获取所有的规格
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_ShaftOuterDiameter = QComboBox()
            com_ShaftOuterDiameter.addItems(items_list_ShaftOuterDiameter)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_ShaftOuterDiameter.setCurrentIndex(-1)
            else:
                com_ShaftOuterDiameter.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_ShaftOuterDiameter)


        elif column == 7:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_RubberOuterDiameter = select_DB.get_field_value('产品参数_橡胶外径表', '外径值')  # 获取所有的材质
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_RubberOuterDiameter = QComboBox()
            com_RubberOuterDiameter.addItems(items_list_RubberOuterDiameter)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_RubberOuterDiameter.setCurrentIndex(-1)
            else:
                com_RubberOuterDiameter.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_RubberOuterDiameter)

        elif column == 8:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_commonDifference = select_DB.get_field_value('产品参数_公差表', '公差值')  # 获取所有的材质
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_commonDifference = QComboBox()
            com_commonDifference.addItems(items_list_commonDifference)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_commonDifference.setCurrentIndex(-1)
            else:
                com_commonDifference.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_commonDifference)

        elif column == 9:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_amplitude = select_DB.get_field_value('产品参数_振幅表', '振幅值')  # 获取所有的材质
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_amplitude = QComboBox()
            com_amplitude.addItems(items_list_amplitude)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_amplitude.setCurrentIndex(-1)
            else:
                com_amplitude.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_amplitude)

        elif column == 10:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_laserInSpection = ['是', '否']
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_laserInSpection = QComboBox()
            com_laserInSpection.addItems(items_list_laserInSpection)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_laserInSpection.setCurrentIndex(-1)
            else:
                com_laserInSpection.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_laserInSpection)

        elif column == 11:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_polish = ['是', '否']
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_polish = QComboBox()
            com_polish.addItems(items_list_polish)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_polish.setCurrentIndex(-1)
            else:
                com_polish.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_polish)

        elif column == 12:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_pressInMode = select_DB.get_field_value('产品参数_压入方式表', '压入方式')  # 获取所有的材质
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_pressInMode = QComboBox()
            com_pressInMode.addItems(items_list_pressInMode)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_pressInMode.setCurrentIndex(-1)
            else:
                com_pressInMode.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_pressInMode)

        elif column == 13:
            if self.usertype >= 10 and self.usertype < 20:  # 资材账号
                return

            items_list_otherCategories = select_DB.get_field_value('产品参数_其它分类表', '分类名称')  # 获取所有的材质
            old_value = self.tableWidget_1.item(row,column).text()  # 修改前的值

            # 在单元格中添加一个QComboBox下拉框
            com_otherCategories = QComboBox()
            com_otherCategories.addItems(items_list_otherCategories)
            if old_value == '': # 如果修改前值为空，则下拉框默认值为空，否则默认值为修改前的值
                com_otherCategories.setCurrentIndex(-1)
            else:
                com_otherCategories.setCurrentText(old_value)
            self.tableWidget_1.setCellWidget(row, column, com_otherCategories)

    # 主表 单元格改变 信号 函数
    def tableWidget_1_currentCellChanged_func(self, currentRow, currentColumn, previousRow, previousColumn):
        select_DB = ObjectSearch()

        if previousColumn == 2:
            try:
                #  获取4列当前的值
                customer = self.tableWidget_1.cellWidget(previousRow,previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `客户名称` = '{customer}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")

                return

        elif previousColumn == 4:
            try:
                #  获取4列当前的值
                productMix = self.tableWidget_1.cellWidget(previousRow,previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `产品结构` = '{productMix}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 5:
            try:
                lenght = self.tableWidget_1.cellWidget(previousRow,previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `长度` = '{lenght}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 6:
            try:
                #  获取列当前的值
                ShaftOuterDiameter = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号
                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `轴芯外径` = '{ShaftOuterDiameter}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 7:
            try:
                #  获取列当前的值
                rubberOuterDiameter = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号
                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `橡胶外径` = '{rubberOuterDiameter}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 8:
            try:
                #  获取列当前的值
                commonDifference = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `公差` = '{commonDifference}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 9:
            try:
                #  获取列当前的值
                amplitude = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `振幅` = '{amplitude}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 10:
            try:
                #  获取列当前的值
                laserInSpection = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `激光` = '{laserInSpection}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 11:
            try:
                #  获取列当前的值
                polish = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `研磨` = '{polish}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 12:
            try:
                #  获取列当前的值
                pressInMode = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `压入方式` = '{pressInMode}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return

        elif previousColumn == 13:
            try:
                #  获取列当前的值
                otherCategories = self.tableWidget_1.cellWidget(previousRow, previousColumn).currentText()
                value_number = self.tableWidget_1.item(previousRow, 0).text()  # 当前原价单的ID号

                # 生成 mysql UPDATE 语句
                renew_sql = f"""
                UPDATE `原价明细总表_new`
                SET `其它分类` = '{otherCategories}'
                WHERE `ID` = '{value_number}'
                """
            except AttributeError:
                print(f"单元格没有添加下拉框！取值出错！")
                return
        else:
            return

        # print(f"SQL语句2：{renew_sql}")
        select_DB.execute_sql(renew_sql)

    #  更新数据-主表
    def table_update_price(self):
        row_select = self.tableWidget_1.selectedItems()
        # print(row_select)
        if len(row_select) == 0:
            return
        else:
            result_value = row_select[0].text() # 修改后的值
            # print(f"修改后的值是：{result_value}")

        current_row = self.tableWidget_1.currentRow()   # 修改的行号
        # print(f"当前行：{current_row}")
        current_column = self.tableWidget_1.currentColumn() # 修改的列号
        # print(f"当前列：{current_column}")

        value_number = self.tableWidget_1.item(current_row,0).text()    # 修改行的序号
        # value_product_number = self.tableWidget_1.item(current_row,1).text()    # 修改行的成品编码

        # if current_column == 2:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `客户名称` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        if current_column == 3:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `品名` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """

        # elif current_column == 4:
        #     print(f"程序执行到此处")
        #     select_DB = ObjectSearch()
        #     items_list_productMix = select_DB.get_field_value('产品参数_产品结构表', '名称')  # 获取所有的分类
        #     select_DB.close()
        #     com_productMix = QComboBox()
        #     # old_productMix = self.tableWidget_1.item(current_row,current_column).text() # 保存修改前的值
        #     com_productMix.addItems(items_list_productMix)
        #     self.tableWidget_1.setCellWidget(current_row,current_column,com_productMix)
        #     result_value = com_productMix.currentText()
        #
        #
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `产品结构` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 5:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `长度` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 6:
        #     # 生成 mysql UPDATE 语句
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `轴芯外径` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 7:
        #     # 生成 mysql UPDATE 语句
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `橡胶外径` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 8:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `公差` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 9:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `振幅` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 10:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `激光` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 11:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `研磨` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 12:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `压入方式` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        # elif current_column == 13:
        #     renew_sql = f"""
        #     UPDATE `原价明细总表_new`
        #     SET `其它分类` = '{result_value}'
        #     WHERE `ID` = '{value_number}'
        #     """
        elif current_column == 14:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `月产量` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 15:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `固定费用` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 16:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `运费` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 17:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `管理费` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 18:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `材料费` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 19:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `加工费` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 20:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `包装费` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 21:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `总金额` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 22:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `生效日期` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 23:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `作成日期` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 24:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `作成` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 25:
            renew_sql = f"""
            UPDATE `原价明细总表_new`
            SET `确认` = '{result_value}'
            WHERE `ID` = '{value_number}'
            """
        elif current_column == 26:
            return

        mysql = ObjectSearch()
        # print(f"SQL语句：{renew_sql}")
        mysql.execute_sql(renew_sql)

    #  tablewidget的 【cellDoubleClicked】 信号的函数-备注项的修改
    def edit_widget_fun(self,row,column):
        # print(self.tableWidget_1.item(row,column).text())

        row_select = self.tableWidget_1.selectedItems()
        # print(row_select)
        if len(row_select) == 0:
            return
        else:
            result_value = row_select[0].text()  # 修改后的值
            # print(f"修改后的值是：{result_value}")

        current_row = self.tableWidget_1.currentRow()  # 修改的行号
        # print(f"当前行：{current_row}")
        # current_column = self.tableWidget_1.currentColumn()  # 修改的列号
        # print(f"当前列：{current_column}")

        # result_value = self.tableWidget_1.item(row,column).text()

        value_number = self.tableWidget_1.item(current_row, 0).text()  # 修改行的序号(ID)

        if column == 26:
            self.editwidget = EditWidget(value_number,self.tableWidget_1.item(row, column).text())
            self.editwidget.show()
            # temp_string = self.editwidget.pushButton_save_fun()

    #  更新数据-材料费
    def table_update_material(self):
        row_select = self.tableWidget_2.selectedItems()
        # print(row_select)
        if len(row_select) == 0:
            return
        else:
            result_value = row_select[0].text() # 修改后的值
            # print(f"修改后的值是：{result_value}")

        current_row = self.tableWidget_2.currentRow()   # 修改的行号
        # print(f"当前行：{current_row}")
        current_column = self.tableWidget_2.currentColumn() # 修改的列号
        # print(f"当前列：{current_column}")

        value_number = self.tableWidget_2.item(current_row,0).text()    # 修改行的序号
        value_product_number = self.tableWidget_2.item(current_row,1).text()    # 修改行的成品编码

        if current_column == 3:
            renew_sql = f"""
            UPDATE `材料费`
            SET `材料名称` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 4:
            renew_sql = f"""
            UPDATE `材料费`
            SET `料号` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 5:
            renew_sql = f"""
            UPDATE `材料费`
            SET `供应商` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 6:
            renew_sql = f"""
            UPDATE `材料费`
            SET `单价` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 7:
            renew_sql = f"""
            UPDATE `材料费`
            SET `用量` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 8:
            renew_sql = f"""
            UPDATE `材料费`
            SET `每模用量` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 9:
            renew_sql = f"""
            UPDATE `材料费`
            SET `每模出数` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 10:
            renew_sql = f"""
            UPDATE `材料费`
            SET `切割个数` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 11:
            renew_sql = f"""
            UPDATE `材料费`
            SET `金额` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        mysql = ObjectSearch()
        # print(f"SQL语句：{renew_sql}")
        mysql.execute_sql(renew_sql)

    #  更新数据-加工费
    def table_update_processing(self):
        row_select = self.tableWidget_3.selectedItems()
        # print(row_select)
        if len(row_select) == 0:
            return
        else:
            result_value = row_select[0].text() # 修改后的值
            # print(f"修改后的值是：{result_value}")

        current_row = self.tableWidget_3.currentRow()   # 修改的行号
        # print(f"当前行：{current_row}")
        current_column = self.tableWidget_3.currentColumn() # 修改的列号
        # print(f"当前列：{current_column}")

        value_number = self.tableWidget_3.item(current_row,0).text()    # 修改行的序号
        value_product_number = self.tableWidget_3.item(current_row,1).text()    # 修改行的成品编码

        if current_column == 3:
            renew_sql = f"""
            UPDATE `加工费`
            SET `工序名称` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 4:
            renew_sql = f"""
            UPDATE `加工费`
            SET `工序代码` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 5:
            renew_sql = f"""
            UPDATE `加工费`
            SET `工程单价` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 6:
            renew_sql = f"""
            UPDATE `加工费`
            SET `工数` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 7:
            renew_sql = f"""
            UPDATE `加工费`
            SET `切割数` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 8:
            renew_sql = f"""
            UPDATE `加工费`
            SET `用量` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 9:
            renew_sql = f"""
            UPDATE `加工费`
            SET `计算方式` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 10:
            renew_sql = f"""
            UPDATE `加工费`
            SET `金额` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """

        mysql = ObjectSearch()
        # print(f"SQL语句：{renew_sql}")
        mysql.execute_sql(renew_sql)

    #  更新数据-包装费
    def table_update_packing(self):
        row_select = self.tableWidget_4.selectedItems()
        # print(row_select)
        if len(row_select) == 0:
            return
        else:
            result_value = row_select[0].text()  # 修改后的值
            # print(f"修改后的值是：{result_value}")

        current_row = self.tableWidget_4.currentRow()  # 修改的行号
        # print(f"当前行：{current_row}")
        current_column = self.tableWidget_4.currentColumn()  # 修改的列号
        # print(f"当前列：{current_column}")

        value_number = self.tableWidget_4.item(current_row, 0).text()  # 修改行的序号
        value_product_number = self.tableWidget_4.item(current_row, 1).text()  # 修改行的成品编码

        if current_column == 3:
            renew_sql = f"""
            UPDATE `包装费`
            SET `料号` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 4:
            renew_sql = f"""
            UPDATE `包装费`
            SET `包装名称` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 5:
            renew_sql = f"""
            UPDATE `包装费`
            SET `单价` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 6:
            renew_sql = f"""
            UPDATE `包装费`
            SET `用量` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 7:
            renew_sql = f"""
            UPDATE `包装费`
            SET `包装数` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 8:
            renew_sql = f"""
            UPDATE `包装费`
            SET `回收否` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 9:
            renew_sql = f"""
            UPDATE `包装费`
            SET `计算方式` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        elif current_column == 10:
            renew_sql = f"""
            UPDATE `包装费`
            SET `金额` = '{result_value}'
            WHERE `序号` = '{value_number}' AND `成品编码` = '{value_product_number}'
            """
        mysql = ObjectSearch()
        # print(f"SQL语句：{renew_sql}")
        mysql.execute_sql(renew_sql)

    #  输出EXCEL文件
    def output_excel(self):
        # print(f"当前的ID号：{self.ID}")
        temp_id = self.tableWidget_1.item(0,0).text()
        search_db = ObjectSearch()  # 实例化数据库查询类
        general_table_data_1 = list(search_db.get_price1(f" ID = {temp_id}"))  # 按ID在数据库中查询原价总表数据
        finished_product_code = search_db.id_to_productionNumber(int(temp_id))  # 通过ID号获取成品编码
        general_table_data = list(general_table_data_1[0])
        # del general_table_data[7]
        for x in range(len(general_table_data)):    # 处理列表中的None，转换成''
            if general_table_data[x] is None:
                general_table_data[x] = ''
        # print(f"原价总表数据：{general_table_data}")

        select_sql_where_material = f" 成品编码 = '{finished_product_code}' "  # 查询条件
        material_list_original = search_db.get_price2("`材料费`", select_sql_where_material)  # 获取材料表的相关数据
        material_list = []
        for x in range(len(material_list_original)):  # 处理列表中的None,转换成''
            temp_1 = list(material_list_original[x])
            for y in range(len(temp_1)):
                if temp_1[y] is None:
                    temp_1[y] = ''
            material_list.append(temp_1)
        # print(f"材料表的数据：{material_list}")

        select_sql_where_processing = f" 成品编码 = '{finished_product_code}' ORDER BY `成品编码`, `序号` "  # 查询条件
        processing_list_original = search_db.get_price2("`加工费`", select_sql_where_processing)  # 获取加工表的相关数据
        processing_list = []
        for x in range(len(processing_list_original)):  # 处理列表中的None,转换成''
            temp_2 = list(processing_list_original[x])
            for y in range(len(temp_2)):
                if temp_2[y] is None:
                    temp_2[y] = ''
            processing_list.append(temp_2)
        # print(f"加工数据：{processing_list}")

        select_sql_where_packing = f" 成品编码 = '{finished_product_code}' "  # 查询条件
        packing_list_original = search_db.get_price2("`包装费`", select_sql_where_packing)  # 获取包装表的相关数据
        packing_list = []
        for x in range(len(packing_list_original)):  # 处理列表中的None,转换成''
            temp_3 = list(packing_list_original[x])
            for y in range(len(temp_3)):
                if temp_3[y] is None:
                    temp_3[y] = ''
            packing_list.append(temp_3)
        # print(f"包装费数据：{packing_list}")

        search_db.close()

        out_name = f"{finished_product_code}.xlsx"
        # print(out_name)
        #  获取桌面的路径
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        temp_str = winreg.QueryValueEx(key, 'Desktop')[0]
        # print(f"桌面路径：{temp_str}")

        file_path_name = f"{temp_str}\{out_name}"
        excel_Object = OutExcel(file_path_name)
        # print(f"输出的文件全名：{file_path_name}")
        excel_Object.output_excel(file_path_name, general_table_data, material_list, processing_list, packing_list)

    #  定义函数：根据传入的用户类型，确定原价单显示界面的功能是否可用
    def settingWidgetAvailable(self,usertype):
        if usertype >= 10 and usertype < 20:    # 资材账号
            for x in range(4,14):   # 设置分类的10列不能修改
                self.tableWidget_1.setItemDelegateForColumn(x, EmptyDelegate(self))

        elif usertype >= 20 and usertype < 30:    # 技术部账号
            self.btn_updateYuanJia.hide()   #  隐藏【上传原价】按钮

            # print(f"用户类型为【技术】识别码：{usertype}")
            number_list = [0,1,2,3,14,15,16,17,18,19,20,21,22,23,24,25,26]
            # 设置总表除了分类数据外其他列不能更改
            for i in number_list:
                self.tableWidget_1.setItemDelegateForColumn(i, EmptyDelegate(self))

            #  设置表格不能编辑
            self.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑
            self.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑
            self.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑

            #  断开 QTableWidget单元格双击信号与槽函数的连接
            self.tableWidget_2.itemChanged.disconnect(self.table_update_material)    # 断开信号 材料表——单元格修改后自动触发动作
            self.tableWidget_3.itemChanged.disconnect(self.table_update_processing)    # 断开信号 加工表——单元格修改后自动触发动作
            self.tableWidget_4.itemChanged.disconnect(self.table_update_packing)    # 断开信号 包装表——单元格修改后自动触发动作
            self.tableWidget_1.cellDoubleClicked.disconnect(self.edit_widget_fun)  # 断开信号 总表——备注单元格双击触发动作


        elif usertype >= 30 and usertype < 40:  # 品质、生产账号，只具有查看功能
            # print(f"用户类型为【品质、生产】识别码：{usertype}")

            self.pushButton_update_image.hide() #  隐藏【上传图片】按钮
            self.pushButton_update_document.hide()  # 隐藏【上传文档】按钮
            self.btn_updateYuanJia.hide()   #  隐藏【上传原价】按钮

            #  设置表格不能编辑
            self.tableWidget_1.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑
            self.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑
            self.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑
            self.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格用户不能编辑

            #  断开 QTableWidget单元格双击信号与槽函数的连接
            self.tableWidget_1.itemChanged.disconnect(self.table_update_price) # 断开信号 总表——单元格修改后自动触发动作
            self.tableWidget_2.itemChanged.disconnect(self.table_update_material)    # 断开信号 材料表——单元格修改后自动触发动作
            self.tableWidget_3.itemChanged.disconnect(self.table_update_processing)    # 断开信号 加工表——单元格修改后自动触发动作
            self.tableWidget_4.itemChanged.disconnect(self.table_update_packing)    # 断开信号 包装表——单元格修改后自动触发动作

            self.tableWidget_1.cellDoubleClicked.disconnect(self.edit_widget_fun)  # 断开信号 总表——备注单元格双击触发动作
            self.tableWidget_1.currentCellChanged.disconnect(self.tableWidget_1_currentCellChanged_func)  # 断开信号  单元格改变信号
            self.tableWidget_1.cellDoubleClicked.disconnect(self.tableWidget_1_cellDoubleClicked_func)  # 断开信号  单元格双击信号

            #  隐藏价格信息
            for i in range(15,22):  # 总表
                self.tableWidget_1.setColumnHidden(i,True)
            self.tableWidget_2.setColumnHidden(6,True)
            self.tableWidget_2.setColumnHidden(11,True)
            self.tableWidget_3.setColumnHidden(5,True)
            self.tableWidget_3.setColumnHidden(10,True)
            self.tableWidget_4.setColumnHidden(5,True)
            self.tableWidget_4.setColumnHidden(10,True)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        self.signal.emit()