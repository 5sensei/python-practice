# 今天学的是关于调用api的部分，首先就是把想要调用的api放到url后面，通过requests,get进行网络请求，在这之前最好用try     except防止崩溃，
# 确保status_code也就是状态码正常再用.json进行字符串转字典，最后通过对应的键进行精准查询






import requests

# 1. 专门查询厦门天气的公开 API（format=j1 代表要求返回标准的 JSON 格式数据）
url = "https://wttr.in/Xiamen?format=j1"

try:
    # 2. 发送请求（带上防崩和规避代理的保险）
    response = requests.get(url, timeout=5, proxies={"http": None, "https": None})

    if response.status_code == 200:
        # 3. 将返回的 JSON 文本转成 Python 字典
        weather_data = response.json()  # .json()作用是把返回的字符串信息转化成可查询的字典

        # 4. 从复杂的嵌套字典里层层剥离，精准抓取厦门当前温度和天气描述
        current_condition = weather_data["current_condition"][0]  # 后面两个方框代表查询字典，第一个方框是键
        temp_c = current_condition["temp_C"]  # 当前摄氏度
        weather_desc = current_condition["weatherDesc"][0]["value"]  # 天气描述

        print("🏙️ 【厦门今日天气播报】")
        print(f"当前温度：{temp_c} ℃")
        print(f"天气情况：{weather_desc}")

    else:
        print(f"天气接口请求异常，状态码：{response.status_code}")

except Exception as e:
    print(f"发生错误：{e}")

import requests

# 这是一个专门返回客户端公网 IP 的免费公开 API
url = "https://api.ipify.org?format=json"

try:
    # 照例加上防崩、超时和绕过代理的保险
    response = requests.get(url, timeout=5, proxies={"http": None, "https": None})

    if response.status_code == 200:
        # 1. 核心一步：把文本转成字典
        data = response.json()

        # 2. 从字典里直接取到 IP
        my_ip = data.get("ip")

        print(f"🌐 【公网 IP 查询成功】你的 IP 地址是：{my_ip}")
    else:
        print(f"请求异常，状态码：{response.status_code}")

except Exception as e:
    print(f"发生错误：{e}")