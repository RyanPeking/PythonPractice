'''
python对json文件操作分为编码与解码
dumps   字符串
dump    json对象  可以通过fp文件流写入

解码:
    loads
    load

'''
# import json
#
# str = "[{'username': 'daochang', 'age':18}]"
# # print(type(str))
# json_str = json.dumps(str, ensure_ascii=False)
# print(json_str)
# print(type(json_str))
# new_str = json.loads(json_str)
# print(new_str, type(new_str))

import requests, json
from bs4 import BeautifulSoup
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

r = requests.get('http://www.seputu.com/', headers=header)
# print(r.text)

soup = BeautifulSoup(r.text, 'lxml')

for mulu in soup.find_all(class_='mulu'):
    print(mulu)

