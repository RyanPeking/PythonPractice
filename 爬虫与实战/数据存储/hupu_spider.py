import requests
from lxml import etree
from hupu_mongo import MongoAPI


def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    html = res.text
    # print(html)
    html = etree.HTML(html)
    return html

def parse(html):
    # titles = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a/text()')
    # # print(len(titles))

    parse_hrefs = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a/@href')
    parse_hrefs = ['https://bbs.hupu.com/' + href for href in parse_hrefs]
    # print(len(parse_hrefs))

    titles = []
    for href in parse_hrefs:
        title = get_title(href)
        titles.append(title)
    # print(titles)
    # print(len(titles))

    authors = html.xpath('//div[@class="author box"]/a[@class="aulink"]/text()')
    # print(authors)
    # print(len(authors))

    # 获取发布时间
    times = html.xpath('//div[@class="author box"]/a[2]/text()')
    # print(times)
    # print(len(times))

    # 获取回复数和发布时间
    datas = html.xpath('//ul[@class="for-list"]/li/span[@class="ansour box"]/text()')
    datas = [x.split('\xa0/\xa0') for x in datas]
    # 回复数
    replies = [x[0] for x in datas]
    browses = [x[1] for x in datas]
    # print(replies, browses)
    # print(len(replies), len(browses))

    # 最后回复时间
    last_times = html.xpath('//div[@class="endreply box"]/a/text()')
    # print(last_times)
    # print(len(last_times))

    # 最后回复人
    last_names = html.xpath('//div[@class="endreply box"]/span[@class="endauthor "]/text()')
    # print(last_names)
    # print(len(last_names))

    items = zip(titles, parse_hrefs, authors, times, replies, browses, last_times, last_names)

    return items

# 数据存储
def data_storage(items):
    # print(items)
    hupu_post = MongoAPI('192.168.61.98', 27017, 'hupu', 'post')
    for item in items:
        hupu_post.add({
            'titles': item[0],
            'parse_hrefs': item[1],
            'authors': item[2],
            'times': item[3],
            'replies': item[4],
            'browses': item[5],
            'last_times': item[6],
            'last_names': item[7],

        })



# 获取标题
def get_title(url):
    html = spider(url)
    try:
        title = html.xpath('//div[@class="bbs-hd-h1"]/h1[@id="j_data"]/text()')[0]
    except:
        title = None
    print(title)
    return title

def main():
    url = 'https://bbs.hupu.com/nba'
    html = spider(url)
    data_storage(parse(html))

if __name__ == '__main__':
    main()