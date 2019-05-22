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
        'ak': 'Ll7lskGYsQ8CNKaRxGZa55vDt3l59pnI'
    }

    url = 'http://api.map.baidu.com/place/v2/search?'
    res = requests.get(url, params=data, headers=headers)
    decode_json = res.json()
    return decode_json

# province_list = ['四川省', '山东省',  '广东省',
#                  '宁夏省']
# for each_province in province_list:
#     decode_json = get_json(each_province)
#     for each_city in decode_json['results']:
#         print(each_city)
#         city = each_city['name']
#         num = each_city['num']
#         output = '\t'.join([city, str(num)])+'\n'
#         with open('cities.txt', 'a', encoding='utf-8') as f:
#             f.write(output)

decode_json = get_json("南充市")
print(decode_json)