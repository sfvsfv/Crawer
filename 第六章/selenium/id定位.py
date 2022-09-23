# coding=gbk
"""
作者：川川
@时间  : 2022/3/15 22:09
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')
