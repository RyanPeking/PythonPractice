# -*- coding: utf-8 -*-
import os
import scrapy
import re
from urllib import request

class LanrentukuSpider(scrapy.Spider):
    name = 'lanrentuku'
    allowed_domains = ['lanrentuku.com']
    start_urls = ['http://www.lanrentuku.com/vector/flower/p1.html']

    # base_url = 'http://www.lanrentuku.com/vector/flower/p%s.html'
    # for page in range(1,2):
    #     start_urls.append(base_url % page)
    # print(start_urls)

    root_dir = 'tuku'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    def parse(self, response):
        # print(response.text)
        paths = response.url.split('/')
        with open(paths[-1], 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))

        dd_list = response.xpath('//div[@class="list-pic"]/dl/dd').extract()
        for dd in dd_list:
            # print(type(dd))
            # 匹配缩略图
            pattern = re.compile(r'<img.*src="(.*?)"')
            src = pattern.findall(dd)
            # print(src)
            if src != []:
                print(src[0])

            # 获取详情页
            pattern = re.compile(r'<a.*href="(.*?)"')
            a_list = pattern.findall(dd)
            if a_list != []:
                href = a_list[0]
                href = request.urljoin(response.url, href)
                print(href)

                yield scrapy.Request(url=href, callback=self.detail_page)

    def detail_page(self, response):
        imgs = response.xpath('//div[@class="content-a"]/p/img/@src').extract()[0]
        print(imgs)

        # 下载图片
        yield scrapy.Request(url=imgs, callback=self.download_pic)

    def download_pic(self, response):
        paths = response.url.split('/')
        filename = self.root_dir + '/' + paths[-1]

        with open(filename, 'wb') as f:
            f.write(response.body)
