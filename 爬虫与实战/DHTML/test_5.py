from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://movie.douban.com/')

# 第一次
driver.save_screenshot('/home/tlxy/practice/爬虫与实战/DHTML/img/dou_1.png')
# 向下滚动10000像素
js = 'document.body.scrollTop=10000'
# js = 'var q=document.documentElement.scollTop=10000'

driver.execute_script(js)
time.sleep(5)
driver.save_screenshot('/home/tlxy/practice/爬虫与实战/DHTML/img/dou_2.png')
driver.quit()