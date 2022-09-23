# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 1:30
"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver.get('https://www.taobao.com/')  # get请求

driver.find_element_by_id('q').send_keys('华为手机')
time.sleep(3)
# driver.find_element_by_id('q').clear()
driver.find_element_by_class_name('btn-search').click()
time.sleep(2)
driver.find_element_by_name('fm-login-id').send_keys('15682448658')  # 输入淘宝账号
time.sleep(2)
driver.find_element_by_name('fm-login-password').send_keys('zxcvbnm123')  # 输入淘宝密码
time.sleep(2)

# try:
# 找到滑块
hua = driver.find_element_by_id('nc_1_n1z')
# 判断滑块是否可见
if hua.is_displayed():
    ActionChains(driver).click_and_hold(on_element=hua).perform()
    # 往右边移动258个位置
    ActionChains(driver).move_by_offset(xoffset=258, yoffset=0).perform()
    # 松开鼠标
    ActionChains(driver).pause(0.5).release().perform()
else:
    print('出错了')
# except:
#     pass
