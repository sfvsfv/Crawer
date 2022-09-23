# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 22:49
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.save_screenshot('全屏截图.png')  # 全屏截图
time.sleep(2)
driver.find_element_by_id('sb_form_q').screenshot('元素截图.png')  # 元素截图
time.sleep(2)

driver.quit()
