# coding=gbk
"""
作者：川川
@时间  : 2022/3/27 23:55
"""
import ddddocr

ocr = ddddocr.DdddOcr()
with open('clean.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

print(res.upper())



