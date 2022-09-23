# coding=gbk
"""
作者：川川
@时间  : 2022/3/27 23:39
"""
import pytesseract
from PIL import Image
# 读取图片
im = Image.open('clean.png')
# 识别文字
string = pytesseract.image_to_string(im)
print(string)