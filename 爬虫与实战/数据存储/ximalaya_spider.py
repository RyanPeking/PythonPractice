'''
喜马拉雅网站音乐下载
https://www.ximalaya.com/revision/play/album?albumId=3595841&pageNum=1&sort=-1&pageSize=30
https://www.ximalaya.com/revision/play/album?albumId=8587845&pageNum=1&sort=-1&pageSize=30


https://www.ximalaya.com/yinyue/yaogun/
['rock',]



'''
import requests
from pypinyin import lazy_pinyin
import re
import json
from urllib import request

# 翻译要查找的歌曲类型
def fanyi(string):
    string = lazy_pinyin(string)
    string = ''.join(string)
    # print(string)
    return string

# 获取详情页面信息
def start_spider(str, headers):
    url = "https://www.ximalaya.com/yinyue/{}/".format(str)
    html = requests.get(url, headers=headers).text
    # print(html)

    return html

# 获取albumId值
def get_albumId(html, headers):
    albumIds = re.findall(r'"albumId":(.*?),', html)
    # print(albumIds)

    albumId = albumIds[0]
    print(albumId)

    # 构建下载地址
    down_url = 'https://www.ximalaya.com/revision/play/album?albumId={}&pageNum=1&sort=-1&pageSize=30'.format(albumId)
    # down_url = 'https://www.ximalaya.com/revision/play/album?albumId=4140580&pageNum=1&sort=-1&pageSize=30'

    # 请求音乐json文件
    res = requests.get(down_url, headers=headers)
    print(res.status_code)
    print(res.text)
    music_json = res.text
    return music_json

# 开始下载音乐
def download_music(music_json):
    # 获取歌曲标题
    music_json = json.loads(music_json)
    titles = music_json['data']['tracksAudioPlay']
    for title in titles:
        print(title['trackName'])
        print(title['src'])
        if '/' in title['trackName']:
            title['trackName'] = title['trackName'].replace('/', '-')
        request.urlretrieve(title['src'], '/home/tlxy/practice/爬虫与实战/数据存储/baotu/'+title['trackName'])

if __name__ == '__main__':
    headers = {
        # 'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN, zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.ximalaya.com',
        # 'Cookie': 'x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; device_id=xm_1558421400988_jvxfv4wsnduonw; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1558421401,1558422009; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1558422009',
        # 'xm-sign': '59e9b955db277e93c60de9ae4bffe093(96)1558425612502(23)1558425613677'
    }
    music_type = input("Please input your music type:")
    music_type = fanyi(music_type)
    html = start_spider(music_type, headers)
    music_json = get_albumId(html, headers)
    # download_music(music_json)
