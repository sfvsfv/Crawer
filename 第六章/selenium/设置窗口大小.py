# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 0:13
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(500, 400)

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')
