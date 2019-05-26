'''
动态HTML

JS  一般嵌入在多媒体文件中，网页游戏

JQuery  在源代码中包含JQuery入口
        <script type="text/javascript" src="http://..../jquery-1.11.1.min.js?v=34234></script>

Ajax    异步加载

DHTML   类似于Ajax   （Dynamic HTML）


如何解决这类页面的数据抓取
    1.直接从js中采集内容（费时费力）
    2.利用python的第三方库直接运行js
    3.selenium && PhantomJS
'''

'''
selenium
    是一个web的自动化测试工具
    可以指定命令自动操作
    让浏览器自动加载数据，截屏，判断网站上某些动作是否发生
    
    安装
        - pip install selenium==2.48.0
        - https://pypi.org/simple/selenium/
        
    参考文档
        - https://selenium-python.readthedocs.io/index.html
'''

'''
PhantomJS
    基于Webkit的无界面浏览器
    selenium + PhantomJS
    
    安装：
        - http://phantomjs.org/download.html
        - 将安装路径添加到环境变量
'''