# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 0:00
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get请求

driver.implicitly_wait(10)  # 隐式等待10秒

driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('川川菜鸟')
