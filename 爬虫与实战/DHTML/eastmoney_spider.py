import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import os

browser = webdriver.PhantomJS()
# 让窗口最大化
browser.maximize_window()
wait = WebDriverWait(browser, 10)

def index_page(page):
    try:
        print("正在抓取第：%s 页" % page)
        wait.until(EC.presence_of_all_elements_located((By.ID, "dt_1")))
        if page > 1:
            # 确定页数输入框
            input = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="PageContgopage"]')))
            input.click()
            input.clear()
            input.send_keys(page)
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#PageCont > a.btn_link')))
            submit.click()
            time.sleep(2)

        # 确认是否成功跳转
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#PageCont > span.at'),str(page)))
    except Exception:
        return None

def parse_table():
    # 提取表格内容
    # element = wait.until(EC.presence_of_all_elements_located((By.ID, "dt_1")))
    # 第二种
    element = browser.find_element_by_css_selector("#dt_1")
    # 提取表格内容
    td_content = element.find_element_by_tag_name("td")

    lst = []
    for td in td_content:
        lst.append(td.text)

    # 确定表格列数
    col = len(element.find_element_by_css_selector('tr:nth-child(1) > td'))

    lst = [lst[i:i+col] for i in range(0, len(lst), col)]

    # 获取详情页面连接
    lst_link = []
    links = element.find_element_by_css_selector('#dt_1 a.red')
    for link in links:
        url = link.get_attribute('href')
        lst_link.append(url)
    lst_link = pd.Series(lst_link)
    df_table = pd.DataFrame(lst)
    df_table['url'] = lst_link
    return df_table

def write_to_file(df_table, category):
    file_path = '/home/tlxy/tulingxueyuan/爬虫与实战/DHTML/img'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    os.chdir(file_path)
    df_table.to_csv('{}.csv'.format(category), mode='a', encoding='utf-8', index=0, header=0)

def set_table():
    print('*'*80)
    print('\t\t\t\t东方财富网报表下载')
    print('..........................')
    # 设置财务报表获取时间
    year = int(float(input("请输入要查询的年份：")))
    while (year < 2007 or year > 2019):
        year = int(float(input("请重新输入：")))

    quarter = int(float(input("请输入您要查询的季度（1：1季度,2：年中报， 3:3季度， 4：年度）：")))
    while (quarter < 1 or quarter > 4):
        quarter = int(float(input("请重新输入您要查询的季度（1：1季度,2：年中报， 3:3季度， 4：年度）：")))

    quarter = '{:02d}'.format(quarter*3)
    date = '{}{}'.format(year, quarter)

