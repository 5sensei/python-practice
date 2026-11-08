# 我的 28 天工程地基自救打卡存档

- **当前进度**：已完成 Day 9（Python面向对象 Class/__init__/self，SQL GROUP BY分组）
- **核心代码记忆**：
  - Student 类：封装 name, score 及 show_info(), check_pass() 方法。
  - Manager 类：内部维护 self.roster 列表，实现 add_student() 和 show_all()。
- **下一步即将攻克**：Day 10（终端 pip、requests 库网络请求、SQL HAVING 过滤）

- **当前进度**：已完成 Day 10（终端 pip 环境管理、requests 库网络请求、try...except 异常防崩、面向对象 Spider 类封装，SQL HAVING 分组过滤）
- **核心代码记忆**：
  - requests.get(url, timeout=3) 发送网络请求并设置超时防死机。
  - status_code == 200 校验连通性，response.text 获取网页文本。
  - WHERE 用于分组前筛选普通行，HAVING 用于分组后配合聚合函数（如 AVG、COUNT）筛选统计结果。
- **下一步即将攻克**：Day 11（API 初体验、JSON 解析、厦门天气接口实战、牛客 SQL 进阶）

- **当前进度**：已完成 Day 11（公开 API 调用、response.json() 转换字典、嵌套字典/列表取值，牛客 SQL 刷至第 27 题[cite: 5]）
- **核心代码记忆**：
  - 标准三板斧：requests.get() 发请求 -> response.json() 转字典 -> .get() 防御性取值。
  - proxies={"http": None, "https": None} 规避本地代理对国内/直连 API 的 SSL 干扰[cite: 3, 4]。
  - 链式取值 data.get("a", {}).get("b") 防止因键缺失导致 KeyError 崩溃[cite: 3]。
- **下一步即将攻克**：Day 12（Pandas 读取 CSV、缺失值处理 dropna/fillna、条件筛选，以及 SQL 内连接 INNER JOIN）

- **当前进度**：已完成 Day 12（Pandas 读取 CSV、缺失值清洗 dropna/fillna、双层方框条件筛选，牛客 SQL 刷至第 28 题）
- **核心代码记忆**：
  - 读取表格：`df = pd.read_csv("xxx.csv")`（调用 pd 造出表格对象 df）。
  - 缺失值清洗：`df.dropna()` 直接删掉含空值（NaN）的行；`df["列名"] = df["列名"].fillna(目标值)` 填补空值（数字、字符串均可）。
  - 类型修正：出现 `NaN` 会导致整列自动变成浮点数（带 `.0`），填补后可用 `.astype(int)` 强转回整数。
  - 条件筛选：`df[df["score"] > 90]`（内层方框负责判断对错生成 True/False 名单，外层方框拿着名单去原表格抓人，对应 SQL 的 WHERE）。
- **下一步即将攻克**：Day 13（Pandas 的 groupby 分组统计与排序，以及牛客 SQL 第 29~31 题）