# 今天是对第三天学的提升，代码的精简及常用方法
# ai告诉我工作中是不会用第三天练习那样子写代码的，基本都是浓缩成一行写完

roster = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 58},
    {"name": "王五", "score": 92}
]

# 请只用 1 行列表推导式，分别完成下面两个需求（不准写传统的 4 行 for 循环）：
# 需求 1（带条件）： 提取出所有及格同学（score >= 60）的名字，存入 pass_names
pass_name = [m["name"] for m in roster if m["score"] >= 60]
print(pass_name)

# 需求 2（不带条件）： 把全班所有人的成绩（score）都加 5 分，
# 生成一个新的成绩列表 new_scores（结果应该是 [90, 63, 97]）并打印。

new_scores = [n["score"] + 5 for n in roster  ]
print(new_scores)