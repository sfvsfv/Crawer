# coding=gbk
"""
作者：川川
@时间  : 2022/3/15 17:20
"""
import urllib.parse
import urllib.request
from lxml import etree
import time
import os


def qingqiu(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    if page == 1:
        url = url.format('')  # 填写空
    else:
        url = url.format('_' + str(page))  # 填写下划线加页码

    request = urllib.request.Request(url=url, headers=headers)
    return request


def download(image_src):
    dirpath = 'photo'
    # 创建一个文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    # 创建文件名
    filename = os.path.basename(image_src)
    # 图片路径
    filepath = os.path.join(dirpath, filename)
    # 发送请求，保存图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def jiexi(content):
    # 生成对象
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # 遍历列表，依次下载图片
    for image_src in image_list:
        image_src = 'http:' + image_src
        download(image_src)


if __name__ == "__main__":
    url = 'http://sc.chinaz.com/tupian/gudianmeinvtupian{}.html'

    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))

    for page in range(start_page, end_page + 1):
        print("第%s页开始下载······" % page)
        request = qingqiu(url, page)
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容
        jiexi(content)
        time.sleep(5)  # 避免被反爬，不能爬太快
        print("第%s页下载完毕······" % page)
    print("下载完成！")
