import unittest
from selenium import webdriver
from ddt import data, unpack, ddt

@ddt
class sinaTest(unittest.TestCase):
    '''使用@classmethod，让浏览器只开一次'''
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get('https://mail.sina.com.cn/')
    #     cls.driver.implicitly_wait(30)
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    '''setUp,tearDown,浏览器每次都会执行一次'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    '''data表示元组的列表数据'''
    @data(('','',u'请输入邮箱名'), ('','password', u'请输入邮箱名'), ('email','',u'您输入的邮箱名格式不正确'))

    '''unpack表示用来解压元组到多个参数'''
    @unpack
    def test_001(self, email, password, result):
        self.driver.find_element_by_id('freename').send_keys(email)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        self.driver.find_element_by_link_text('登录').click()
        dirError = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEqual(dirError, result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
