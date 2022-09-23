# coding=gbk
"""
作者：川川
@时间  : 2022/3/15 4:44
"""
import requests
from lxml import etree

#我们这次是使用etree来获取的所有二手房的title，也就是标题

url='https://bj.58.com/ershoufang/'
#cookie='lastCity=100010000; __zp_stoken__=ce26bZyQcLhoDK1A7M0RzPzMQEDJzHHpAQCJkUHtpSSFDSCkNeko0HBZxSywqeBxlHh8PIE4CLwgTSWsacwcdbEMNUBBzE2APASkfAktgOFskSn9HCTgkLmE7GFxecS8MGE4FGX99IHdsQHV5YQ%3D%3D; __c=1610949395; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F&g=&s=3&friend_source=0&s=3&friend_source=0; __a=13532184.1600828409.1610683874.1610949395.205.23.3.205; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1610082805,1610683875,1610949395,1610949407; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1610949407'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
}

page_text=requests.get(url,headers).text
tree=etree.HTML(page_text)#拿到的网页，而不是局部的数据
title=tree.xpath('//h3[@class="property-content-title-name"]/text()')
price=tree.xpath('//span[@class="property-price-total-num"]/text()')

for i,j in zip(title,price):
    print(i,j)