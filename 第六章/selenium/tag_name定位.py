# coding=gbk
"""
作者：川川
@时间  : 2022/3/15 22:33
"""
from selenium import webdriver  # 导入模块

browser = webdriver.Chrome()  # 初始化
browser.get('https://www.taobao.com')  # get请求淘宝网页

biao = browser.find_element_by_tag_name('input')
print(biao)
