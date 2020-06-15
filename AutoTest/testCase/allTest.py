
import unittest
import os
import time
import HTMLTestRunner


def allCases():

    '''
    获取所有测试模块
    :return:
    '''

    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def getNowTime():
    '''获取当前的时间'''
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))


def run():
    fileName = os.path.join(os.path.dirname(__file__), 'report', getNowTime()+'_report.html')
    fp = open(fileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试报告',
        description='UI自动化测试报告详细信息'
    )
    runner.run(allCases())
    fp.close()


if __name__ == '__main__':
    run()