'''
    学习关于键盘的操作
    1.keys模块中的Keys类
    2.from selenium.webdriver.common.keys import Keys
    3.以百度为例，先在百度输入框中输入搜索字符
    4.然后将输入框里面的内容选中,ctrl+a；ctrl+c进行复制
    5.再用backspace进行删除
    6.再打开bing首页
    7.将内容粘贴到bing输入框中，ctrl+v
    by:gp
    time:2020.5.25:15：40
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('https://www.baidu.com')
binput = driver.find_element_by_id('kw')
binput.send_keys('selenium')
time.sleep(3)
binput.send_keys(Keys.CONTROL, 'a')
time.sleep(3)
binput.send_keys(Keys.CONTROL, 'c')
time.sleep(3)
driver.get('https://cn.bing.com/')
time.sleep(3)
bing = driver.find_element_by_class_name('b_searchbox')
bing.send_keys(Keys.CONTROL, 'v')
time.sleep(3)