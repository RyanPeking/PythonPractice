# 1.爬虫简介
- 爬虫定义：
- 两个特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- Python网络包简介
    - Python2.x：
    - Python3.x：
    - Python2：urllib和urllib2配合使用，或者requests
    - Python3：urllib，requests
    
# 2.urllib
- 包含模块
    - urllib，request：打开和读取url
    - urllib.error：包含urllib.request产生的常见的错误
        使用try捕捉
    - urllib.parse:包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
    - 案例v1
    
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是，可能有误
    - 需要安装，1.source activate spider 2.conda install chardet
    - 案例v2
- urlopen的返回对象
    - 案例v3
    - geturl:返回请求对象的url
    - info：请求