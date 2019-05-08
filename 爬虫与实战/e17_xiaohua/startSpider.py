from scrapy import cmdline

cmdline.execute('scrapy crawl xiaohua -o respBody -t json'.split())