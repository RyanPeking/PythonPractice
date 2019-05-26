# 导入webdriver
from selenium import webdriver
# 若想调用键盘按键需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器对象   executable_path=指定PhantomJS路径
driver = webdriver.Chrome()

# get方法
driver.get("https://www.baidu.com")

# 生成当前页面快照并保存
# driver.save_screenshot('/home/tlxy/tulingxueyuan/爬虫与实战/DHTML/img/index.png')

# print(driver.title)

# 模拟百度搜索
# id='kw'
driver.find_element_by_id('kw').send_keys('python')

# id=su
driver.find_element_by_id('su').click()

time.sleep(5)

driver.save_screenshot('python.png')

# 打印当前页面源码
# print(driver.page_source)

# 获取当前页面cookie信息
# print(driver.get_cookies())

# 发送ctrl+x剪切输入框中的内容
driver.find_element_by_id('kw').clear()

# driver.save_screenshot('/home/tlxy/tulingxueyuan/爬虫与实战/DHTML/img/python.png')

# 再次输入内容
driver.find_element_by_id('kw').send_keys(u'北京图灵学院')
# driver.save_screenshot('/home/tlxy/tulingxueyuan/爬虫与实战/DHTML/img/python2.png')

# 获取当前url地址
print(driver.current_url)
driver.quit()


'''
定位元素：
    find_element_by_id
'''

