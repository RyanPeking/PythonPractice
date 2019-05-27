'''
https://book.douban.com/subject_search?search_text=python&cat=1001
'''

from selenium import webdriver
import time
from lxml import etree

def spider(url, i):
    driver = webdriver.PhantomJS()
    driver.get(url)

    # 等待两秒钟
    time.sleep(2)

    # 生成图片快照
    driver.save_screenshot('/home/tlxy/practice/爬虫与实战/DHTML/img/douban_book.png')

    file_name = '/home/tlxy/practice/爬虫与实战/DHTML/img/douban_book.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    # 解析内容
    parse(file_name, i)

    driver.quit()

# 解析数据
def parse(file, i):
    # 读取文件
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # print(html)

    html = etree.HTML(html)

    # 获取所有book
    books = html.xpath('//div[@class="item-root"]')

    print(".........正在抓取豆瓣读书第{}页..........".format(i + 1))

    # 获取所有子节点
    for book in books:

        # 封面图片连接
        book_src = book.xpath('./a/img/@src')[0]

        # 书名
        book_name = book.xpath('.//div[@class="title"]/a/text()')[0]

        # 书的连接
        book_url = book.xpath('.//div[@class="title"]/a/@href')[0]

        # 评分
        try:
            book_star = book.xpath('.//span[@class="rating_nums"]/text()')[0]
        except:
            book_star = "评价人数不足"

        # 作者
        book_author = book.xpath('.//div[@class="meta abstract"]/text()')[0]

        print(book_src, book_name, book_url, book_star, book_author)


if __name__ == '__main__':
    for i in range(11):
        url = 'https://book.douban.com/subject_search?search_text=python&cat=1001&start={}'.format(i*15)
        spider(url, i)
        time.sleep(1)