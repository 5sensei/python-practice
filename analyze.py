import pandas as pd

# 1.读取刚刚生成的 csv 文件
df = pd.read_csv("scores.csv")

print("---这是表格的前5行---")
print(df.head())

print("\n---这是所有的python成绩---")
print(df["python成绩"])