# coding=gbk
"""
作者：川川
@时间  : 2022/3/27 23:19
"""
import pytesseract
from PIL import Image
# 读取图片
im = Image.open('img_1.png')
# 识别文字，并指定语言
string = pytesseract.image_to_string(im, lang='chi_sim')
print(string)