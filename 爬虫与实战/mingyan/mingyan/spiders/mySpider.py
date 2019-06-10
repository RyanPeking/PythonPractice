# -*- coding: utf-8 -*-
import scrapy
from mingyan.items import MingyanItem


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'

    # start_urls = ['http://lab.scrapyd.cn//']
    def start_requests(self):
        urls = ['http://lab.scrapyd.cn/page/{}'.format(str(num)) for num in range(1,7)]
        print(urls)
        # http://lab.scrapyd.cn/page/1
        for url in urls:
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # page = response.url.split('/')
        # print(page)
        # page = page[-2]
        #
        # filename = 'mingyan-%s.html'%page
        #
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        #
        # self.log("保存文件：%s"%filename)
        item = MingyanItem()
        title = response.xpath('//div[@class="quote post"]/span[@class="text"]/text()').extract()[0]

        author = response.xpath('//small[@class="author"]/text()').extract()[0]
        tag = response.xpath('//div[@class="tags"]//a/text()').extract()[0]
        # print(author, ">>>>>>", title,">>>>>>", tag)

        item['title'] = title
        item['author'] = author
        yield item