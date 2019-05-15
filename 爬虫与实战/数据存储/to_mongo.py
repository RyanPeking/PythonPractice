'''
mongoDB：非关系型数据库
mongoDB属于更加适合爬虫的数据库
mongoDB是一个基于分布式文件存储的数据库，由C++编写
主要为web应用提供可扩展的高性能数据存储解决方案

概念说明：
SQL:            mongoDB              说明
database        database            数据库
table           collection          表/集合
row             document            行/文档
column          field               字段/域
index           index               索引
primary         primary             主键/_id为主键

安装mongoDB
    请自行百度
        sudo apt-get install mongodb
如何Python操作mongodb
    pip install pymongo
'''

import pymongo

# client = pymongo.MongoClient()
# client = pymongo.MongoClient('192.168.61.98', 27017)
client = pymongo.MongoClient('mongodb://192.168.61.98:27017')
# print(client)

# 获取数据库，连接数据库
db = client.TL

# 获取集合
std = db.student

datas = std.find()
print(datas, type(datas))
for data in datas:
    print(data)