# 今天把mysql连接到pycharm然后开始建立数据库做练习，以下是今天练习的代码
create database if not exists god_db;
use god_db;
create table if not exists student (
    id int auto_increment primary key , -- 自动递增学生编号，设置id为主键
    name varchar(50),
    score int
);
show tables;
select * from student;
INSERT INTO student (name,score) VALUES
('神',100),
('小宝',99),
('53分龙',53);
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS class_info;

-- 1.创建班级表
CREATE TABLE class_info (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(50),
    teacher VARCHAR(50)
);
-- 2.创建学生表（带班级编号）
CREATE TABLE STUDENT (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    score INT,
    class_id INT
);

-- 3.写入原始数据
INSERT INTO class_info VALUES (101,'人工智能一班','划水郭'),(102,'人工智能二班','认真苏');
INSERT INTO student (name,score,class_id) VALUES
('王大帅',100,101),
('琴小宝',99,101),
('猪小肉',99,101),
('路人',66,102),
('不相干',1,NULL); -- 注意：不相干没有分配班级
UPDATE student
SET score = 0
WHERE name = '路人';
SELECT DISTINCT name,score
FROM student
WHERE class_id = 101 and score >= 80
ORDER BY score DESC;
TRUNCATE TABLE student;
INSERT INTO student (name, score, class_id) VALUES
('张三', 95, 101),
('李四', 88, 101),
('王五', 65, 102),
('赵六', 76, 102),
('孙七', 92, NULL);
SELECT name, score
FROM student
WHERE class_id = 101 and score >= 80
ORDER BY score DESC;
SELECT s.name,s.score,c.class_name,c.teacher
FROM student AS s
INNER JOIN class_info AS c ON s.class_id = c.class_id;
SELECT class_id,ROUND(AVG(score),3) AS avg_score
FROM student
WHERE class_id IS NOT NULL
GROUP BY class_id
HAVING avg_score > 0;