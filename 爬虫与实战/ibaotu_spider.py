import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
        self.offset = 1

    def start(self, url):
        res = requests.get(url=url, headers = self.headers)
        html = res.text

        html = etree.HTML(html)

        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        # print(video_src)
        video_title = html.xpath('//div[@class="show-image"]/img/@alt')
        # print(video_title)

        # 处理下一页
        next_page = html.xpath('//a[@class="next"]/@href')
        if next_page:
            next_page = "http:" + next_page[0]

        else:
            return

        print(next_page)

        self.write_file(video_src, video_title)
        self.start(next_page)

    def write_file(self, video_src, video_title):
        for src, title in zip(video_src, video_title):
            response = requests.get("http:" + src, headers=self.headers)
            filename = title + '.mp4'
            # print(filename)

            with open("/home/tlxy/practice/爬虫与实战/数据存储/baotu/"+filename, 'wb') as f:
                f.write(response.content)

if __name__ == '__main__':
    spider = Spider()

    url = 'https://ibaotu.com/shipin/7-0-0-0-0-1.html'
    spider.start(url)