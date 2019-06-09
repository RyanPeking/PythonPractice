# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import settings

class XcspiderPipeline(object):
    print("1")
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbname = settings.MONGODB_DBNAME
        sheetname = settings.MONGODB_SHEETNAME
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.port = mydb[sheetname]
    def process_item(self, item, spider):
        print('2')
        data = dict(item)
        print(data)
        self.port.insert(data)
        print("插入成功")
        return item


# host = '127.0.0.1'
# port = 27017
# dbname = 'DB_XICI'
# sheetname = 'XICI'
# client = pymongo.MongoClient(host=host, port=port)
# mydb = client[dbname]
# print(settings.MONGODB_HOST)