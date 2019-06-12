# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from SunGovDG.items import DongguanItem


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # 每个页面的匹配规则
    pagelink = LinkExtractor(allow=('page='))
    # print(pagelink)

    # 每个帖子的匹配规则
    contentlink = LinkExtractor(allow=(r'/question/\d+/\d+.shtml'))

    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, callback='parse_item')
    ]

    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        # print(response.url)
        title = response.xpath('//div[@class="wzy1"]//span[@class="niae2_top"]/text()').extract()[0].replace("提问：", '').replace(r'\xa0\xa0\xa0\xa0', '')
        number = response.xpath('//div[@class="wzy1"]//span[2]/text()').extract()[0].replace("编号:", '').replace(r'\xa0\xa', '')
        content = response.xpath('//td[@class="txt16_3"]/text()').extract()[0]

        # print(title, number, content)

        item = DongguanItem()

        item['title'] = title
        item['number'] = number
        item['content'] = content
        item['url'] = response.url
        print(item)
        yield item