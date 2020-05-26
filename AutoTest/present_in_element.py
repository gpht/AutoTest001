'''
    1.从selenium中导入webdriver
    2.从selenium.webdriver中导入webdriverwait
    3.从selenium.webdriver中导入webdriverwait中的依赖expected_conditions
    4.从selenium.webdriver by中导入By
    5.text_to_be_present_in_element'用于验证文本信息或错误的文本提示'
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mail.sina.com.cn/#')
driver.implicitly_wait(30)
driver.find_element_by_id('freename').send_keys('')
driver.find_element_by_id('freepassword').send_keys('')
driver.find_element_by_link_text('登录').click()
WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'), '请输入邮箱名'))
