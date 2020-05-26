'''
    此文件需要导入init.py文件
'''
from init import initTest
class BaiduTest(initTest):
    def test_001(self):
        self.driver.find_element_by_link_text('新闻').click()
        