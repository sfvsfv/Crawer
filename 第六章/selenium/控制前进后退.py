# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 0:16
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
#
# driver.get('https://cn.bing.com/?mkt=zh-CN')
#
# driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')
#
# # click点击事件
# b = driver.find_element_by_class_name('search')
# ActionChains(driver).click(b).perform()
#
# c=driver.find_element_by_xpath('//*[@id="b_results"]/li[1]/div[1]/h2/a').click()

from selenium import webdriver
import time

driver = webdriver.Chrome()

# 进入CSDN
first = 'https://www.csdn.net/'
print("进入：%s" % (first))
driver.get(first)
time.sleep(3)
# 进入知乎
second = 'https://www.zhihu.com/'
print("进入%s" % (second))
driver.get(second)
time.sleep(3)
# 后退到CSDN
print("返回到：%s " % (first))
driver.back()
time.sleep(3)
# 前进到知乎
driver.forward()
print('又前进到：%s' % (second))

time.sleep(3)
driver.quit()
