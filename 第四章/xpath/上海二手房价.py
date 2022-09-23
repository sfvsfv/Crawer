# coding=gbk
"""
作者：川川
@时间  : 2022/3/14 19:59
"""

from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
url = 'https://xa.58.com/ershoufang/?q=%E4%B8%8A%E6%B5%B7'
# 请求获取源码
page_text = requests.get(url=url, headers=headers).text
# 标准化
tree = etree.HTML(page_text)

if __name__ == '__main__':
    div_list = tree.xpath('//section[@class="list"]/div')
    print(div_list)
    fp = open('./上海二手房.txt', 'w', encoding='utf-8')
    for div in div_list:
        title = div.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        print(title)
        price = str(
            '总价格为' + div.xpath('.//div[@class="property-price"]/p/span[@class="property-price-total-num"]/text()')[
                0]) + '万元'
        print(price)
        fp.write(title + '\t' + price + '\n' + '\n')

