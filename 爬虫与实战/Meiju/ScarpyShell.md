# Scrapy Shell
    - 交互终端
    - python开发环境下
    - ipython
## 启动Scrapy Shell
    - scrapy shell 'www.baidu.com'
    - response.body.decode('utf8')


## Scrapy提供的选择器
    - 基本选择器
        - xpath():传入xpath表达式，得到selector list
        - extract():序列化该节点为unicode字符串列表
        - css():传入css表达式，返回selector list，语法规则同BeautifulSoup
        - re():传入正则表达式进行规则匹配
        - http://www.scrapyd.cn/doc/
        
## 
    - scrapy crawl mySpider -o mingyan.json
    
    
## scrapy日志等级
    - DEBUG：调试信息
    - INFO：一般信息
    - WARNING：警告信息
    - ERROR：一般错误
    - CRITICAL:严重错误
## scrapy日志设置
    - LOG_ENABLED:默认TRUE
    - LOG_ENCODING:编码类型，默认为utf-8
    - LOG_FILE:日志的输入文件，默认当前路径下，可改
    - LOG_LEVEL：默认为DEBUG