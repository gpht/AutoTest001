'''
    1.先打开sina网址
    2.获得当前的浏览器窗口句柄
    3.现点击注册，进入注册页面
    4.获得浏览器的所有窗口句柄
    5.再循环遍历窗口句柄，当前的窗口不是登录页
    6.再点击注册的邮箱，将其浏览器关闭
    7.再返回到登录的窗口句柄
    by:gp
    time:2020.5.21
'''

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mail.sina.com.cn/')
current_handle = driver.current_window_handle
time.sleep(3)
driver.find_element_by_link_text('注册').click()
handles = driver.window_handles
for handle in handles:
    if handle != current_handle:
        driver.switch_to.window(handle)
        driver.find_element_by_name('email').send_keys('gp')
        time.sleep(3)
        driver.close()

driver.switch_to.window(current_handle)
time.sleep(3)
driver.find_element_by_id('freename').send_keys('gp')
print('获取执行的浏览器名称：{}'.format(driver.name))
