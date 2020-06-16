'''
    主要验证：新浪登录页面，用户名和密码均为空时，显示的错误提示信息
'''
from selenium import  webdriver
import  unittest

class sinaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_sina(self):
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[2]/a').click()
        self.driver.find_element_by_id('freename').send_keys('')
        self.driver.find_element_by_id('freepassword').send_keys('')
        self.driver.find_element_by_link_text('登录').click()
        divError = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEqual(divError,'请输入邮箱名')

if __name__ == '__main__':
    unittest.main(verbosity=2)
