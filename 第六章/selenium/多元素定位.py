# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 17:55
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')

driver.get('https://cn.bing.com/?mkt=zh-CN')

# driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')

tag_names = driver.find_elements_by_tag_name("input")[0].send_keys('python')
# for tag in tag_names:
#     print(tag)
time.sleep(5)
driver.quit()
