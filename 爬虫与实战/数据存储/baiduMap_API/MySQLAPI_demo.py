'''
python连接mysqldemo
1.获取数据库 pymysql(python3)    Mysqldb(python2)
2.获取记录
3.增加记录
4.修改记录
5.删除记录
'''

__author__ = "RyanWu"


import pymysql

class MysqlDemo(object):
    # 设置数据库的连接参数，默认编码类型为utf-8，参数为字符串
    def __init__(self, host, username, password, dbname):
        self.conn = pymysql.connect(host, username, password, dbname, port=3306, charset='utf8')
        self.cursor = self.conn.cursor()

    # 获取数据 此处传值为sql语句
    def get_all(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return False

    # 获取单条数据
    def get_one(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            return False

    # 插入一条记录数据  tableName   data(dict)
    def insert(self, table_name, data):
        if len(data.keys()) == 1:

            sql = 'insert into {}{} VALUES '.format(table_name, data.keys()[0]).replace("'", '')+'("{}")'.format(data.values()[0])
        else:
            sql = 'insert into {}{} VALUES'.format(table_name, tuple(data.keys())).replace("'", '')+str('{}'.format(tuple(data.values())))
            print(sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            # 返回插入后的id
            return self.cursor.lastrowid
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False

    # 执行一条sql语句
    def query(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    # 删除一条记录    tablename   restrication_str
    def delete(self):
        sql = ''
        pass

    # 删除表
    def delete_tab(self, table_name):
        pass

    # 格式化表  trnacete
    def format_tab(self, table_name):
        sql = 'trnacate table {}'.format(table_name)
        pass


    # 更新记录 tableName    data(字典)    restrication_str
    def update(self, table_name, data, restrication_str):
        data_str = ''
        for item in data.items():
            data_str += '{}="{}",'.format(item[0], item[1])
        values = data_str[:-1]
        sql = 'update {} set {} WHERE {}'.format(table_name, values, restrication_str)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False
# dicts = {
#     'name':'Tuling',
#     'age':18,
#     'sex':'M'
# }
#
# data_str = ''
# for item in dicts.items():
#     data_str += '{}="{}",'.format(item[0], item[1])
#     # print(data_str)
#     values = data_str[:-1]
#     # print(values)
# print(dicts.keys()[0])

