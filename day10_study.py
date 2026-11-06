from http.client import responses

import requests

# 1. 目标网址（这里先用百度首页练手）
url = "https://www.baidu.com"

# 2. 发送 GET 请求，把服务器返回的包裹存进 response 变量里
response = requests.get(url)

# 3. 强行指定用 utf-8 编码解析，防止中文变成乱码
response.encoding = "utf-8"

# 4. 查看状态码（200 代表请求成功，404 代表找不到网页）
print(f"请求状态码：{response.status_code}")

# 5. 打印网页的前 300 个字符看看里面有什么
print("网页内容预览：")
print(response.text[:300])


# requests.get(网址)：相当于你在浏览器地址栏输入网址并按回车。
# response.status_code：检查有没连上，200 就是绿灯通行。
# response.text：网页的纯文本源码（字符串格式，所以能直接用 Day 1 学的 [:300] 切片！）。


# 在上面的基础上加上前面学的try     except放崩溃机制
import requests
url = "https://www.baidu.com"
try:
    response2 = requests.get(url,timeout=5)  # 5秒钟未响应直接报错防止崩溃

    if response2.status_code == 200:
        response2.encoding = "utf-8"
        print(f"抓取成功！前300个字符：{response2.text[:300]}")
    else:
        print(f"网页返回状态异常码：{response2.status_code}")
except Exception as e:
    print(f"请求错误，返回异常码：{e}")
