'''
注册百度地图API账号并进行开发者认证
目标：获取全国公园信息并保存至mysql数据库中

地点检索详情连接
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求


基础地址
http://api.map.baidu.com/place/v2/search?
参数：
    query:公园
    region：成都市
    scope:2
    page_size:20
    output:json
    ak:
'''


import requests

def get_json(loc, page_num=0):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    data = {
        'query': "公园",
        'region': loc,
        'scope': "2",
        'page_size': 20,
        'page_num':page_num,
        'output': "json",
        'ak': ''
    }

    url = 'http://api.map.baidu.com/place/v2/search?'
    res = requests.get(url, params=data, headers=headers)
    decode_json = res.json()

    return decode_json

a = get_json("北京市")
print(a)
