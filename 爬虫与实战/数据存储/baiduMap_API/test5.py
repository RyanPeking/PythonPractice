from MySQLAPI_demo import MysqlDemo

mysql = MysqlDemo('192.168.61.98', 'root', '123456', 'ceshi')

data = {
    'FIRST_NAME':'Tuling',
    'LAST_NAME':'Xueyuan',
    'AGE': '18',
    'SEX':'M',
    'INCOME':'100000'
}

mysql.insert('BJTLXY', data)

sql = 'select * from BJTLXY WHERE FIRST_NAME="Tuling"'
res = mysql.get_one(sql)
print(res)

res = mysql.get_all('select * from BJTLXY')
print(res)
