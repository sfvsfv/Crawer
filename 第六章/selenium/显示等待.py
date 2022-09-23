# coding=gbk
"""
作者：川川
@时间  : 2022/3/16 23:50
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #导入WebDriverWait类
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get请求
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]'))
    )
    element.send_keys('python')
finally:
    driver.quit()
