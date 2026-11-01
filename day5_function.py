# 今天学def函数定义以及return返回值
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
