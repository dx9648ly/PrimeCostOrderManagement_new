# -*- coding: utf-8 -*-
from decimal import Decimal

import pymysql

class ObjectSearch():
    def __init__(self,column=None,searchKey=None):
        """
        注意：column 和 searchKey 是对应关系。
        :param column: 列名——————只能为‘ID'或者‘成品编码’
        :param searchKey: 搜索关键字—————— 如果 column 为‘ID’，则可以输入数字。否则必须是字符串
        """
        # if column != "ID":
        #     if column != "成品编码":
        #         print("参数输入错误，column只能为\"ID\"或\"成品编码\"")
        #         return
        self.searchKey = searchKey
        self.column = column
        # 数据库连接
        self.db = pymysql.connect(host='192.168.20.223',
                             port=3306,
                             user='root',
                             password='WF2021rootADMIN#',
                             database='wingfung-originalprice')
        # 获取游标
        self.cursor = self.db.cursor()


    #从ID号获取对应的成品编码
    def id_to_productionNumber(self,id):
        id = int(id)
        temp_select_sql = f"""
        SELECT 成品编码
        FROM `原价明细总表_new`
        WHERE ID = {id}
        """
        self.cursor.execute(temp_select_sql)
        temp_result = self.cursor.fetchone()
        # print(temp_result[0])
        return temp_result[0]

    #  获取字段值
    def get_field_value(self,tableName,fieldName):
        temp_select_sql = f"""
        SELECT {fieldName}
        FROM `{tableName}`
        GROUP BY {fieldName}
        """
        self.cursor.execute(temp_select_sql)
        result = self.cursor.fetchall()
        temp = []

        for _ in result:    #嵌套列表展开
            temp += _

        return  temp


    #获取所有的ID号
    def get_id(self):
        search_sql_id = """
        SELECT ID
        FROM `原价明细总表_new`
        GROUP BY ID
        """
        self.cursor.execute(search_sql_id)
        result = self.cursor.fetchall()
        temp = []

        for _ in result:    #嵌套列表展开
            temp += _

        return  temp

    #获取所有的成品编码
    def get_fpc(self):
        search_sql = """
        SELECT 成品编码
        FROM `原价明细总表_new`
        GROUP BY 成品编码
        """
        self.cursor.execute(search_sql)
        result = self.cursor.fetchall()
        temp = []

        for _ in result:    #嵌套列表展开
            temp += _

        return temp

    #  多条件查询总表数据
    def get_price1(self,select_str=None):
        '''
        多条件查询【原价明细总表】
        :param select_str: 查询条件
        :return: 返回包含所有字段的查询结果
        '''
        if select_str is None or select_str == '':
            search_sql_price = f"""
            SELECT *
            FROM `原价明细总表_new`
            """
        else:
            search_sql_price = f"""
            SELECT *
            FROM `原价明细总表_new`
            WHERE {select_str}
            """

        self.cursor.execute(search_sql_price)

        result = self.cursor.fetchall()
        return result

    #  多条件查询总表数据_new
    def get_price_new(self,select_str=None):
        '''
        多条件查询【原价明细总表】
        :param select_str: 查询条件
        :return: 返回包含所有字段的查询结果
        '''
        if select_str is None or select_str == '':
            search_sql_price = f"""
            SELECT *
            FROM `原价明细总表_new`
            """
        else:
            search_sql_price = f"""
            SELECT *
            FROM `原价明细总表_new`
            WHERE {select_str}
            """

        self.cursor.execute(search_sql_price)

        result = self.cursor.fetchall()
        return result

    #  自定义条件查询数据
    def get_price2(self,tableName,select_str):
        '''
        自定义条件查询记录
        :param tableName: 表名
        :param select_str: 查询条件
        :return: 返回包含所有字段的查询结果
        '''
        if tableName is None or select_str is None:
            return
        else:
            search_sql_price = f"""
            SELECT *
            FROM {tableName}
            WHERE {select_str}
            """

        self.cursor.execute(search_sql_price)

        result = self.cursor.fetchall()
        return result

    #  执行自定义语句
    def search(self,selectString):
        '''
        直接按自定义的SQL语句执行操作
        :param selectString: 自定义的SQL语句
        :return: 返回执行结果
        '''
        if selectString is not None:
            self.cursor.execute(selectString)

            result = self.cursor.fetchall()

            return result

    #  获取数据库表中指定字段的值，并把重复值去掉
    def getFieldValue(self,tableName,fieldName):
        """
        获取数据库表中指定字段的值，并把重复值去掉
        :param tableName: 表名
        :param fieldName: 字段名
        :return: 包含指定字段所有不重复值的_列表
        """
        search_sql = f"""
            SELECT {fieldName}
            FROM {tableName}
            GROUP BY {fieldName}
        """

        self.cursor.execute(search_sql)
        result = self.cursor.fetchall()
        temp = []

        for _ in result:  # 嵌套列表展开
            temp += _
        temp = set(temp)    # 去掉重复的值,返回的类型为set
        temp = list(temp)   # 把set类型转换成list
        temp.sort() # 排序
        return temp

    #  获取数据库表中指定字段的值
    def getFieldValue1(self,tableName,fieldName,conditionStr):
        """
        获取数据库表中指定字段的值，同时值按字段名排序
        :param tableName: 表名
        :param fieldName: 字段名
        :param conditionStr: 查询条件
        :return: 包含表中指定字段的排序后的所有值_列表
        """
        search_sql = f"""
            SELECT {fieldName}
            FROM {tableName}
            WHERE {conditionStr}
            GROUP BY {fieldName}
        """

        self.cursor.execute(search_sql)
        result = self.cursor.fetchall()
        temp = []

        for _ in result:  # 嵌套列表展开
            temp += _
        # temp = set(temp)    # 去掉重复的值

        return temp

    #  按条件获取数据库指定表的值
    def getFieldValue2(self,tableName,conditionStr):
        """
        按条件获取数据库指定表的值
        :param tableName: 表名
        :param fieldName: 字段名
        :param conditionStr: 查询条件
        :return: 包含表中指定字段的排序后的所有值_列表
        """
        search_sql = f"""
            SELECT *
            FROM {tableName}
            WHERE {conditionStr}
        """

        self.cursor.execute(search_sql)
        result = self.cursor.fetchall()
        temp = []

        for _ in result:  # 嵌套列表展开
            temp += _
        # temp = set(temp)    # 去掉重复的值

        return temp

    #获取数据库字段名
    def get_fieldName(self,tableName):
        """
        获取数据库指定表的字段名列表
        :param tableName: 表名
        :return: 包含所有字段名称的列表
        """
        search_sql = """
        SELECT *
        FROM {}
        LIMIT 1
        """.format(tableName)

        # print(search_sql)
        self.cursor.execute(search_sql)  #随便查询一条数据
        temp_result = self.cursor.fetchall()
        col_result = self.cursor.description    # 获取查询结果的字段描述

        fieldName = []
        for i in range(len(col_result)):
            fieldName.append(col_result[i][0])  #   获取字段名，追加到列表中

        return fieldName

    #  把单条记录写入数据库、所有字段
    def executeInsertIDback(self,tableName,sqlstring):
        sql = f"""insert into {tableName} values{sqlstring}"""
        try:
            # print(f"SQL语句：\n{sql}")
            self.cursor.execute(sql)
            self.db.commit()
            the_id = int(self.cursor.lastrowid)
            return the_id
        except:
            print("表-插入数据异常")
            self.db.rollback()
            return False
        # finally:
        #     self.db.close()  # 关闭数据库连接

    #  写数据库指定表、指定字段
    def writeSqlTable(self,sqlstring):
        try:
            self.cursor.execute(sqlstring)
            self.db.commit()
            the_id = int(self.cursor.lastrowid)
            return the_id
        except:
            self.db.rollback()
            return False
        # finally:
        #     self.db.close()  # 关闭数据库连接

    #  多条记录插入数据库-材料表
    def insertItemsMaterial(self,data):
        """
        插入多条记录
        :return:
        """
        sql_str = f"""insert into `材料费` values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            self.cursor.executemany(sql_str,data)
            # self.cursor.mogrify(sql_str)
            self.db.commit()
            print(f"材料表数据写入成功！")
        except Exception as e:
            print("材料表-插入数据异常")
            self.db.rollback()

    #  多条记录插入数据库-加工表
    def insertItemsProcessing(self,datas):
        """
        插入多条记录
        :return:
        """
        sql_str = f"""insert into `加工费` values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        try:
            self.cursor.executemany(sql_str, datas)
            self.cursor.mogrify(sql_str)
            self.db.commit()
            print(f"加工表数据写入成功！")
        except Exception as e:
            print("加工表-插入数据异常")
            self.db.rollback()

    #  多条记录插入数据库-包装表
    def insertItemsPacking(self,datas):
        """
        插入多条记录
        :return:
        """
        sql_str = f"""insert into `包装费` values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        try:
            self.cursor.executemany(sql_str, datas)
            self.db.commit()
            print(f"包装表数据写入成功！")
        except Exception as e:
            print("包装表-插入数据异常")
            self.db.rollback()

    #  直接执行SQL语句
    def execute_sql(self,sqlstring):
        """
        直接执行传入的语句
        :param sqlstring:
        :return:
        """
        try:
            self.cursor.execute(sqlstring)
            self.db.commit()
        except Exception as e:
            print("语句执行异常!")
            self.db.rollback()
        finally:
            self.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        游标对象，数据库关闭
        :param exc_type:异常类型
        :param exc_val:异常值
        :param exc_tb:异常的错误栈信息
        :return:
        """
        self.cursor.close()
        self.db.close()

    def close(self):
        self.cursor.close()
        self.db.close()

    # 检测数据库的连接状态
    def state_connection(self):
        try:
            self.close()
            self.db.ping()  # 采用连接对象的ping()函数检测连接状态
            print('连接正常')
        # 出现异常重新连接
        except:
            print("连接已经关闭！")


