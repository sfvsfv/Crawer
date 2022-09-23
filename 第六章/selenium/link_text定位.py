# coding=gbk
"""
作者：川川
@时间  : 2022/3/15 22:25
"""
# from selenium import webdriver  # 导入模块
#
# browser = webdriver.Chrome()  # 初始化
# browser.get('https://www.taobao.com')  # get请求淘宝网页
#
# href = browser.find_element_by_link_text('女装')  # 文本定位女装
# print(href)

from selenium import webdriver  # 导入模块

browser = webdriver.Chrome()  # 初始化
browser.get('https://www.taobao.com')  # get请求淘宝网页

href = browser.find_element_by_link_text('零食')  # 文本定位零食
print(href)