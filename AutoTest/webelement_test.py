'''
    1.主要来学习webelement的方法在UI自动化中的使用
    by:gp
    time:2020.5.21.16:23
    2.学习clear()的使用
    3.学习refresh()页面的刷新
    4.学习get_attribute的使用：获取输入框中的值或获取输入框中的提示信息
    5.学习is_displayed()是否可见
    7.查看百度输入框是否可编辑，is_enabled()
'''

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
# 在百度浏览器中定位到输入框，输入内容后，清除内容，并页面刷新
# driver.get('https://www.baidu.com')
# time.sleep(2)
# element = driver.find_element_by_id('kw')
# element.send_keys('gp')
# time.sleep(2)
# element.clear()
# time.sleep(2)
# driver.refresh()

driver.get('https://mail.sina.com.cn/#')
element = driver.find_element_by_id('freename')
print('输入框中的提示内容为：'.format(element.get_attribute('placeholder')))

time.sleep(2)
driver.get('https://www.baidu.com')
# element = driver.find_element_by_link_text('关于百度')
# print('关于百度是否可见：{}'.format(element.is_enabled()))
element1 = driver.find_element_by_id('kw')
print('查看百度输入框是否可编辑：'.format(element1.is_enabled()))
