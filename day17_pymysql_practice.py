import pymysql

# 1. 连服务器（Connect）—— 接通昨天的 god_db
conn = pymysql.connect(
    host="localhost",  # 1. 服务器地址：相当于填“快递收件地址”，localhost 就是“本机电脑”
    port=3306,  # 2. 端口号：相当于“门牌号”，MySQL 默认永远住在 3306 房间（注意是数字，不加引号）
    user="root",  # 3. 用户名：相当于“登录账号”，root 是最高管理员
    password="123456",  # 4. 密码：相当于“门禁密码”（字符串，必须加引号）
    database="god_db",  # 5. 数据库名：告诉 Python 进门后直接打开哪个“文件夹”（不填就不知道去哪找表）
    charset="utf8mb4",  # 6. 字符编码：防止中文乱码的“翻译官”（固定写 utf8mb4，能兼容所有汉字和表情）
)

# 2. 派办事员（Cursor）
cursor = conn.cursor()

# 3. 下达指令（Execute）—— 把昨天多表联查的 SQL 搬进来！
sql = """
SELECT s.name, s.score, c.class_name, c.teacher
FROM student s
INNER JOIN class_info c ON s.class_id = c.class_id
ORDER BY s.score DESC;
"""
cursor.execute(sql)

# 4. 拿回结果并收工（Fetch & Close）
# 注意：纯查询（SELECT）没有修改数据，所以不需要 conn.commit()
results = cursor.fetchall()  # 一次性把查到的所有行取回来

print("从 MySQL 成功读取到的数据：")
for row in results:
    print(row)

cursor.close()
conn.close()
