from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://accounts.douban.com/passport/login'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(4)

driver.save_screenshot('douban_index.png')

# captcha = input("please input your code:")

driver.find_element_by_xpath("//a[@class='link-account']").click()
driver.find_element_by_id("username").send_keys("wushunyan@163.com")
driver.find_element_by_id("password").send_keys("wsy2008401")
# driver.find_element_by_id("code").send_keys(captcha)

driver.find_element_by_class_name("btn btn-account").click()

time.sleep(5)

driver.save_screenshot("logined.png")

with open("douban_home.html", "w", encoding='utf-8') as f:
    f.write(driver.page_source)

driver.quit()

