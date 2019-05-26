'''
模拟豆瓣登录
url = 'https://www.douban.com/'
'''

from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.implicitly_wait(5)


driver.find_element_by_class_name('account-tab-account on').click()
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('')
driver.find_element_by_class_name('btn btn-account').click()
driver.implicitly_wait(4)

with open('/home/tlxy/tulingxueyuan/爬虫与实战/DHTML/img/douban.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
