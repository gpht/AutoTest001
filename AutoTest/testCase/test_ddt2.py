'''
    把数据放在@data中，可以把@data中的数据分享到一个方法中
    实现把@data中的数据存储在列表里，@data调用函数getData时，前面加了一个*
    因为@data要求数据类型是元组，加*后便把getData函数返回的数据列表类型变为元组类型
'''
import unittest
from ddt import data, unpack, ddt
from selenium import webdriver


def getData():
    return [
        ['','',u'请输入邮箱名'],
        ['', 'password', u'请输入邮箱名'],
        ['email', '', u'您输入的邮箱名格式不正确']
    ]

@ddt
class sinaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    @data(*getData())
    @unpack
    def test_sina(self, username, password, result):
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        self.driver.find_element_by_link_text('登录').click()
        dirError = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'
        ).text
        self.assertEqual(dirError, result)


if __name__ == '__main__':
    unittest.main(verbosity=2)





