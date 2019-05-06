'''
爬取腾讯招聘的网站
'''

from bs4 import BeautifulSoup
from urllib import request

def qq():

    url = ""
    rsp = request.urlopen(url)
    html = rsp.read()

    soup = BeautifulSoup(html, 'lxml')

    tr1 = soup.select("tr[class='even']")
    tr2 = soup.select("tr[class='odd']")
    trs = tr1 + tr2

    for tr in trs:
        name = tr.select("td a")[0]