# -*- coding: utf-8 -*-
import scrapy
from XcSpider.items import XiciDailiItem

class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        items_1 = response.xpath('//tr[@class="odd"]')
        items_2 = response.xpath('//tr[@class=""]')

        items = items_1 + items_2

        infos = XiciDailiItem()
        # print(items)
        for item in items:
            # print(item)
            # 获取国家图片连接
            countries = item.xpath('./td[@class="country"]/img/@src').extract()
            # print(countries)
            if countries != []:
                country = countries[0]
            else:
                country = None

            try:
            # 获取ipaddress
                ipaddress = item.xpath('./td[2]/text()').extract()[0]
            except:
                ipaddress = None
            # print(ipaddress)
            try:
                port = item.xpath('./td[3]/text()').extract()[0]
            except:
                port = None
            try:
                serveraddr = item.xpath('./td[4]/text()').extract()[0]
            except:
                serveraddr = None
            try:
                isanonymous = item.xpath('./td[5]/text()').extract()[0]
            except:
                isanonymous = None
            try:
                type = item.xpath('./td[6]/text()').extract()[0]
            except:
                type = None
            try:
                alivetime = item.xpath('./td[7]/text()').extract()[0]
            except:
                alivetime = None
            try:
                verifictiontime = item.xpath('./td[8]/text()').extract()[0]
            except:
                verifictiontime = None

            infos['country'] = country
            infos['ipaddress'] = ipaddress
            infos['port'] = port
            infos['serveraddr'] = serveraddr
            infos['isanonymous'] = isanonymous
            infos['type'] = type
            infos['alivetime'] = alivetime
            infos['verifictiontime'] = verifictiontime
            yield infos
            # print(infos)
            # print(ipaddress, port, severaddr, isanonymous, type, alivetime, verifictiontime)

