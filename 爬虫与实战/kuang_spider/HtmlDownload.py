import requests

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",}

        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            res.encoding = 'utf-8'
            return res.text

        return None