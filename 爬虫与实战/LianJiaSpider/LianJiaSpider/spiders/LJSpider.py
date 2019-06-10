# -*- coding: utf-8 -*-
import random

import os
import scrapy
import time
from LianJiaSpider.settings import headers
from LianJiaSpider.items import LianjiaSpiderItem
from urllib import request


class LjspiderSpider(scrapy.Spider):
    name = "LJSpider"
    allowed_domains = ["lianjia.com"]
    # start_urls = (
    #     'http://www.lianjia.com/',
    # )

    def start_requests(self):

        start_urls = [
            'https://bj.lianjia.com/zufang/pg{}'.format(page) for page in range(1,5)
        ]
        for start_url in start_urls:
            # print(start_url)
            yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True, headers=headers)

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        infos = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        # print(infos)
        for info in infos:
            # 获取房屋标题
            house_title = info.xpath('.//p[@class="content__list--item--title twoline"]/a/text()').extract()[0].strip().replace(' ', '')
            # print(house_title)
            # 获取房屋详情链接
            house_hrefs = info.xpath('.//p[@class="content__list--item--title twoline"]/a/@href').extract()

            house_href = 'https://bj.lianjia.com/' + house_hrefs[0]

            # 获取小区名称
            house_names = info.xpath('.//p[@class="content__list--item--des"]/a/text()').extract()
            house_name = '-'.join(house_names)
            # print(house_name)
            time.sleep(random.choice([0.5,1,1.5,2]))
            yield scrapy.Request(url=house_href, callback=self.detail_parse, dont_filter=True, headers=headers, meta={'house_title':house_title,'house_href':house_href,'house_name':house_name})


    def detail_parse(self, response):
        infos = response.xpath('//div[@class="content clear w1150"]')

        for info in infos:
            # 房源编号
            house_nums = info.xpath('.//i[@class="house_code"]/text()').extract()
            house_num = house_nums[0].split('：')[-1]
            # print(house_num)

            # 房屋价格
            house_price = info.xpath('.//p[@class="content__aside--title"]/span/text()').extract()
            house_price = house_price[0] + '元/月'
            # print(house_price)

            # 经纪人
            # house_people = info.xpath('.//span[@class="contact_name"]/@title').extract()[0]
            # print(house_people)



            house_infos = info.xpath('.//p[@class="content__article__table"]/span/text()').extract()

            # 租赁方式
            house_style = house_infos[0]
            # 厅室
            house_room = house_infos[1]
            # 大小
            house_size= house_infos[2]
            # 方向
            house_toward = house_infos[3]

            # 图片地址
            house_imgdir = '/home/tlxy/practice/爬虫与实战/LianJiaSpider/LianJiaSpider/lianjiaImg/' + response.meta['house_title']
            # print(house_imgdir)

            # print(house_style, house_room, house_size, house_toward)

            # 进行数据存储
            item = LianjiaSpiderItem()

            item['house_title'] = response.meta['house_title']
            item['house_href'] = response.meta['house_href']
            item['house_name'] = response.meta['house_name']
            item['house_num'] = house_num
            item['house_price'] = house_price
            item['house_style'] = house_style
            item['house_room'] = house_room
            item['house_size'] = house_size
            item['house_toward'] = house_toward
            item['house_imgdir'] = house_imgdir
            # print(item)

            yield item

            # # 图片信息处理
            # house_img_urls = info.xpath('.//div[@class="content__article__slide__item"]/a/img/@src').extract()
            # # print(house_img_url)
            # if len(house_img_urls) != 0:
            #     for house_img_url in house_img_urls:
            #         # 图片名称
            #         img_name = str(time.time()) + '.jpg'
            #         if not os.path.exists(house_imgdir):
            #             os.makedirs(house_imgdir)
            #
            #         request.urlretrieve(house_img_url, house_imgdir+'/'+img_name)





