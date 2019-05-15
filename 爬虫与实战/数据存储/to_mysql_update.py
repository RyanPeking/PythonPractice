import pymysql

db = pymysql.connect('192.168.61.98', 'root', '123456', 'ceshi')
# print(db)
# 创建游标
cursor = db.cursor()

# sql更新
sql = "UPDATE BJTLXY SET AGE = AGE-1 WHERE FIRST_NAME='%s'"%('huang')
try:
    cursor.execute(sql)
    db.commit()
except:
    # 发生错误请回滚
    db.rollback()
    print("执行错误")
db.close()