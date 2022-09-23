# coding=gbk
"""
作者：川川
@时间  : 2022/3/28 3:38
"""

import requests
from PIL import Image
# 忽略警告
import logging

logging.captureWarnings(True)

# 识别网络生成验证码
url = 'https://so.gushiwen.org/RandCode.ashx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

# 把原始图片保存
response = requests.get(url=url, headers=headers, verify=False)
with open('./test.png', 'wb') as fp:
    fp.write(response.content)  # content是二进制内容


# 编写函数对彩色图片进行灰度化处理
def covertimage(path):
    img = Image.open(path)
    # 灰度化
    img = img.convert('L')

    # 图片都是由数据组成，加载
    data = img.load()
    # 图片宽和高
    w, h = img.size

    # 对于黑白图片，像素值是0 纯黑
    # 像素值255 纯白
    for i in range(w):
        for j in range(h):
            # 取出来图片中所有的像素值
            if data[i, j] > 135:
                data[i, j] = 255
            else:
                data[i, j] = 0
    img.save('clean.png')


covertimage('test.png')  # 执行函数

