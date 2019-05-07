from selenium import webdriver
import time

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

driver = webdriver.Chrome()
driver.get(url)

js = 'document.body.scrollTop=10000'
time.sleep(3)

driver.save_screenshot('douban1.png')

driver.execute_script(js)
time.sleep(3)

driver.save_screenshot('douban2.png')
driver.quit()

