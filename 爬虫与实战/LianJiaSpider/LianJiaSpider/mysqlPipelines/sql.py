import pymysql
from LianJiaSpider import settings

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

db = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=MYSQL_PORT,database=MYSQL_DB, charset='utf8')
cursor = db.cursor()
print("数据库连接成功")

class Sql():
    @classmethod
    def insert_db_lianjia(cls, house_title,house_href,house_name,house_num,house_price,house_style,house_room,house_size,house_toward,house_imgdir):
        sql = 'insert into lianjia(house_title,house_href,house_name,house_num,house_price,house_style,house_room,house_size,house_toward,house_imgdir) VALUES (%(house_title)s, %(house_href)s, %(house_name)s, %(house_num)s,%(house_price)s, %(house_style)s, %(house_room)s, %(house_size)s, %(house_toward)s, %(house_imgdir)s)'
        value = {
            'house_title':house_title,
            'house_href':house_href,
            'house_name':house_name,
            'house_num':house_num,
            'house_price':house_price,
            'house_style':house_style,
            'house_room':house_room,
            'house_size':house_size,
            'house_toward':house_toward,
            'house_imgdir':house_imgdir

        }
        try:
            cursor.execute(sql,value)
            db.commit()
            print('插入成功')
        except Exception as e:
            print(e)
            print('插入失败')
            db.rollback()

    # 去重
    @classmethod
    def select_name(cls, house_title):
        sql = "select exists(select 1 from lianjia where house_title=%(house_title)s"
        value = {
            'house_title':house_title
        }
        cursor.execute(sql, value)
        return cursor.fetchall()[0]
