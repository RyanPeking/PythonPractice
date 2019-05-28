from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.PhantomJS()
# 让窗口最大化
browser.maximize_window()
wait = WebDriverWait(browser, 10)

def index_page(page):
    print("正在抓取第：%s 页"%page)
    wait.until(EC.presence_of_all_elements_located((By.ID, "")))
    if page