# 爬虫书籍售后、内容纠错、代码更新、爬虫项目分析
Python从入门到实战配套程序代码，书籍更正，代码更正，项目补充。


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

