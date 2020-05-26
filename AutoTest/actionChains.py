'''
    1.鼠标的操作的方法
    2.在selenium中常用鼠标的操作方法，主要在action_chains模块的ActionChains类中
    3.from selenium.webdriver.common.action_chains import ActionChains
    4.鼠标右击操作：context_click
    5.鼠标双击操作：double_click
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
# 实例化ActionChains
actionChains = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('https://www.baidu.com')

# so = driver.find_element_by_id('kw')
# # 在百度输入框中进行鼠标右击操作
# actionChains.context_click(so).perform()

driver.find_element_by_id('kw').send_keys('selenium')
# 定位百度一下按钮
element = driver.find_element_by_id('su')
actionChains.double_click(element).perform()


time.sleep(3)