if __name__ == '__main__':
    # values = ObjectSearch('成品编码','60201T-001-1')
    # values = ObjectSearch(searchKey='60201T-001-1',column='成品编码')
    # values = ObjectSearch(searchKey=10,column='ID')
    values = ObjectSearch()

    # values.get_price()
    # values.get_material()
    # values.get_procedure()
    # values.get_packing()

    # print(values.get_price())
    # # print(type(values.get_price()))
    # print(values.get_material())
    # # print(type(values.get_material()))
    # print(values.get_procedure())
    # # print(type(values.get_procedure()))
    # # print(len(values.get_procedure()))
    # print(values.get_packing())
    # # print(type(values.get_packing()))

    # values.close()
    #
    #
    # values1=ObjectSearch("ID")
    # print(values1.get_id())

    # values.close()
    # values.state_connection()

    a = ['6666666601', 'CHINA', '8888888801', 'B', 'Φ5', '非常重要', 10000, Decimal('1.000'), Decimal('1.000'),
     Decimal('1.000'), Decimal('0.262'), Decimal('0.325'), Decimal('0.133'), Decimal('3.720'), '2021-04-20',
     '2021-04-20', '测试', '测试', '1、测试\n2、测试2']

    aa = [('1', '6666666608', '8888888808', '10699R-016', '2槽塑胶垫片', '板仓', '1.000', '1.000', None, None, None, '1.000'), ('2', '6666666608', '8888888808', '20201R-686', 'K60EG54E(S)', '建设', '41.000', '1.000', '1.000', '320', '1', '0.128')]
    aa1 = ('1', '6666666608', '8888888808', '10699R-016', '2槽塑胶垫片', '板仓', '1.000', '1.000', None, None, None, '1.000')

    bb = [('1', '999-999-003', '111-111-003', '20202R-082', 'SH851U', '建设', '85.000', '1.000', '1.000', '324', '1', '0.262'), ('2', '999-999-003', '111-111-003', '10199T-028', '别针-PIN', '东京兼', '1.000', '1.000', None, None, None, '1.000')]

    cc = [('a', '999-999-039', '111-111-039', '位置检查', 'WZJC', '52.000', '200', None, None, '52.000/200', '0.260'),
     ('b', '999-999-039', '111-111-039', '切割', 'QG', '66.000', '200', None, None, '66.000/200', '0.330'),
     ('c', '999-999-039', '111-111-039', '加温干燥', 'JWGZ', '52.000', '200', None, None, '52.000/200', '0.260'),
     ('d', '999-999-039', '111-111-039', '组装', 'ZZ', '52.000', '200', None, None, '52.000/200', '0.260'),
     ('e', '999-999-039', '111-111-039', '手工压入轴承', 'SGYR-ZC', '52.000', '200', None, None, '52.000/200', '0.260'),
     ('f', '999-999-039', '111-111-039', '冲压', 'CY', '98.000', '200', None, None, '98.000/200', '0.490'),
     ('g', '999-999-039', '111-111-039', '检查轴承转动', 'JCZCZD', '52.000', '200', None, None, '52.000/200', '0.260'),
     ('h', '999-999-039', '111-111-039', '研磨芯清洗', 'YMXQX', '52.000', '200', None, None, '52.000/200', '0.260')]

    # values.insertItemsMaterial(bb)
    # ss = values.get_price2("materialcost","`成品编码` = '60201T-001-1'")
    # print(ss)
    # values.insertItemsProcessing(cc)

    a = values.search("SELECT * FROM `原价明细总表_new`")
    print(len(a))
    values.close()