import urllib

if __name__ == '__main__':
    url = 'http://news.cctv.com/2019/03/11/ARTIx14nOr8yJm6EwqOlyfcb190311.shtml'

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))