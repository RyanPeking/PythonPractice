# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from Meiju.items import MeijuSpiderItem

class MeijuspiderSpider(scrapy.Spider):
    name = 'MeijuSpider'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        response.xpath('//ul[@class="top-list  fn-clear"]/li')
        content = etree.HTML(response.body.decode("GBK"))
        # print(type(response.body))
        # print(response.text)
        # print(type(response.text))
        movies = content.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            # print(movie)
            a_list = movie.xpath('./h5/a')
            a = a_list[0].text      # 电影名

            # 电影状态
            try:
                state = movie.xpath('.//span[@class="state1 new100state1"]/font')[0].text
            except IndexError:
                state = movie.xpath('.//span[@class="state1 new100state1"]')[0].text
            # print(state)

            item = MeijuSpiderItem()

            item['name'] = a
            item['state'] = state

            print(a, '^^^^^^', state)

            yield item