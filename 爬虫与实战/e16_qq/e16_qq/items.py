# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class E16QqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QQItem(scrapy.Item):
    name = scrapy.Field()
    positionInfo = scrapy.Field()
    workLocation = scrapy.Field()
