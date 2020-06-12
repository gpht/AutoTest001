
import unittest
import os

def allCases():
    '''
    获取所有测试模块
    :return:
    '''
    suite = unittest.TestLoader().discover(
        start_dir = os.path.dirname(__file__),
        pattern = 'test_*.py',
        top_level_dir = None
    )
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(allCases())