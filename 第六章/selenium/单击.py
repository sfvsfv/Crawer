# coding=gbk
from selenium import webdriver
import time
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')
driver.get("https://cn.bing.com/?mkt=zh-CN")
driver.maximize_window()
time.sleep(3)
# 定位的元素
su = driver.find_element_by_class_name('search')
# 定位好再执行
ActionChains(driver).context_click(su).perform()
