import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import os

browser = webdriver.Chrome()
# 让窗口最大化
browser.maximize_window()
wait = WebDriverWait(browser, 10)

def index_page(page):
    try:
        print("正在抓取第 %s 页" % page)
        wait.until(EC.presence_of_all_elements_located((By.ID, "dt_1")))
        # print(type(page))
        # print(page)
        if page > 1:
            # 确定页数输入框
            input = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="PageContgopage"]')))
            input.click()
            input.clear()
            input.send_keys(page)
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#PageCont > a.btn_link')))
            submit.click()
            time.sleep(2)
            # print('1')

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
    td_content = element.find_elements_by_tag_name("td")

    # print(td_content)

    lst = []
    for td in td_content:
        lst.append(td.text)

    # 确定表格列数
    col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))

    lst = [lst[i:i+col] for i in range(0, len(lst), col)]

    # 获取详情页面连接
    lst_link = []
    links = element.find_elements_by_css_selector('#dt_1 a.red')
    for link in links:
        url = link.get_attribute('href')
        lst_link.append(url)
    lst_link = pd.Series(lst_link)
    df_table = pd.DataFrame(lst)
    df_table['url'] = lst_link
    return df_table

def write_to_file(df_table, category):
    file_path = '/home/tlxy/practice/爬虫与实战/DHTML/img'
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

    # 设置报表类型
    tables = int(input("请输入查询的报表对应内容数字（1-业绩报表， 2-业绩快报， 3-业绩预告，4-预约披露时间，5-资产负债表，6-利润表，7-现金流量表）："))
    dict_tables = {
        1:'业绩报表',
        2:'业绩快报',
        3:'业绩预告',
        4:'预约披露时间',
        5:'资产负债表',
        6:'利润表',
        7:'现金流量表'
    }
    dict = {
        1: 'yjbb',
        2: 'yjkb/13',
        3: 'yjyg',
        4: 'yysj',
        5: 'zcfz',
        6: 'lrb',
        7: 'xjll'
    }

    category = dict[tables]

    # 设置url地址
    url = 'http://data.eastmoney.com/{}/{}/{}.html'.format('bbsj', date, category)

    # 选择爬取的页数
    start_page = int(input('请输入下载起始页：'))
    nums = input("请输入要下载多少页：")

    print('*'*80)

    # 确定页面最后一页
    browser.get(url)
    try:
        page = browser.find_element_by_css_selector('.next+ a')
        # print("jajdjda")
        # print(page)
    except:
        # page = browser.find_element_by_css_selector('.at+ a')
        pass

    end_page = int(page.text)
    # print(end_page)

    if nums.isdigit():
        end_page = start_page + int(nums)
    elif nums == '':
        end_page = end_page
    else:
        print("页数有误")


    print('准备下载:{}{}'.format(date, dict_tables[tables]))
    print(url)
    yield {
        'url':url,
        'category':dict_tables[tables],
        'start_page':start_page,
        'end_page':end_page
    }

def main(category, page):

    index_page(page)
    df_table = parse_table()
    write_to_file(df_table, category)
    print('第%s抓取完成'%page)
    print('.......................')
    browser.quit()


if __name__ == '__main__':
    for i in set_table():
        category = i.get('category')
        start_page = i.get('start_page')
        end_page = i.get('end_page')

    for page in range(start_page, end_page):
        main(category, page)
    print('抓取完成')