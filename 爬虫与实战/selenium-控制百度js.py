from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 美化输入框
js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"

# 执行代码
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot('redbaidu.png')

# js隐藏相应元素，隐藏logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()', img)

# 滚动滑动条到最底下
js = "$('.scroll_top').click(function(){$('html, body').animate({scrollTop:'0px'}, 800)});"

time.sleep(3)
driver.save_screenshot("nullbaidu.png")