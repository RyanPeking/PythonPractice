# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QDreaderItem(scrapy.Item):
    # 首页内容
    title = scrapy.Field()#标题
    href = scrapy.Field()#详情页链接
    # 详情页内容
    author = scrapy.Field()#作者
    info = scrapy.Field()#简要信息
