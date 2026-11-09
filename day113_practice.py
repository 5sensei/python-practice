import pandas as pd
# 现在独立把缺失的功能代码补上


# ==========================================
# 准备工作：生成一份班级考勤与平时分表格
# ==========================================
raw_data = """name,major,late_count,score
张三,人工智能,1,88
李四,软件工程,4,72
王五,人工智能,0,95
赵六,数据科学,2,81
孙七,软件工程,5,60
周八,人工智能,1,90
"""
with open("attendance_day13.csv", "w", encoding="utf-8") as f:
    f.write(raw_data)

df = pd.read_csv("attendance_day13.csv")  #调用pandas库读取这份文件
print("--- 0. 原始考勤表 ---")
print(df)


# ==========================================
# 填空 1：不分组，直接算出全班所有人的平均平时分 (score)
# ==========================================
total_avg = df["score"].mean()  #.mean为计算平均值，如果要分组前面就改成df.groupby(）
print("\n--- 1. 全班总平均分 ---")
print(f"{total_avg}分")


# ==========================================
# 填空 2：按迟到次数 (late_count) 从多到少进行降序排列，揪出迟到王
# ==========================================
df_late_sorted = df.sort_values(by="late_count", ascending=False)
print("\n--- 2. 按迟到次数从多到少排序 ---")
print(df_late_sorted)


# ==========================================
# 填空 3：按专业 (major) 分组，计算每个专业的平均平时分 (score)
# ==========================================
major_avg_score = df.groupby("major")["score"].mean()
print("\n--- 3. 各专业的平均平时分 ---")
print(f"{major_avg_score}分")


# ==========================================
# 填空 4：按专业 (major) 分组，找出每个专业里最高的迟到次数 (late_count)
# ==========================================
major_max_late = df.groupby("major")["late_count"].max()
print("\n--- 4. 各专业最高的迟到次数 ---")
print(major_max_late)


# ==========================================
# 填空 5：按专业 (major) 分组，数一数每个专业各有几名学生 (name)
# ==========================================
major_student_count = df.groupby("major")["name"].count()
print("\n--- 5. 各专业的学生人数 ---")
print(major_student_count)