# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 17:13
"""
from selenium import webdriver
import time
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')
driver.get("https://cn.bing.com/?mkt=zh-CN")
time.sleep(3)
# 输入内容
driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')
time.sleep(3)
# 回退一次，删除最后一个字
driver.find_element_by_id('sb_form_q').send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 输入一个空格键，添加新的内容python
driver.find_element_by_id('sb_form_q').send_keys(Keys.SPACE)
driver.find_element_by_id('sb_form_q').send_keys('python')
time.sleep(3)
# ctrl+a 全选输入框内容
driver.find_element_by_id("sb_form_q").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# 全选后再ctrl+c复制
driver.find_element_by_id('sb_form_q').send_keys(Keys.CONTROL, 'c')
time.sleep(3)
# 复制好后先把内容删除
driver.find_element_by_id('sb_form_q').send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 删除好后再粘贴回来
driver.find_element_by_id('sb_form_q').send_keys(Keys.CONTROL, 'v')
time.sleep(3)

driver.quit()  # 关闭浏览器
