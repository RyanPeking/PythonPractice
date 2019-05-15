import pymysql

db = pymysql.connect('192.168.61.98', 'root', '123456', 'ceshi')
# print(db)
# 创建游标
cursor = db.cursor()

# 创建删除sql语句
sql = "DELETE FROM BJTLXY WHERE INCOME > '%d'"%(99999)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    print("执行失败")
db.close()