'''
anacobda 清华软件源
安装pandas,numpy
利用pandas保存数据
url = 'www.cbooo.cn'
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://www.cbooo.cn/year?year=2019'
datas = requests.get(url).text
# print(datas)
soup = BeautifulSoup(datas, 'lxml')
movies_table = soup.find('table', {'id': "tbContent"})
movies = movies_table.find_all('tr')
# print(movies)
names = [tr.find_all('td')[0].a.get('title') for tr in movies[1:]]
# print(names)

hrefs = [tr.find_all('td')[0].a.get('href') for tr in movies[1:]]
# print(hrefs)

types = [tr.find_all('td')[1].string for tr in movies[1:]]
# print(types)

boxoffice = [int(tr.find_all('td')[2].string) for tr in movies[1:]]
# print(boxoffice)

mean_price = [int(tr.find_all('td')[3].string) for tr in movies[1:]]

mean_people = [int(tr.find_all('td')[4].string) for tr in movies[1:]]

countries = [tr.find_all('td')[5].string for tr in movies[1:]]

times = [tr.find_all('td')[6].string for tr in movies[1:]]

def getInfo(url):
    datas = requests.get(url).text
    soup = BeautifulSoup(datas, 'lxml')
    director = soup.select('dl.dltext dd')[0].get_text()
    return director

directors = [getInfo(url).strip('\n') for url in hrefs]
# print(directors)

df = pd.DataFrame({
    'name':names,
    'href':hrefs,
    'type':types,
    'boxoffice':boxoffice,
    'mean_price':mean_price,
    'mean_people':mean_people,
    'countries':countries,
    'time':times,
    'director':directors

})
# print(df)

# 数据存储
df.to_csv('movies.csv')
x = df.groupby('type').agg({'boxoffice':["count", "mean"]})
print(x)



df_2 = pd.read_csv('movies.csv')