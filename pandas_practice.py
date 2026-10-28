import pandas as pd

# 1.读取表格
df = pd.read_csv('scores.csv')

# 2.打印表格
print("神的表格")
print(df)

# 3.算平均数
# 在pandas里面只要拿到单独一列，比如df["python成绩"]，后面加上 .mean(),就是求平均值,加上 .max()，就是求最大值
pingjun = df["python成绩"] .mean()
zuidazhi = df["python成绩"] .max()

print("成绩统计")
print(f"平均成绩：{pingjun}")
print(f"最高分是：{zuidazhi}")