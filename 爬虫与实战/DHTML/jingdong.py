from selenium import webdriver
import pymongo
# 负责条件的发起，触发
from selenium.webdriver.support import expected_conditions as EC
'''
设置等待
selenium主要提供隐性等待和显性等待
driver:传入webdriver的实例
 timeout：超时时间，等待的最长时间（考虑隐性等待时间）
 poll_frequency=POLL_FREQUENCY：调用until或者until_not中的方法的间隔时间，默认0.5秒
 ignored_exceptions=None：忽略异常，如果在调用until或者until_not的过程中抛出元祖中的异常，则不中断代码，继续执行
                                    如果是元祖外的异常，则中断代码，抛出异常
'''
from selenium.webdriver.support.ui import WebDriverWait
import time
# 捕获超时异常
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 启动浏览器
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 50)

# 连接数据库
client = pymongo.MongoClient('192.168.61.98', 27017)
db = client.jd_computer
collection = db.computer


def to_mongodb(data):
    # 数据存储
    try:
        collection.insert(data)
        print("Insert the data successfully")

    except:
        print("Insert the data failed")

def search():
    browser.get('https://www.jd.com/')
    try:
        # 查找搜索框与搜索按钮，输入信息后点击
        inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#key")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button")))
        # print(inputs)
        inputs[0].send_keys('笔记本')
        submit.click()

        # 查找笔记本按销量
        button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_selector > div:nth-child(2) > div > div.sl-value > sl-v-list > ul > li:nth-child(1) > a")))
        button1.click()
        button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_filter > div.f-line top > div.f-sort > a:nth-child(2) > span")))
        button2.click()

        # 获取总页数
        page = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > em:nth-child(1) > b")))
        return page[0].text


    except TimeoutException:
        search()

# 获取下一页
def next_page(page_num):
    # 滑动网页到底部，加载所有商品信息
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    html = browser.page_source
    parse_html(html)
    while page_num == 101:
        exit()
    # 查找下一页按钮，并点击
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.pn-next > em")))
    button.click()


def parse_html(html):


if __name__ == '__main__':
    search()