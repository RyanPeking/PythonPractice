'''
视频播放地址
https://www.bilibili.com/video/av50623860
'''

import requests
import json
from lxml import etree
import os
import time


def getInfo(startPage, endPage):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    for page in range(startPage, endPage+1):
        url = 'https://search.bilibili.com/all?keyword=%E8%A7%86%E9%A2%91&page='+str(page)
        res = requests.get(url, headers=headers)
        html = etree.HTML(res.text)
        videos = html.xpath('//li[@class="video matrix"]/a/@href')
        video_url = []
        for video in videos:
            video = "https:" + video
            video_url.append(video)
        title = html.xpath('//li[@class="video matrix"]/a/@title')

    data = zip(title, video_url)

    return data

def downloadVideo(data):
    path = '/home/tlxy/practice/爬虫与实战/数据存储/bilibili'
    if not os.path.exists(path):
        os.makedirs(path)

    for title, url in data:
        # 视频存放路径
        root = path + "/" + title
        # print(title, url)

        print("正在下载视频：{}".format(title))
        print(root, url)
        # 利用os.system操作you-get进行视频下载
        os.system("you-get -o {} {}".format(root, url))
        time.sleep(3)
        print("视频{}下载完成".format(title))

if __name__ == '__main__':
    data = getInfo(1,3)
    downloadVideo(data)