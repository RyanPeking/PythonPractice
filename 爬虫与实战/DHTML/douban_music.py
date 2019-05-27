'''
解析豆瓣音乐排行榜
url = 'https://music.douban.com/chart'
'''

from selenium import webdriver
import os
from lxml import etree

# 路径
root_dir = '/home/tlxy/practice/爬虫与实战/DHTML/img/douban'
if not os.path.exists(root_dir):
    os.makedirs(root_dir)

driver = webdriver.PhantomJS()

driver.get('https://music.douban.com/chart')
driver.implicitly_wait(5)

file_name = root_dir + "//music_1.png"
# driver.save_screenshot(file_name)

result = driver.page_source

html = etree.HTML(result)

li_list = html.xpath('//ul[@class="col5"]/li[@class="clearfix"]')

count = 1
for li in li_list:
    # 获取排名信息
    index = li.xpath('.//span[@class="green-num-box"]/text()')[0]
    # print(index)
    if count <= 10:
        src = li.xpath('.//img/@src')
        if src != []:
            src = src[0]
            print(src)

        # 获取歌名
        name = li.xpath('.//h3/a')
        if name:
            name = name[0].text
            print(name)

        # 歌手以及播放次数
        singer = li.xpath('.//p')
        if singer:
            singer = singer[0].text
            print(singer)

    else:
        pass




