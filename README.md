# 爬虫书籍售后、内容纠错、代码更新、爬虫项目分析
Python从入门到实战配套程序代码，书籍更正，代码更正，项目补充。



京东购买地址如下：
https://item.jd.com/14049708.html
购买后请下方加我微信，邀请你到读者售后群，方便交流。

<!-- 
参考更新仓库：
https://github.com/wistbean/learn_python3_spider
https://github.com/xingag/spider_python
--> 

## 本书代码售后答疑
希望本书的内容能够教会你学习爬虫的方法，而不是复制粘贴代码。书籍中难免有表述错误的地方，如果有疑问，你可以与我联系。
<br><br>
如果本仓库的代码过时等问题，你可以在此提Issues，也可以与联系出版社反馈，我将尽快的回答你，并且更新修复后的代码在本仓库。
<br><br>
读者可以直接邮箱对我提问，详细说明你遇到的问题，请反复检查确保是代码真实存在的问题再问，提问基本格式：详细问题描述+详细的截图

我的邮箱：2835809579@qq.com ，我的微信：hxgsrubxjogxeeag
## 书中内容纠错
由于排版等原因，可能书中小部分内容写错了，在此更正，非常抱歉。


## 爬虫项目
### 艺术二维码制作
99一个二维码，还售罄？？
<br>
![image](https://github.com/sfvsfv/Crawer/assets/62045791/8d9a74ec-4675-4320-b90a-4a8c651e4a56)
<br>
不存在，只需要不到一毛钱成本就可以制作完成。到知数云https://data.zhishuyun.com/services ，申请艺术二维码API，可免费体验20次：

![image](https://github.com/sfvsfv/Crawer/assets/62045791/a1393d79-346d-4f5a-a51a-41b45ef97dad)

参考代码如下，你只需要修改token为你自己的token即可：
```csharp
# coding=gbk
'''
作者：川川
书籍： Python网络爬虫入门到实战
京东地址：https://item.jd.com/14049708.html
'''

import requests

url = "https://api.zhishuyun.com/qrart/generate?token=你自己的token"

headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

payload = {
    "type": "link",
    "content": "https://chat.zhangsan.cloud/",
    "prompt": "mexican tacos",
    "pattern": "rd1",
    "preset": "vibrant-palette",
    "qrw": 2,
    "rawurl": True,
    "padding_level": "5",
    "aspect_ratio": "768x768",
    "position": "center",
    "pixel_style": "square",
    "marker_shape": "square",
    "sub_marker": "square",
    "rotate": "0",
    "ecl": "M",
    "padding_noise": "0.25"
}

response = requests.post(url, json=payload, headers=headers)
# 解析JSON响应
response_data = response.json()
image_url = response_data.get("image_url")
print(image_url)
if image_url:
    # 获取图像数据
    image_response = requests.get(image_url)
    image_data = image_response.content

    # 将图像数据保存为本地文件
    image_filename = "AI.jpg"  # 本地文件名
    with open(image_filename, "wb") as image_file:
        image_file.write(image_data)

    print(f"图像已保存为 {image_filename}")
else:
    print("未找到图像URL")
```

### 中国大学生排名

```csharp
# coding=gbk
'''
作者：川川
书籍： Python网络爬虫入门到实战
京东地址：https://item.jd.com/14049708.html
'''

import pandas as pd
import csv
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service  # 新增
from selenium.webdriver.common.by import By

# start_time = time.time()  # 计算程序运行时间


# 获取网页内容
def get_one_page(year):
    try:
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }

        #  https://www.shanghairanking.cn/rankings/bcur/%s11
        url = 'https://www.shanghairanking.cn/rankings/bcur/%s11' % (str(year))
        # print(url)

        response = requests.get(url, headers=headers)
        if response.content is not None:
            content = response.content.decode('utf-8')
            # print(content.encode('gbk', errors='ignore').decode('gbk'))
            return content.encode('gbk', errors='ignore').decode('gbk')
        else:
            content = ""
            return content.encode('gbk', errors='ignore').decode('gbk')
            # print(content.encode('gbk', errors='ignore').decode('gbk'))

    except RequestException:
        print('爬取失败')


def extract_university_info(data):
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find('table', {'data-v-4645600d': "", 'class': 'rk-table'})
    tbody = table.find('tbody', {'data-v-4645600d': ""})
    rows = tbody.find_all('tr')

    university_info = []
    for row in rows:
        rank = row.find('div', {'class': 'ranking'}).text.strip()
        univ_name_cn = row.find('a', {'class': 'name-cn'}).text.strip()
        univ_name_en = row.find('a', {'class': 'name-en'}).text.strip()
        location = row.find_all('td')[2].text.strip()
        category = row.find_all('td')[3].text.strip()
        score = row.find_all('td')[4].text.strip()
        rating = row.find_all('td')[5].text.strip()

        info = {
            "排名": rank,
            "名称": univ_name_cn,
            "Name (EN)": univ_name_en,
            "位置": location,
            "类型": category,
            "总分": score,
            "评分": rating
        }

        university_info.append(info)
        # 打印数据
        print(
            f"排名: {rank}, 名称: {univ_name_cn}, Name (EN): {univ_name_en}, 位置: {location}, 类型: {category}, 总分: {score}, 评分: {rating}"
        )

    return university_info


# data = get_one_page(2023)
# 获取一个页面内容
# print(extract_university_info(data))

def get_total_pages(pagination_html):
    soup = BeautifulSoup(pagination_html, 'html.parser')
    pages = soup.find_all('li', class_='ant-pagination-item')
    if pages:
        return int(pages[-1].text)
    return 1


html = get_one_page(2023)


def get_data_from_page(data):
    content = extract_university_info(data)
    return content



total_pages = get_total_pages(html)
# print(total_pages)




def write_to_csv(data_list, filename='output.csv'):
    # 检查文件是否存在，以决定是否写入表头
    file_exists = False
    try:
        with open(filename, 'r', encoding='utf-8'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["排名", "名称", "Name (EN)", "位置", "类型", "总分", "评分"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # 写入表头
        for data in data_list:
            writer.writerow(data)




from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.get("https://www.shanghairanking.cn/rankings/bcur/202311")

for page in range(1, total_pages + 1):
    jump_input_locator = browser.find_element(By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input')
    jump_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(jump_input_locator)
    )
    jump_input.clear()

    jump_input.send_keys(page)  # 输入页码
    jump_input.send_keys(Keys.RETURN)  # 模拟 Enter 键
    time.sleep(3)  # 等待页面加载

    html = browser.page_source
    content = get_data_from_page(html)
    write_to_csv(content)

time.sleep(3)
browser.quit()
```

## cookies登录CSDN
### 获取cookie

```csharp
# coding=gbk
'''
作者：川川
书籍： Python网络爬虫入门到实战
京东地址：https://item.jd.com/14049708.html
'''
from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service  # 新增
import time
service = Service(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)


browser.get("https://www.csdn.net/")

print('请在十秒内扫码登录')
time.sleep(10)

dictCookies = browser.get_cookies()
jsonCookies = json.dumps(dictCookies)

with open('cookies.txt', 'w') as f:
    f.write(jsonCookies)
print('cookies保存成功！')
```
### 登录

```csharp
# coding=gbk
'''
作者：川川
书籍： Python网络爬虫入门到实战
京东地址：https://item.jd.com/14049708.html
'''

import json
from selenium import webdriver
import time

browser = webdriver.Chrome()
with open('cookies.txt', 'r', encoding='u8') as f:
    cookies = json.load(f)
browser.get("https://www.csdn.net/")
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get("https://www.csdn.net/")
time.sleep(10)
```

