# 今天学的是class类，把变量以及功能一一绑定

# ==================== 第一部分：定义 Student（学生）类 ====================

# 1. 定义一个名为 Student 的类
class Student:

    # 2. 定义初始化方法 __init__，接收参数：self, name, score
    #    在方法内部，将 name 和 score 分别绑定到 self.name 和 self.score 上
    def __init__(self,name,score):
        self.name = name
        self.score = score

        # 3. 定义 show_info 方法（只需接收 self 参数）
        #    用 return 返回一段字符串，包含该学生的姓名和成绩
    def show_info(self):
        return f"学生姓名：{self.name},学生成绩：{self.score}"

        # 4. 定义 check_pass 方法（只需接收 self 参数）
        #    判断 self.score 是否大于等于 60，是则 return "及格"，否则 return "挂科"
    def check_pass(self):
        if self.score >= 60:
            return "及格"
        else:
            return "挂科"


# ==================== 第二部分：定义 Manager（管理员）类 ====================

# 5. 定义一个名为 Manager 的类
class Manager:


    # 6. 定义初始化方法 __init__（只需接收 self 参数）
    #    在内部创建一个空列表属性 self.roster = []，用来存放学生对象
    def __init__(self):
        self.roster = []

    # 7. 定义 add_student 方法，接收参数：self, stu_obj（传进来的学生对象）
    #    把 stu_obj 添加（append）到 self.roster 列表中，并打印一句录入成功的提示
    def add_student(self,stu_obj):
        self.roster.append(stu_obj)
        print(f"录入成功！{stu_obj.name}")

    # 8. 定义 show_all 方法（只需接收 self 参数）
    #    用 for 循环遍历 self.roster 列表中的每一个学生对象：
    #    在循环里，分别调用该学生对象的 show_info() 和 check_pass() 方法并打印出来
    def show_all(self):
        for m in self.roster:
            print(m.show_info(),m.check_pass())


# ==================== 第三部分：外部实战调用 ====================

# 9. 根据 Student 图纸，造出 3 个具体的学生对象：
#    s1（张三，85分）、s2（李四，92分）、s3（王五，55分）
s1 = Student("帅哥",99)
s2 = Student("小宝",55)
s3 = Student("肉肉",91)
# 10. 根据 Manager 图纸，造出 1 个管理员对象 boss
boss = Manager()

# 11. 调用 boss 的 add_student 方法，把 s1、s2、s3 依次添加进去
boss.add_student(s1)
boss.add_student(s2)
boss.add_student(s3)

# 12. 调用 boss 的 show_all 方法，查看全班成绩单和及格情况
boss.show_all()

