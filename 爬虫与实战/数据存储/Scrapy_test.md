# scrapy框架学习
    - 框架
    - 爬虫变得相当简单
    - 异步网络框架Twisted(默认自带多线程）
    - 提供各种接口以及中间件
    
## scrapy长什么样子
    - Spider(爬虫)
        - 1.初次发起我们的爬虫请求
        - 2.解析response得到的数据，若是url地址，将url传递给调度器进行循环爬取，若是数据传递给item pipeline
    - Scheduler(调度器)
        - 负责接收引擎发送过来的request请求，在此处进行队列的整合
    - downloader(下载器)
        - 主要负责从互联网进行网页内容请求
    - Item Pipeline(数据存储)
        - 主要负责spider中得到数据（item），进行数据的处理与保存
    - Scrapy Engine(引擎)
        - 负责spider，Itempipeline，scheduler，downloader之间的协调和通信/数据传送
    - Download Middlewares
        - 下载中间件，主要进行下载功能的扩展
    - Spider Middlewares
        - 主要进行扩展spider功能/扩展与引擎之间的通信功能
        
        
        
## scrapy框架的安装
    - 搭建虚拟环境
        - 查看所有的虚拟环境
            - conda env list
        - 创建虚拟环境
            - conda create -n xxx(名字) python=3.6
        - 创建完成激活虚拟环境
            - linux:
                - source activate xxx
            - win:
                - activate xxx
        - 安装scrapy框架
            - pip install scrapy
            
            
    - 环境搭建问题
        - pip instal pywin32
        - pip install Twisted
        - pip install scrapy
        
        
## 创建第一个scrapy项目
        
    # 创建项目
        - scrapy startproject projectName 
    # 创建爬虫实例
        - scrapy genspider Spidername domain.com
        
    # 注意：
        - 爬虫名称与项目名称不能相同