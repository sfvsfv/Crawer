# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 2:51
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get请求

driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('川川菜鸟')
driver.find_element_by_id('sb_form_q').submit()  # 提交
time.sleep(2)
# 清空重新输入
driver.find_element_by_id('sb_form_q').clear()
driver.find_element_by_id('sb_form_q').send_keys('python')

time.sleep(2)
# 定位元素才能执行操作
driver.find_element_by_id('sb_form_q').submit()
