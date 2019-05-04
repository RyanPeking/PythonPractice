'''
1.主页https://tieba.baidu.com/f?kw=张继科
2.进去之后，贴吧有很多页
    第一页https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
    第二页https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
    第三页https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
3.由上面网址可以找到规律，每一页只有后面数字不同，且数字应该是（页数-1）x50

解决方法：
1.准备构建参数字典
    字典包含三部分 kw ie pn
2.使用parse构建完整url
3.使用for循环下载

'''

from urllib import request, parse

if __name__ == '__main__':
    qs = {
        "kw": "张继科",
        "ie": "utf-8",
        "pn": 0
    }
    urls = []
    base_url = "https://tieba.baidu.com/f?"
    for i in range(10):
        pn = i * 50
        qs['pn'] = str(pn)
        # 把qs编码后和基础url进行拼接
        urls.append(base_url + parse.urlencode(qs))

    print(urls)

    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        print(url)
        print(html)