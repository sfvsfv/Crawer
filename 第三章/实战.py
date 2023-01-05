# coding=utf-8
import requests
import re
import logging

logging.captureWarnings(True)
import time

# 第一页
url = 'https://xiaohua.zol.com.cn/baoxiaonannv/'
# 第n页
url2 = 'https://xiaohua.zol.com.cn/baoxiaonannv/%d.html'

header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
}


def writefile(items):
    with open('duanzi.txt', 'a') as f:
        print('一共有%d条段子' % len(items))
        for item in items:
            f.write(item + '\n')
            f.write('————————————————————————————————————————\n')
        pass


# 正则表达式
pattern = re.compile(r'<div class="summary-text">(.*?)</div>')


def load(page):
    if page == 1:
        # 获取源码内容，verify=False不认证
        response = requests.get(url, headers=header, verify=False, timeout=10).text
        # 正则匹配
        item = pattern.findall(response)
        # 写入
        writefile(item)
    elif page > 1:
        for p in range(1, page + 1):
            if p == 1:
                duanzi = url
            else:
                duanzi = url2 % (p)
            print(duanzi)
            requests.packages.urllib3.disable_warnings()
            response = requests.get(duanzi, headers=header, verify=False, timeout=10).text
            # 正则匹配
            item = pattern.findall(response,re.S)
            # 写入
            writefile(item)
            time.sleep(2)
        pass


if __name__ == '__main__':
    n = int(input('请输入爬取的页数：'))
    load(n)
