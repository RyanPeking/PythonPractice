import time
from selenium import webdriver
from scrapy.http import HtmlResponse


class XiaoHuaDownloadMiddlewares(object):
    def process_request(self, request, spider):
        '''
        自定义爬虫下载中间件
        :param request:
        :param spider:
        :return:
        '''
        driver = webdriver.Chrome()
        driver.get(request.url)
        time.sleep(2)
        driver.save_screenshot('1.png')
        js = 'document.body.scrollTop=10000'
        driver.execute_script(js)

        time.sleep(4)
        driver.save_screenshot('2.png')
        html = driver.page_source
        driver.quit()
        # 一定记得return
        # HtmlResponse对应的是爬虫中的parse函数
        return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)