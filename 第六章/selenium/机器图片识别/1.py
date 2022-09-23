# coding=gbk
"""
作者：川川
@时间  : 2022/3/27 22:15
"""
import pytesseract as ts
from PIL import Image

im = Image.open('img_2.png')

text = ts.image_to_string(im,lang='chi_sim')
print(text)