'''
    这里主要学习浏览器的操作，对javascript的处理
    selenium提供了对javascript的处理，使用方法是excute_script
    在百度搜索中，搜索完后需要滑动支浏览器底部，才能出现下一页；
    以百度搜索为例，滑动浏览器底部或顶部
    1.在百度搜索框中输入内容，点百度一下
    2.将页面滑动到浏览器的底部，找到下一页
    3.找到下一页后，点击下一页
    4.先滑动浏览器到底部
    5.再滑动浏览器到顶部
    save_screenshot:保存当前截图
    get_screenshot_as_file:保存当前屏幕快照保存成.png文件，保存文件的时候可以填写完整的文件路径
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)
# 浏览器滑动到底部js代码
down = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(down)
time.sleep(3)
driver.find_element_by_partial_link_text('下一页').click()
time.sleep(3)
# 浏览器滑动到顶部js代码
up = 'var w=document.documentElement.scrollTop=0'
# 先滑动浏览器到底部
driver.execute_script(down)
time.sleep(3)
# 再滑动浏览器到顶部
driver.execute_script(up)
driver.save_screenshot('baidu.png')
driver.get_screenshot_as_file('D:\PycharmProjects\AutoTest\p.png')
