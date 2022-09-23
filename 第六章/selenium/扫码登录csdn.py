# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 21:51
"""
from selenium import webdriver
import time
import json
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')

driver.get('https://passport.csdn.net/login?code=public')

flag = True
while flag:
    try:
        # driver.find_element_by_xpath("//a[@class='header-entry-avatar']")
        driver.find_element_by_class_name('hasAvatar')
        flag = False
        print("已登录，现在为您保存cookie...")
    except NoSuchElementException as e:
        time.sleep(3)
with open('cookies.txt', 'w', encoding='u8') as f:
    json.dump(driver.get_cookies(), f)

time.sleep(3)
driver.close()