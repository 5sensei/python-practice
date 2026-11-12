import sqlite3

# 1. 连接到本地数据库（如果没有 school.db，Python 会自动帮你创建一个）
conn = sqlite3.connect("school.db")

# 2. 获取游标（相当于拿到了操作数据库的笔）
cursor = conn.cursor()

# 3. 创建一张名为 student 的表格
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    score REAL
)
""")

# 4. 尝试往表里插入一条真实的学生数据
cursor.execute("INSERT INTO student (name, age, score) VALUES ('张三', 20, 88.5)")

# 5. 提交保存（Commit）并关闭连接
conn.commit()
# 6. 查询数据库里的所有学生数据
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()  # 获取所有查询结果

print("从数据库里查到的所有学生：")
for row in rows:
    print(row)
conn.close()

print("数据库创建成功，并且成功插入了一条测试数据！")