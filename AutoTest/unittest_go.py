'''
    主要学会使用unittest框架
'''
import unittest
from selenium import webdriver

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_so(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_baidu_di(self):
        self.driver.find_element_by_link_text('地图').click()

if __name__ =='__main__':
    if __name__ == '__main__':
        unittest.main(verbosity=2)
