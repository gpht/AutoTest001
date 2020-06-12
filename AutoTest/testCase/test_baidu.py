'''
    测试百度的title是否正确
'''
import unittest
from selenium import webdriver

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
    def test_baidu_title(self):
        '''测试百度首页的title是否显示正确'''
        self.assertEqual(self.driver.title,'百度一下，你就知道')

if __name__ == '__main__':
    unittest.main(verbosity=2)
