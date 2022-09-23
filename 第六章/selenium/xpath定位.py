# coding=gbk
"""
作者：川川
@时间  : 2022/3/15 22:34
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get请求

driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('川川菜鸟')
# click点击事件
b = driver.find_element_by_class_name('search')
ActionChains(driver).click(b).perform()
