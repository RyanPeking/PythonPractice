'''
利用selenium执行js脚本
'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# 让输入框有红颜色框脚本
js = "var j=document.getElementById('kw');j.style.border='2px solid red'"

# 调用搜索输入框的脚本
driver.execute_script(js)

# 快照截图
# driver.implicitly_wait(2)
# driver.save_screenshot('/home/tlxy/practice/爬虫与实战/DHTML/img/red_baidu.png')

# 使用js隐藏图片
img = driver.find_element_by_xpath('//div[@id="lg"]/img')

driver.execute_script('$(arguments[0]).fadeOut()', img)
# driver.execute_script('$arguments[0].fadeOut()', img)
# driver.execute_script('img[0].style.display="none')
driver.implicitly_wait(5)
driver.save_screenshot('/home/tlxy/practice/爬虫与实战/DHTML/img/baidu.png')

# 向下滚动到页面底部

driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop:'0px'}, 800)")

driver.implicitly_wait(5)
driver.save_screenshot('/home/tlxy/practice/爬虫与实战/DHTML/img/null_baidu.png')