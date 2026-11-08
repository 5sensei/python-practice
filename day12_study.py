# 今天学习pandas，先试着看懂这串代码
import pandas as pd

# ==========================================
# 准备工作：先用代码自动生成一个带“空值”的测试表格 CSV
# ==========================================
raw_data = """name,age,score,city
张三,20,85,厦门
李四,21,,泉州
王五,,55,
赵六,18,92,海南
孙七,18,48,
"""
with open("students_day12.csv", "w", encoding="utf-8") as f:  # 参数为w写入，当前面的容器不存在时候会直接新建一个，如果本来就有则会先清空再写入
    f.write(raw_data)


# ==========================================
# 核心操作 1：读取 CSV 表格 (pd.read_csv)
# ==========================================
df = pd.read_csv("students_day12.csv")  #用pd.read_csv直接读取文件赋值给df
print("--- 1. 原始表格数据（注意里面的 NaN 代表空值/缺失值）---")
print(df)


# ==========================================
# 核心操作 2：处理缺失值 - 直接删掉有空值的行 (dropna)
# ==========================================
df_dropped = df.dropna()  # 起个变量名让他作为df经过dropna处理后的数据
print("\n--- 2. 使用 dropna() 删掉含空值的行 ---")
print(df_dropped)


# ==========================================
# 核心操作 3：处理缺失值 - 把空值填补成指定数字 (fillna)
# ==========================================
# 真实开发中，缺考的同学成绩不能随便删掉，通常把空成绩填补为 0 分
df_filled = df.copy()  # 这边要copy复制一份是因为下面的操作会影响第二步里面的表格，正常不需要
df_filled["score"] = df_filled["score"].fillna(0).astype(int)  # 用法统一都是变量.xx输入对应指令
df_filled["city"] = df_filled["city"].fillna("厦门")
df_filled["age"] = df_filled["age"].fillna(18).astype(int) # 空年龄默认填18岁
print("\n--- 3. 使用 fillna() 把空缺的成绩补为 0，空年龄补为 18 ---")
print(df_filled)


# ==========================================
# 核心操作 4：条件筛选（完全对应 SQL 的 WHERE）
# ==========================================
# 语法规律：外层 df[...] 代表筛选表格，内层 df['score'] > 60 是判断条件
passed_students = df_filled[df_filled["score"] > 90]   # 之所以要两层方框是因为内部先判断是否大于90，会产生true或者false两种结果，这个时候直接打印不会有具体名单只有那两种结果，需要外部再二次判断如果是才赋值给变量
adult_students = df_filled[df_filled["age"] == 18]
# 在 Pandas 里只要你想按条件筛选并打印出具体的表格内容（包括人名、年龄等完整信息），就必须写这两个方框。内层做判断，外层去拿人
print("\n--- 4. 筛选出成绩大于 90 分的及格同学 ---")
print(passed_students)
print(adult_students)