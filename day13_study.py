# 今天学pandas的一些常用操作，比如求平均值，最大值最小值，分组，排序，以及统计数量等


import pandas as pd

# ==========================================
# 准备工作：生成一份包含多个城市的成绩单 CSV
# ==========================================
raw_data = """name,age,score,city
张三,20,85,厦门
李四,21,95,泉州
王五,19,75,厦门
赵六,18,92,福州
孙七,20,88,泉州
周八,22,60,厦门
"""
with open("students_day13.csv", "w", encoding="utf-8") as f:
    f.write(raw_data)

df = pd.read_csv("students_day13.csv")
print("--- 1. 原始表格 ---")
print(df)


# ==========================================
# 核心操作 1：按列排序 (sort_values，对应 SQL 的 ORDER BY)
# ==========================================
# by="score" 代表按成绩排；ascending=False 代表降序（从高到低，对应 DESC）
df_sorted = df.sort_values(by="score", ascending=False)
print("\n--- 2. 按成绩从高到低排序 ---")
print(df_sorted)


# ==========================================
# 核心操作 2：分组统计平均分 (groupby，对应 SQL 的 GROUP BY)
# ==========================================
# 拆解公式：按 "city" 分组 -> 拎出 "score" 这一列 -> 算平均数 .mean()
city_avg_score = df.groupby("city")["score"].mean()
print("\n--- 3. 统计每个城市的平均成绩 ---")
print(city_avg_score)


# ==========================================
# 核心操作 3：分组统计人数 (count，对应 SQL 的 COUNT)
# ==========================================
city_count = df.groupby("city")["name"].count()
print("\n--- 4. 统计每个城市有多少名学生 ---")
print(city_count)