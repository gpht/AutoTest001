'''
    将测试固件webdriver的初始条件写入到init.py文件中
'''
from selenium import webdriver
import unittest
class initTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.quit()