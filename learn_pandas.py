import pandas as pd

# 1.建立一个字典数据
data ={
    "姓名": ["神","猪","狗","鸡","小宝"],
    "班级": ["一班","二班","三班","四班","一班"],
    "python成绩": [100,1,2,3,99]

}

# 2.把这个字典变成一个数据表
df = pd.DataFrame(data)

# 3.把这个表格保存成一个真正的 cvs 文件
df.to_csv("scores.csv",index=False,encoding="utf-8-sig")

print("恭喜王大帅生成表格成功！")