#coding=utf-8
import unittest
from selenium import webdriver
import os
import time


def getData(index):
    with open(os.path.join(os.path.dirname(__file__), 'sina.txt'), 'r', encoding='utf-8') as f:
        d = f.readlines()
        print('d', d[index])
        return d[index]


class testSina(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def sina_login(self, username, password):
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        self.driver.find_element_by_link_text('登录').click()

    def assertDir(self):
        dirError = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'
        )
        print('dir', dirError.text)
        return (dirError.text)

    def test_username_password_null(self):
        '''email和password均为空'''
        self.sina_login(getData(0), getData(0))
        self.assertEqual(self.assertDir(), getData(2))
        time.sleep(2)

    def test_username_null(self):
        '''email为空，密码不为空'''
        self.sina_login(getData(0), getData(1))
        self.assertEqual(self.assertDir(), getData(2))
        time.sleep(2)


    def test_username_format(self):
        '''测试email的格式不正确的提示信息'''
        self.sina_login(getData(1), getData(1))
        self.assertEqual(self.assertDir(), getData(3))
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
