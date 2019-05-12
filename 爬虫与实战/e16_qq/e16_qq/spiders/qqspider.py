import scrapy
import re

from e16_qq.items import QQItem

class QQSpider(scrapy.Spider):

    name = 'qq'
    # 设置只能爬取腾讯域名的信息
    allowed_domains = ['hr.tencent.com']

    start_urls = [
        'https://careers.tencent.com/search.html'
    ]

    page = 1
    print('正在执行qqspider')
    def parse(self, response):
        print(response.text)
        print("正在执行parse")
        print(response.xpath('//*[contains(@class, "recruit-list")]'))
        for each in response.xpath('//*[contains(@*, "recruit-list")]'):
            item = QQItem()
            name = each.xpath('./a/h4').extract()[0]
            positionInfo = each.xpath('./a/p[contains(@*,"recruit-text")]').extract()[0]
            workLocation = each.xpath('./a/p[contains(@*,@"recruit-tips")/span]').extract()[1]

            item['name'] = name.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')

            global start_urls, page
            page += 1
            url = start_urls[0] + '?index=' + page
            print(item)
            print(url)
            yield scrapy.Request(url, callback=self.parse)

            yield item