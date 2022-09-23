# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 22:03
"""
import json

from selenium import webdriver

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe')


def newcookie(cookies):
    domain2 = {}  # 做一个域到cookie的映射
    for cookie in cookies:
        domain = cookie['domain']
        if domain in domain2:
            domain2[domain].append(cookie)
        else:
            domain2[domain] = []
    maxCnt = 0
    ansDomain = ''
    for domain in domain2.keys():
        cnt = len(domain2[domain])
        if cnt > maxCnt:
            maxCnt = cnt
            ansDomain = domain
    ansCookies = domain2[ansDomain]
    return ansCookies


with open('cookies.txt', 'r', encoding='u8') as f:
    cookies = json.load(f)

cookies = newcookie(cookies)

driver.get("https://passport.csdn.net/login?code=public")
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://passport.csdn.net/login?code=public")
driver.refresh()
