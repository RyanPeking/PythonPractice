import time
from selenium import webdriver
from fake_useragent import UserAgent
from scrapy.http import HtmlResponse


class LRTKDownloaderMiddleware(object):
    def __init__(self):
        self.ug = UserAgent()
    def process_request(self, request, spider):
        '''

        :param request: 请求对象
        :param spider: 爬虫对象
        :return:
        '''
        # 加入headers头部US
        request.headers.setdefault('User-Agent', self.ug.random)

        driver = webdriver.Chrome()
        driver.get(request.url)
        time.sleep(1)
        driver.save_screenshot('1.png')


        # 查找下一页
        print('.............请求下一页..............')
        a = driver.find_element_by_xpath('//*[@id="l"]/div[5]/ul/li[13]/a')

        # print(next_url_list)
        #
        # a = next_url_list.find_element_by_xpath('./a')
        a.click()

        time.sleep(2)

        html = driver.page_source

        return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)