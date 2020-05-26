'''
    说明：让固件只执行一次
    1.对于有些功能来说，如，在百度中点击新闻，后跳转到一个页面，
    后面还想点击百度首页的地图，那么在第一个测试用例中就需要进行处理，让其回到百度首页后，
    第二条测试用例才可以在百度首页中看到地图。不然，会报错。
    针对这个功能，可以在第一条测试用例里面，融入到多窗口的概念，点击首页中的新闻后，
    让其回到第一个窗口，再点击首页中的地图
    2.也可以使用稍微简单一点的，让浏览器回到第一个页面，用driver.back()

'''
from selenium import webdriver
import unittest
import time
class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://www.baidu.com')
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        # 不退出浏览器，是为了更好的看清楚自动化执行过程
        pass

    # def test_001(self):
    #     current_window = self.driver.current_window_handle
    #     self.driver.find_element_by_link_text('新闻').click()
    #     handles = self.driver.window_handles
    #     for handle in handles:
    #         if handle != current_window:
    #             handle = current_window
    #             time.sleep(3)

    def test_001(self):
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()#浏览器返回到第一个页面

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()
        print('test_002')
