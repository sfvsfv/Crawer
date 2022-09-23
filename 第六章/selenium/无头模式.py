# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 23:53
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
# 添加请求头
options.add_argument(
    'User-Agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36"')

options.add_argument('--headless')   # 无头模式

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe', options=options)  # 启动时加载配置
driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')
