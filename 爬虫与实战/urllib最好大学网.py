from urllib import request
from lxml import etree

url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'

resp = request.urlopen(url)

html = resp.read().decode()

# print(html)

html = etree.HTML(html)

schools = html.xpath('//tr[@class="alt"]')

for school in schools:
    # ranking = school.xpath('./td')[0].text
    ranking = school.xpath('./td/text()')[0]
    print(ranking)