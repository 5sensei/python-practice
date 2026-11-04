import json

from streamlit import exception


# 今天学的是try跟except，就是防止报错程序直接崩溃，拿第七天的代码进行改造
# ==================== 第一部分：定义 4 个核心工具函数 ====================

# 1. 定义存档函数 save_data(student_list, filename)
# 要求：使用 with open ("w"模式, utf-8编码) 配合 json.dump 把列表存进文件
def save_data(student_list, filename):
    with open(filename,"w" ,encoding= "utf-8" ) as f:
        json.dump(student_list , f, ensure_ascii=False, indent=4)


# 2. 定义读档函数 load_data(filename)
# 要求：使用 with open ("r"模式, utf-8编码) 配合 json.load 读取文件，并用 return 返回结果
def load_data(filename):
    with open (filename,"r" ,encoding="utf-8") as f:
        return json.load(f)

# 3. 定义添加学生函数 add_student(student_list, name, score)
# 要求：把 {"name": name, "score": score} 字典追加(append)到 student_list 中
def add_student(student_list,name,score):
    student_list.append({"name":name,"score":score})


# 4. 定义按名字查成绩函数 get_score(student_list, target_name)
# 要求：用 for 循环遍历列表，如果找到名字等于 target_name 的字典，return 他的 score；
# 如果整个循环跑完都没找到，在循环外面兜底 return "查无此人"
def get_score(student_list, target_name):
    for student in student_list:
        if student["name"] == target_name:
            return student["score"]
    return"查无此人"
# ==================== 第二部分：主程序运行与闭环测试 ====================

# 步骤 A [开机初始化]：
# 先准备一个初始列表 roster（包含张三 85 分、李四 92 分），或者直接调用 load_data("data.json") 读取已有存档
# 改造：如果硬盘里面本来没有data2这个文件就会报错，所以需要用try跟except
try:
    roster = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92}
    ]
    print("读档成功！")
except FileNotFoundError:
    print("未找到历史文档，已为您新建空白花名册！")

    roster = []



# 步骤 B [控制台交互 / 功能调用]：
# 1. 调用 add_student 往 roster 里添加一个新学生（比如用 input() 让用户输入名字和成绩，或者直接写死添加 "王五", 95）
# 2. 调用 save_data 把更新后的 roster 保存到 "data.json"
# 3. 调用 load_data 重新从 "data.json" 读取数据赋值给 latest_roster
# 4. 调用 get_score 在 latest_roster 里查询刚才添加的学生成绩，并 print 打印出来！
a = input("神命令你输入一个名字：")
# 改造：如果输入的不是数字那么系统也会直接报错，来不及保存，需要修改
try:
    b = int(input("神命令你输入这人的成绩："))
except ValueError as e:  # Exception虽然是万能捕手，但是如果你本身代码拼写错误他会直接无视，所以应分类，记住这四种：
                   # FileNotFoundError：找不到文件错误
                   # ValueError，值转换错误
                   # KeyError,字典找不到键错误
    print(f"你在逗我？叫你输入数字！系统错误原因：{e}")
    b = 0

add_student(roster,a,b)
save_data(roster,"data2.json")
latest_roster = load_data("data2.json")
result = get_score(latest_roster,a)
print(f"{a}的成绩是{result}")
print(roster)