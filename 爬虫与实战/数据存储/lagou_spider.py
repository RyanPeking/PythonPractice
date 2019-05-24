'''
-url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
- post
-first:false
pn:2
kd:python爬虫

'''

import requests

for page in range(1, 2):
    data = {
        "first":'false',
        'pn':page,
        'kd':'python爬虫'
    }


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?oquery=%E7%88%AC%E8%99%AB&fromSearch=true&labelWords=relative&city=%E5%8C%97%E4%BA%AC',
        'Origin':'https://www.lagou.com',
        'Content-Length':str(len(data)),
        'Connection':'keep-alive',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token':None,
        'X-Requested-With':'XMLHttpRequest',


    }
    # proxies = {'https':'112.85.129.228:9999'}

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

    res = requests.post(url=url, headers=headers, data=data)
    print(res.text)

url = 'https://www.lagou.com/'
res = requests.get(url)
print(res.text)