# -*- coding: utf-8 -*-
import scrapy
from XHSpider.items import XhspiderItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/2014.html']

    def parse(self, response):
        infos = response.xpath('//div[@class="items"]')
        # print(infos)
        for info in infos:
            # print(info)
            title = info.xpath('.//p/a/text()').extract()[0]
            href = info.xpath('.//div[@class="picbox"]/a/img/@src').extract()[0]
            if 'http://www.xiaohuar.com' not in href:
                href = 'http://www.xiaohuar.com' + href
            # print(title, href)

            item = XhspiderItem()
            item['title'] = title
            item['href'] = href

            yield item