# coding=gbk
"""
作者：川川
@时间  : 2022/3/16 23:18
"""
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入By类

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element(By.ID, 'sb_form_q').send_keys('python')
