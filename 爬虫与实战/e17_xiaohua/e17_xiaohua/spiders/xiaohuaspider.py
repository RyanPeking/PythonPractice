import scrapy
from e17_xiaohua.items import XiaohuaItem
from urllib import request

class XiaohuaSpider(scrapy.Spider):

    name = 'xiaohua'
    # allow_domains = ['xiaohuar.com']

    start_urls = ['http://www.xiaohuar.com/hua/']

    def parse(self, response):
        # print("正在打印网页")
        # print(response.text)
        bookmarks = response.xpath('//div[@class="item masonry_brick masonry-brick"]')

        for bm in bookmarks:
            item = XiaohuaItem()

            title = bm.xpath('.//div[@class="title"]/span/a/text()').extract()[0]
            href = bm.xpath('.//div[@class="title"]/span/a/@href').extract()[0]
            src = bm.xpath('.//div[@class="img"]/a/img/@src').extract()[0]

            item['title'] = title
            item['href'] = href
            item['src'] = src
            print("正在打印item")
            print(item)
            yield item