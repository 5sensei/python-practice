# 定义字典  空字典大括号里面空着
my_dict={"神":99,"小宝":100}
# 如果有重复的key，则后面的value会覆盖前面的
my_dict2={"神":99,"神":100,"小宝":100}
print(my_dict)
print(my_dict2)

# 字典跟集合一样不能用下标索引，可以用对应的key值来取对应的value
print(my_dict2["神"])

# 字典的key跟value可以是任意数据类型，但是key本身不能是字典
# 嵌套字典 例如记录学生各科的考试信息
chengji = {
    "神":{"语文":149,
        "数学":150,
        "英语":149
          },
    "小宝":{"语文":90,
            "数学":130,
            "英语":105}
       }



print(chengji)

# 从嵌套字典获取数据
a = chengji ["神"]["语文"]
print(a)

# 字典的常用操作
# 1.新增元素，只要给字典一个新的元素跟对象就行,若要更新，下方的key选择要更新的对象，更改value即可
my_dict["猪"] = 0
my_dict["小宝"] = 100
print(my_dict)

# 2.删除元素， 格式：字典.pop（key）
my_dict.pop("猪")
print(my_dict)

# 3.清空字典   格式：字典.clear()
chengji.clear()
print(chengji)

# 4.获取全部的key   格式：字典.keys()
b = my_dict.keys()
print(b)

# 5.遍历字典  用for循环遍历，通过获取全部的key完成遍历
for c in b:
    print(f"字典的key是：{c}")
    print(f"字典的value是：{my_dict[c]}")  # 这里用对应的key取出对应的value

# 方法2 直接对字典进行for循环，每次循环都是直接得到key(更简单)
for d in my_dict:
    print(f"2字典的key是：{d}")
    print(f"2字典的value是：{my_dict[d]}")  # 这里用对应的key取出对应的value

# 因为字典不支持下表索引，所以不能用while循环

# 统计字典的元素数量 用len（）函数
shuliang = len(my_dict)
print(f"字典中的元素数量有：{shuliang}个")

