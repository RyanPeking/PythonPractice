import re
from bs4 import BeautifulSoup
from urllib import request

class HtmlParse(object):
    def parse(self, page_url, html_cont):
        '''
        解析页面内容，抽取url和数据
        :param page_url: 下载页面url地址
        :param html_cont: 下载页面的内容
        :return:
        '''

        if page_url is None or html_cont is None:
            return None

        soup = BeautifulSoup(html_cont, 'lxml', from_encoding='utf-8')
        new_url = self._get_new_url(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_url, new_data


    def _get_new_url(self, page_url, soup):
        '''
        抽取新的url地址
        :param page_url:
        :param soup:
        :return:
        '''

        new_url = set()

        # 抓取符合要求的a标记    href="/item/Sublime"
        links = soup.find_all('a', href=re.compile(r'/item/.*?">'))
        for link in links:
            new_url = link['href']
            new_full_url = request.urljoin(page_url, new_url)
            new_url.add(new_full_url)

        return new_url

    def _get_new_data(self, page_url, soup):
        '''
        抓取有效数据
        :param page_url:
        :param soup:
        :return:
        '''
        data = {}
        data['url'] = page_url
        title =
