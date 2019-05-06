'''
扇贝单词
1.把python单词列表download下来
2.主要练习目的xpath
3.理论上不需要登录
4.https://www.shanbay.com/wordbook/187711/
'''

from urllib import request
from lxml import etree

import json

#词汇表
words = []

def shanbei(page):
    url = "https://www.shanbay.com/wordlist/187711/540709/?page=%s"%page
    print(url)

    rsp = request.urlopen(url)

    html = rsp.read()

    # 解析html
    html = etree.HTML(html)

    tr_list = html.xpath("//tr")

    # 遍历每个tr元素，每一个tr对应一个单词和介绍
    for tr in tr_list:
        '''
        查找相应的单词和解释
        '''
        word = {}

        strong = tr.xpath('.//strong')
        if len(strong):
            name = strong[0].text.strip()
            word['name'] = name
            # print(name)

        # 查找单词的释义
        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content
            # print(content)

        print(word)
        if word != {}:
            words.append(word)
    # print(words)

if __name__ == '__main__':
    shanbei(1)