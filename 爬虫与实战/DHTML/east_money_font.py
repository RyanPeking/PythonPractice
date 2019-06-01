import re

import requests

url = 'http://data.eastmoney.com/bbsj/201903/yjbb.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
res = requests.get(url, headers=headers)
html = res.text
# print(html)

html = html.replace('&#xE712;', '0')
print(html)

pattern = re.compile(r'"basiceps":"(.*?);",')
result = pattern.findall(html)
print(result)
print(len(result))
