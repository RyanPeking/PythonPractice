from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://www.jianshu.com/p/57e0b5f26438')

driver.implicitly_wait(5)

author = driver.find_element_by_xpath('//span[@class="name"]/a').text

data = driver.find_element_by_xpath('.//span[@class="publish-time"]').text

word = driver.find_element_by_xpath('//span[@class="wordage"]').text.strip('字数 ')

print(author, data, word)


