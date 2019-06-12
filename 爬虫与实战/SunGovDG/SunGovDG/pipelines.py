# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs, json

class SungovdgPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonDOngguanPipelines(object):
    def __init__(self):
        # 创建一个只读文件，编码格式为utf-8
        self.filename = codecs.open('sunDG.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(content)
        return item
    def spider_closed(self, spider):
        self.filename.close()
