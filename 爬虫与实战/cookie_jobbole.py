from urllib import request, error, parse
from http import cookiejar
import json

def login():
    url = "http://www.jobbole.com/wp-admin/admin-ajax.php"

    data = {
        "action":"user_login",
        "user_login":"dfasd",
        "user_pass":"dfd",
        "remember_me":1,
        "redirect_url":"http://www.jobbole.com",
    }

    data = parse.urlencode(data).encode()

    f = r'jobbole_cookie.txt'

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Connection": "keep-alive"
    }

    cookie_handler = cookiejar.MozillaCookieJar(f)

    http_handler = request.HTTPCookieProcessor(cookie_handler)

    opener = request.build_opener(http_handler)

    req = request.Request(url, data=data, headers=headers)

    try:
        rsp = opener.open(req)

        cookie_handler.save(f, ignore_discard=True, ignore_expires=True)

        html = rsp.read().decode()
        print(html)

    except error.URLError as e:

        print(e)

def getinfo():
    url = ""

    f =

if __name__ == '__main__':
    login()