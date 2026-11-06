# 写一个网页爬虫类 Spider
#
# 定义一个类叫 Spider。
#
# 在初始化方法 __init__ 里，接收一个参数 url（网址），并把它存成对象自己的属性 self.url。
#
# 在类里面写一个方法叫 fetch(self)：
#
# 用 try...except 包住里面的请求逻辑。
#
# 使用 requests 去请求 self.url，并设置 3 秒超时限制。
#
# 判断返回的状态码：如果等于 200，就打印出网页文本的前 100 个字符；否则打印 "状态码异常"。
#
# 如果进入 except，就打印 "网络报错"。
#
# 在类的最外面，根据 Spider 图纸造出一个对象 s，
# 传入网址 "[https://www.baidu.com](https://www.baidu.com)"，然后调用它的 fetch() 方法跑起来。
from asyncio import timeout

from twisted.web.http import responses

import requests

class Spider:
    def __init__(self,url):
        self.url = url

    def fetch(self):
        try:
            responses = requests.get(self.url,timeout = 3)
            if responses.status_code == 200:
                print(f"网页文本前100字符为：{responses.text[:100]}")
            else:
                print(f"状态码异常：{responses.status_code}")
        except Exception as e:
            print(f"网络错误：{e}")


s = Spider("https://www.baidu.com")
s.fetch()