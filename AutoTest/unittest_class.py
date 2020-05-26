'''
    学习测试固件只执行一次
    使用setUpClass和tearDownClass的使用
    但是其类上需要加上装饰器@classmethod
'''
import unittest
class doTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        print('setUpClass')

    @classmethod
    def tearDownClass(self):
        print('teardownclass')

    def test_001(self):
        print('test001')

    def test_002(self):
        print('test002')


