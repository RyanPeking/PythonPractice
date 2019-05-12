import scrapy

from e15_meiju.items import MeijuItem

class MeijuSpider(scrapy.Spider):

    name = "meiju"

    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for movie in movies:
            item = MeijuItem()
            print(type(movie.xpath('./h5/a/@title')))
            print(type(movie))
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = movie.xpath('./h5/a/@href').extract()[0]

            tv = movie.xpath('./span[@class="mjtv"]/text()')

            if len(tv):
                item['tv'] = tv.extract()[0]
            else:
                item['tv'] = ""
            print('Item.name:{0}'.format(item['name']))
            yield item