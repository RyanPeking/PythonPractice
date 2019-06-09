# -*- coding: utf-8 -*-
import scrapy
from ImageSpider.items import ImagespiderItem


class ImageSpider(scrapy.Spider):
    name = 'Image'
    allowed_domains = ['http://lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem()
        # 此处获取到的为集合图片，多张图片
        imgurl = response.css(".post img::attr(src)").extract()
        item['imgurl'] = imgurl
        yield item
