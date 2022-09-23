# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 20:06
"""
from selenium import webdriver
import os
import time
driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')
file_path = 'file:///' + os.path.abspath('test.html')
driver.get(file_path)

# 定位上传按钮，添加本地文件
driver.find_element_by_id("up_load").send_keys(r'C:\Users\hp\Pictures\test.jpg')

time.sleep(5)
driver.quit()