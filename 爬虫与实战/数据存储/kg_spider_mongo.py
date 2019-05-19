'''
酷狗音乐top500抓取
url = 'https://www.kugou.com/yy/rank/home/1-8888.html'
变换页面信息
    1-23    500

最终数据存储至mongodb
'''

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
def kg_spider(url):
    '''
    获取酷狗音乐top500，保存至mongo
    :param url:
    :return:
    '''
    res = requests.get(url, headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text, 'lxml')

    ranks = soup.select('.pc_temp_num')
    # print(ranks)
    titles = soup.select('.pc_temp_songlist > ul > li > a')
    # print(titles)
    times = soup.select('.pc_temp_time')

    for rank, title, time in zip(ranks, titles, times):
        rank = rank.get_text().strip()
        # print(rank)
        # print(title)
        song = title.get_text().split('-')[-1].strip()
        singer = title.get_text().split('-')[0].strip()
        song_time = time.get_text().strip()
        print(rank, song, singer, song_time)

        data = {
            'rank': rank,
            'singer': singer,
            'song': song,
            'time': song_time
        }

    # 数据存储

        client = MongoClient()
        songs = client.KG_DB.songs
        songs_id = songs.insert(data)
        print(songs_id)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        data = kg_spider(url)
