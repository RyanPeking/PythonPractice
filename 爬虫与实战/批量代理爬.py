

from urllib import request, error
import random


if __name__ == '__main__':
    proxy_list = [
        {"http": "117.127.0.202:80"},
        {"http": "119.187.120.118:8060"},
        {"http": "180.175.170.137:8060"},
        {"http": "119.190.188.239:8060"},
    ]
    proxy_handler_list = []
    for proxy in proxy_list:
        proxy_handler = request.ProxyHandler(proxy)
        proxy_handler_list.append(proxy_handler)

    opener_list = []
    for proxy_handler in proxy_handler_list:
        opener = request.build_opener(proxy_handler)
        opener_list.append(opener)
    #
    # for opener in opener_list:
    #     request.install_opener(opener)

    url = "http://www.baidu.com"

    try:
        opener = random.choice(opener_list)
        request.install_opener(opener)

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
