# coding=gbk
"""
作者：川川
@时间  : 2022/3/17 23:56
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
# 添加请求头
options.add_argument(
    'User-Agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36"')
options.add_argument(f"--proxy-server=http://127.0.0.1:7890")  # 添加代理
options.add_argument('--headless')   # 无头模式
options.add_argument('--incognito') # 使用无痕模式
options.add_argument('--disable-javascript')  # 禁用javascript
options.add_argument('blink-settings=imagesEnabled=false') # 如果不加载图片, 网站加载快一些
prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
options.add_experimental_option("prefs", prefs)  # 屏蔽'保存密码'提示框

driver = webdriver.Chrome(r'D:\360安全浏览器下载\chromedriver.exe', options=options)  # 启动时加载配置
driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('川川菜鸟')