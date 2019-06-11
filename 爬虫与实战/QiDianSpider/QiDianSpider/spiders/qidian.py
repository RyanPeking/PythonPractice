# -*- coding: utf-8 -*-
import scrapy
from QiDianSpider.items import QDreaderItem

class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    def start_requests(self):
        start_urls = ['https://www.qidian.com/free']
        yield scrapy.Request(url=start_urls[0], callback=self.parse, meta={'phantomjs':True}, dont_filter=True)

    def parse(self, response):
        infos = response.xpath('//div[@class="book-img-text"]/ul/li')
        for info in infos:
            # print(info)
            title = info.xpath('.//div[@class="book-mid-info"]/h4/a/text()').extract()[0]
            href = info.xpath('.//div[@class="book-mid-info"]/h4/a/@href').extract()[0]
            href = 'https://' + href
            # print(title, href)

            item = QDreaderItem()
            item['title'] = title
            item['href'] = href

            yield item
            yield scrapy.Request(url=href,callback=self.parse_detail,meta={'data':item, 'phantomjs':False},dont_filter=True)

    def parse_detail(self, reponse):
        # print('正在执行页面详细解析')
        item = reponse.meta['data']

        author = reponse.xpath('//div[@class="book-info "]//span/a/text()').extract()
        print(author)