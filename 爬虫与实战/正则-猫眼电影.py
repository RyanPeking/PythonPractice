'''
利用正则爬取猫眼电影
1.url:https://maoyan.com/
2.把电影信息尽可能多的拿下来

分析
1.一个影片的内容是以dd开头的单元
2.在单元内存一部电影的所有信息

思路：
1.利用re把dd内容都给找到
2.对应找到的每一个dd，用re挨个查找需要的信息

方法 三步走：
1.把页面down下来
2.提取出dd单元为单位的内容
3.对每一个dd进行单独信息提取
'''

from urllib import request

# 1.下载页面内容
url = "https://maoyan.com/"

rsp = request.urlopen(url)
html = rsp.read().decode()

# print(html)

# 2.按dd提取出内容
import re

s = r'<dd>(.*?)<dd>'

pattern = re.compile(s, re.S)

films = pattern.findall(html)


# print(films)
# print(len(films))

# 3.从每一个dd中单独提取出需要的信息
for film in films:
    # print(film)
    # 提取电影名称
    s = r'title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)