# 说了一些话
from jmespath.compat import string_type

print("王大帅收服小宝肉")
"""
 似乎有些触动
"""
print(999)
print(999.99)
handsome = 99
print(handsome)
handsome = handsome + 1
print("王大帅的英俊：", handsome, "%")
# 可恶电脑要没电了，最后打一点点，好像是什么定时
handsome = handsome + 1
print("王大帅的英俊每过一秒钟：", handsome, "%")
print("王大帅的英俊每过一秒钟：", handsome, "%")
print("王大帅的英俊每过一秒钟：", handsome, "%")
print("王大帅的英俊每过一秒钟：", handsome, "%")

# 神复习到数据类型了
print(type("王大帅"))
print(type(888))
print(type(888.88))

string_type = type("帅大王")
int_type = type(888)
float_type = type(888.88)
print(string_type, int_type, float_type)

name = ("王大帅")
name_type = type(name)
print(name_type)

# 神开始复习数据类型的转换
num_str = str(99)
print(type(num_str), num_str)

# 等号前面只是个单纯的变量名随便起，等号后面括号前面是最后转换成的变量类型，括号里面是原来的变量

float_str = str(666.66)
print(type(float_str), float_str)

num=int("11")
print(type(num), num)

num2=float("11")
print(type(num2), num2)

# 想把字符串转数字得确保引号里面都是数字才行，所以此处转换失败
num3=int("22")
print(type(num3), num3)

float_num=float(11)
print(type(float_num), float_num)

a= int(5.4188)
print(type(a), a)

# 这是deepseek教我的赛博算命
name= input ("请输入你的名字：")
age = input("请输入你的年龄：")
print(f"oioi, {name}, 本帅猜测你今年是{age}岁了")