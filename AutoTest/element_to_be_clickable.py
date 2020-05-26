'''
    1.需要导入selenium的webdriver
    2.还要导入element_to_be_clickable所依赖的模块
    3.实现的是百度浏览器的搜索输入框加载出来后，可进入输入，用element_to_be_clickable来实现
    4.from selenium.webdriver.support.ui import WebdriverWait
    5.from selenium.webdriver.support import expected_conditions
    6.from selenium.webdriver.common.by import By
    by:gp
    time:2020.5.22:14:58
'''
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.implicitly_wait(30)
so = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'kw')))
so.send_keys('selenium')
