import pymysql

db = pymysql.connect('192.168.61.98', 'root', '123456', 'BaiduMap')
cursor = db.cursor()


# # 创建city表
# sql = """
# CREATE TABLE CITY(
# ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# CITY VARCHAR(200) NOT NULL,
# PARK VARCHAR(200) NOT NULL,
# LOCATION_LAT FLOAT ,
# LOCATION_LNG FLOAT ,
# ADDRESS VARCHAR (200),
# STREET_ID VARCHAR (200),
# UID VARCHAR (200),
# CREATE_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP )
# """
#
# cursor.execute(sql)


class Sql():
    @staticmethod
    def insert_city(city, park, location_lat, location_lng, address, street_id, uid):
        sql = 'insert into CITY(city, park, location_lat, location_lng, address, street_id, uid)VALUES' \
              ' (%(city)s, %(park)s, %(location_lat)s, %(location_lng)s, %(address)s, %(street_id)s, %(uid)s)'

        value = {
            'city':city,
            'park':park,
            'location_lat':location_lat,
            'location_lng':location_lng,
            'address':address,
            'street_id':street_id,
            'uid':uid
        }

        try:
            cursor.execute(sql, value)
            db.commit()
            print("插入成功")
        except Exception as e:
            print("插入失败，", e)
            db.rollback()


    # 读取city表中的uid号
    @classmethod
    def read_city(cls):
        sql = 'SELECT uid FROM CITY WHERE ID > 0'
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        return results
