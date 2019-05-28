from selenium import webdriver
import time
from lxml import etree

driver = webdriver.PhantomJS()

def getpage():
    driver.get('https://www.douyu.com/directory/all')
    time.sleep(5)
    html = driver.page_source

    return html

def parse(html):
    html = etree.HTML(html)
    room_li = html.xpath('//ul[@class="layout-Cover-list"]/li')
    # print(len(room_li))
    for room in room_li:
        # 标题
        title = room.xpath('.//h3[@class="DyListCover-intro"]/text()')[0].strip()
        print(title)

        # 标签
        tag = room.xpath('.//span[@class="DyListCover-zone"]/text()')[0].strip()

        # 作者
        author = room.xpath('.//h2[@class="DyListCover-user"]/text()')[0].strip()

        print(title, "****", tag, "****", author)

def main():
    html = getpage()
    parse(html)

if __name__ == '__main__':
    main()