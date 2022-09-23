# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 16:56
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')
time.sleep(2)
#定位搜索按钮
su = driver.find_element_by_class_name('search')
# 定位好再执行
ActionChains(driver).double_click(su).perform()
