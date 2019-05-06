from selenium import webdriver
from bs4 import BeautifulSoup

class Douyu():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.douyu.com/directory/columnRoom/syxx'

    def douyu(self):
        self.driver.get(self.url)


        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')

            titles = soup.find_all('h3', {'class':'DyListCover-intro'})
            nums = soup.find_all('span', {'class':'DyListCover-hot is-template'})

            for title, num in zip(titles, nums):
                print("房间{0} 总共观赏人数{1}".format(title.get_text().strip(), num.get_text().strip()))
            print("="*30)

    def destr(self):
        self.driver.quit()

if __name__ == '__main__':
    douyu = Douyu()
    douyu.setUp()
    douyu.douyu()
    print("")
    douyu.destr()