'''
url = 'http://api.map.baidu.com/place/v2/detail?
uid=435d7aea036e54355abbbcc8&output=json&scope=2
&ak=您的密钥' //GET请求

'''

import requests
import json
from MysqlAPI import Sql

def get_json(uid):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    data = {
        'uid': uid,
        'scope': "2",
        'output': "json",
        'ak': 'Ll7lskGYsQ8CNKaRxGZa55vDt3l59pnI'
    }

    url = 'http://api.map.baidu.com/place/v2/detail'
    res = requests.get(url, params=data, headers=headers)
    decode_json = res.json()
    return decode_json

# 从数据库中获取uid号
results = Sql.read_city()
# print(results)

for item in results:
    uid = item[0]
    decode_json = get_json(uid)
    # print(decode_json)
    infos = decode_json['result']

    try:
        # name
        uid = infos['uid']
    except:
        uid = None

    try:
        street_id = infos['street_id']
    except:
        street_id = None

    # 获取想要的信息
    try:
        # name
        name = infos['name']
    except:
        name = None

    try:
        address = infos['address']
    except:
        address = None

    try:
        shop_hours = infos['detail_info']['shop_hours']
    except:
        shop_hours = None

    try:
        detail_url = infos['detail_info']['detail_url']
    except:
        detail_url = None


    try:
        content_tag = infos['detail_info']['content_tag']
    except:
        content_tag = None

    # print(uid, street_id, name, address, shop_hours, detail_url, content_tag)
    Sql.insert_park(uid, street_id, name, address, shop_hours, detail_url, content_tag)