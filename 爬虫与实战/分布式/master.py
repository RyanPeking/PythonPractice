import requests
import time
from bs4 import BeautifulSoup
import redis

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def push_redis_list():
    r = redis.Redis(host='127.0.0.1', port=6379)
    print(r.keys('*'))

    link_list = [
        'http://www.xtx6.com',
        'http://www.sczw.com',
        'http://www.sm.cn',
        'http://www.qqtn.com',
        'http://www.21food.cn',
    ]

    for url in link_list:
        try:
            response = requests.get(url, headers=headers, timeout=20)
        except:
            print('该网址无法连接：', url)
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        img_list = soup.find_all('img')
        for img in img_list:
            try:
                img_url = img['src']
                if img_url != '':
                    print('加入的图片url地址为：',img_url)
                    r.lpush('img_url', img_url)
            except:
                continue
        print('现在图片连接的个数为：',r.llen('img_url'))

    return

def get_img():
    r = redis.Redis(host='127.0.0.1', port=6379)
    while True:
        try:
            url = r.lpop('img_url')
            url = url.decode('ascii')
            if url[:2] == '//':
                url = 'http:' + url
            print(url)
            try:
                response = requests.get(url,headers=headers, timeout=20)
                name = int(time.time())
                f = open(str(name)+url[-4:], 'wb')
                f.write(response.content)
                f.close()
                print('已经获取图片', url)
            except Exception as e:
                print('爬取图片出问题了', e)
            time.sleep(3)
        except Exception as e:
            print(e)
            time.sleep(10)
            break

    return

if __name__ == '__main__':
    this_machine = 'master'
    print('开始分布式爬取')
    if this_machine == 'master':
        push_redis_list()
    else:
        get_img()