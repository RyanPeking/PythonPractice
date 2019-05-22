import requests
import json
from MysqlAPI import Sql

city_list = []
with open('/home/tlxy/practice/爬虫与实战/数据存储/baiduMap_API/cities.txt', 'r', encoding='utf-8') as f:
    for eachline in f:
        # print(eachline)
        fileds = eachline.split('\t')
        city = fileds[0]
        city_list.append(city)

# print(city_list)
# print(len(city_list))


def get_json(loc, page_num=0):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    data = {
        'query': "公园",
        'region': loc,
        'scope': "2",
        'page_size': 20,
        'page_num':page_num,
        'output': "json",
        'ak': 'Ll7lskGYsQ8CNKaRxGZa55vDt3l59pnI'
    }

    url = 'http://api.map.baidu.com/place/v2/search?'
    res = requests.get(url, params=data, headers=headers)
    decode_json = res.json()
    return decode_json


for eachcity in city_list:
    flag = True
    page_num = 0
    while flag:
        decode_json = get_json(eachcity, page_num)
        # print(eachcity, page_num)
        if decode_json['results']:
            for each_one in decode_json['results']:
                # print(each_one)
                try:
                    park = each_one['name']
                except:
                    park = None

                try:
                    location_lat = each_one['location']['lat']
                except:
                    location_lat = None

                try:
                    location_lng = each_one['location']['lng']
                except:
                    location_lng = None

                try:
                    address = each_one['address']
                except:
                    address = None

                try:
                    street_id = each_one['street_id']
                except:
                    street_id = None

                try:
                    uid = each_one['uid']
                except:
                    uid = None

                print(park, location_lat, location_lng, address, street_id, uid)
                Sql.insert_city(eachcity, park, location_lat, location_lng, address, street_id, uid)

            page_num += 1
        else:
            flag = False