import pandas as pd
import pymysql

df = pd.read_csv("attendance_day13.csv")
print(df.info())

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="god_db",
    charset="utf8mb4",
)
cursor = conn.cursor()

create_sql = """
CREATE TABLE IF NOT EXISTS  attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    major VARCHAR(50),
    late_count INT,
    score INT
);
"""
cursor.execute(create_sql)


insert_sql = "INSERT INTO attendance (name,major,late_count,score) VALUES (%s,%s,%s,%s)"
for index, row in df.iterrows(): # index是行号，row是整行内容，最后面那个是按行迭代的意思
    cursor.execute(
        insert_sql,
        (row["name"], row["major"], int(row["late_count"]), int(row["score"])),
    ) # 把本来的数据传到msql上
conn.commit()
cursor.execute("SELECT COUNT(*) FROM attendance;")
count = cursor.fetchone()[0]
print(f"成功入库总行数：{count} 行！")
cursor.close()
conn.close()