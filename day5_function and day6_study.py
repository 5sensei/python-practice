import json
roster = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 58},
    {"name": "王五", "score": 92}
]
# 请你自己定义并调用以下 3 个独立的函数
# 函数一：添加学生 def add_student(student_list, name, score):
# 功能： 把传进来的 name 和 score 组装成字典，.append() 追加进 student_list 里（不需要写 input，直接用括号里传进来的参数即可）。
# 测试： 在函数外面写一行 add_student(roster, "赵六", 77)，然后打印 roster 看看赵六加进去没。
def add_student(student_list, name, score):
    student_list.append({"name": name, "score": score})
    return student_list # 这边是用append直接更改了外面的roster列表，所以这里的return其实可以去掉，因为不需要拿出来什么东西
add_student(roster,"赵六",77)
print(roster)

# 函数二：按名字查成绩
# 函数头： def find_score(student_list, target_name):
# 业务逻辑： 遍历 student_list，如果找到某个人的 "name" 等于 target_name，就用 return
# 把他的 "score" 交出去；如果整个循环跑完都没找到，在循环外面 return "查无此人"。
# 调用测试： 在函数外面分别打印 find_score(roster, "李四") 和 find_score(roster, "孙七")，看看能不能打出 58 和 查无此人。
def find_score(student_list, target_name):
    for m in student_list:
        if m["name"] == target_name:
            return m["score"]
    return"查无此人"  #跟for对齐表示跳出循环
print(find_score(roster, "李四"),find_score(roster, "孙七"))

# 函数三：获取补考名单
# 第一行定义函数：def get_fail_names(student_list):
# 第二行缩进：直接写 return 加上昨天学的列表推导式，把 student_list 里所有 score < 60 的同学的 "name" 提取出来交出去
# （注意这次遍历的是传进来的参数 student_list，不要手滑写成外面的 roster）。
# 第三行顶格调用：print(get_fail_names(roster))
def get_fail_names(student_list):
    student_list = [m["name"] for m in student_list if m["score"] < 60]
    return student_list # 这里的话我是在内部定义了这个函数，我需要用return把这个东西先拿出来，我才能输出
print(get_fail_names(roster))


# day6study,写完了一天的数据，先用save保存到硬盘，第二天要用再用load读取出来

# 任务1：定义存档函数 def save_data(student_list, filename):
# 在函数内部使用 with open(filename, "w", encoding="utf-8") as f:
# 配合 json.dump() 把传进来的 student_list 保存到文件中（别忘了加 ensure_ascii=False 和 indent=4）
def save_data(student_list, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(student_list, f, ensure_ascii=False ,indent=4)


# 任务2：定义读档函数 def load_data(filename):
# 在函数内部使用 with open(filename, "r", encoding="utf-8") as f:
# 配合 return 和 json.load(f)，把读取出来的数据直接交回函数外面！
def load_data(filename):
    with open(filename,"r", encoding="utf-8") as f:
        loaded_list = json.load(f)
    return loaded_list

# 任务3：调用测试
# 1. 调用 save_data(roster, "data.json") 把花名册存进硬盘
# 2. 调用 new_roster = load_data("data.json") 把数据读出来，并 print(new_roster)
save_data(roster, "data.json") # 把data.json当作容器，把roster放进去
new_roster = load_data("data.json")
print(new_roster)