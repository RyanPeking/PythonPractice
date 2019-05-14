'''
数据存储之mysql
Ubantu环境安装mysql
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmysqlclient-dev

登录数据库：
    sudo mysql -u 用户名 -p

#rhel7环境安装mysql数据库
    http://www.cnblogs.com/guozhiping/p/7684134.html

mysql数据库远程连通：
    1.修改/etc/mysql/my.conf
        找到bind-address = 127.0.0.1 这一行，将这一行注释
        或者：将这一行改为bind-address = 0.0.0.0

    2.让root用户支持远程连接mysql数据库
        mysql -u root -p
        grant all privileges on *.* to root@'%' identified by "yourpassword" with grant option;
        flush privileges

    3.rhel7中防火墙允许mysql服务通过
        firewall-cmd --permanent --add-service=mysql
        firewall-cmd --reload

Python操作mysql
    pip install pymysql

'''

# Python操作mysql创建数据表
import pymysql

# try:
#     # 获取一个数据库连接，注意：如果是utf-8类型，需要定制数据库
#     # 打开数据库连接
#     con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='ceshi', port=3306)
#     # 创建游标，对数据库进行操作，使用cursor()方法
#     # print(con)
#     cur = con.cursor()
#     # 使用execute（）执行sql语句
#     # cur.execute('DROP TABLES IF EXISTS BJTLXY')
#     # 使用预处理语句创建表
#     sql = """CREATE TABLE IF NOT EXISTS BJTLXY(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT)"""
#     cur.execute(sql)
#     con.close()
# except:
#     print("创建失败")


# 数据库插入操作
db = pymysql.connect('127.0.0.1', 'root', '123456', 'ceshi')
# 利用cursor()创建游标对象
cursor = db.cursor()

# sql语句
sql = 'insert into BJTLXY(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)VALUES("Liu2", "DANA", 18, "M", "100000"),("HUANG", "LAOBAN", 19, "M", "99999")'
# 为了防止sql注入
# sql = "INSERT INTO BJTLXY(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
#       VALUE('%s', '%s', '%d', '%c', '%s')"%('Liu', 'DANA', 18, 'M', '100000')

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交执行
    db.commit()
    print('执行成功')
except:
    db.rollback()
    print('执行失败')
db.close()


#
# import pymysql
# import sys
# con=pymysql.connect('127.0.0.1','root','123456','ceshi')
# # with con:
# try:
#     cur=con.cursor()
#     sql = "CREATE TABLE IF NOT EXISTS BJTLXY(FIRST_NAME CHAR(20) NOT NULL)"
#     cur.execute(sql)
#     # cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
#     # cur.execute("INSERT INTO Writers(Name) VALUES('hONORE DE bALZAC')")
#     # cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
#     # cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
#     # cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
# except:
#     print('1')
