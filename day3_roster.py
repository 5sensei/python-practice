roster = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 58},
    {"name": "王五", "score": 92}
]
# 功能一【添加新生】：
#
# 用 input() 让用户输入一个新同学的名字（存进变量 new_name）。
#
# 用 int(input()) 让用户输入新同学的成绩（存进变量 new_score，注意一定要套上 int() 把字符串转成整数！）。
#
# 把 new_name 和 new_score 组装成一个新的字典 new_student = {"name": ..., "score": ...}。
#
# 用列表的 .append() 方法，把 new_student 加进 roster 列表里，并打印出最新的 roster 看看加进去没有。
new_name = input("请输入一个新名字：")
new_score = int(input("请输入ta的成绩："))
new_student = {
    "name": new_name,
    "score": new_score
}
roster.append(new_student)
print(roster)

# 功能二【按名字查成绩】：
#
# 用 input() 让用户输入要查询的同学名字（存进变量 search_name）。
#
# 用 for s in roster: 遍历列表里的每一个字典 s。
#
# 在循环里用 if 判断：如果当前字典的名字 s["name"] 等于（==）用户输入的 search_name，就用 f-string 打印出：找到了！XX的成绩是：XX分。

search_name = input("请输入要查询的人姓名：")
for s in roster:
    if s["name"] == search_name:
        print( f"找到了！{search_name}的成绩是：{s['score']}")

# 功能三【统计全班平均分】（挑战加分项）：
#
# 在循环外先定义一个总分变量 total = 0。
#
# 用 for s in roster: 遍历列表，每次把 s["score"] 累加到 total 上（total = total + s["score"]）。
#
# 循环结束后，用 total / len(roster) 算出平均分并打印出来。
total = 0
for q in roster:
    total += q["score"]
avg = total / len(roster)
print(f"全班平均分是：{avg}")

#期末考试结束了，教务处需要一份**“补考名单”。请你从 roster 里找出所有成绩低于 60 分的同学，
# 把他们的名字**单独装进一个新的列表 fail_names 里，最后打印出这个列表（比如：需要补考的同学有：['李四']）。
fail_names = []
for m in roster:
        if m["score"] < 60:
            fail_names.append(m["name"])
print(f"不及格的人员名单：{fail_names}")