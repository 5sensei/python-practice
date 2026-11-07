#sql书写顺序
from babel.util import distinct
from pandas.conftest import join_type

import analyze

SELECT   (你要查的列)
FROM     (从哪张表)
WHERE    (过滤原始数据的条件) —— 必须在 GROUP BY 前面！
GROUP BY (按什么分组)
HAVING   (过滤分组后数据的条件) —— 必须在 GROUP BY 后面！
ORDER BY (最后排序)






# day1 牛客网sql记录
#----sql1:查询所有列，*代表所有列
select * from user_profile;

#----sql2:查询多列，各个列名之间用英文逗号隔开
select device_id,gender,age,university from user_profile;

#----sql3:查询结果去重，用distinct
select distint university from user_profile;

#或者先查询然后用group by分组结果一样
select university from user_profile group by university;

#----sql4:查询结果限制只返回到第几行  最后边加个limit 数字就行，中间要有空格
select device_id from user_prodile limit 2;

#----sql5:把查询后的列重新命名，加上限制行数 用as就行
select device_id as user_infos_example from user_profile limit 2;

#----sql6:查找完然后排序  用select查询，order by后边跟排序条件，asc升序 desc降序
select device_id,age from user_profile order by age asc;

#----sql7:查找后多个排序，查询时把先按照什么排序的先查，order by 写一次就行
select device_id,gpa,age from user_profile order by gpa asc,age asc;

#----sql8:查找后多列降序排序,就是改成desc
select device_id,gpa,age from user_profile order by gpa desc,age desc;

#----sql9:查找指定类别的目标，用where 类别 = ‘目标’
select device_id,university from user_profile where university = '北京大学';

#----sql10:查找类别大于、小于目标的。用where  目标 >=或者<=
select device_id ,gender,age,university from user_profile where age >= 24;

#----sql11:查找位于某个区间的目标。用where 目标 between xx and xx
select device_id,gender,age from user_profile where age between 20 and 23;

#----sql12:查找不要具体某个小分类的时候，用where !=
select device_id,gender,age,university from user_profile where university != '复旦大学';

#----sql13:返回值中需要去除空值的，就用where !=''，单引号里面放空就行
select device_id,gender,age,university from user_profile where age !='';

#----sql14:查找的条件有多个并且限定范围，用and连接
select device_id,gender,age,university,gpa from user_profile where gender = 'male' and gpa > 3.5;

#----sql15:营想要找到学校为北大或GPA在3.7以上(不包括3.7)的用户进行调研，请你取出相关数据
select device_id,gender,age,university,gpa from user_profile where university = '北京大学' or gpa > 3.7

#----sql16:运营想要找到学校为北大、复旦和山大的同学进行调研，请你取出相关数据
select device_id,gender,age,university,gpa from user_profile where university  in
('北京大学','复旦大学','山东大学') # 不用not in 是因为之后如果加入新数据会一起查出来，除非硬性要求，还有就是加了in 的话后面的内容需要带括号

#----sql17:运营想要找到gpa在3.5以上(不包括3.5)的山东大学用户 或 gpa在3.8以上(不包括3.8)的复旦大学同学进行用户调研，请你取出相应数据,取出的数据按照device_id升序排列
select device_id,gender,university,age from user_profile
where (gpa >3.5 and university in ('山东大学')) # and连接里面的小句子，or连接外部的大句子
   or (gpa >3.8 and university in ('复旦大学'))
order by device_id asc;

#----sql18:在运营想查看所有大学中带有"北京"的用户的信息(device_id,age,university)，请你取出相应数据
select device_id,age,university from user_profile where university like '%北京%';# 查找相关字眼用where   like，字眼用%包起来

#----sql19:运营想要知道复旦大学学生gpa最高值是多少，请你取出相应数据
select max(gpa) as gpa from user_profile; #最大值最小值要用括号包住，正常不用加as gpa，这边是因为牛客网的判断太死板硬性gpa，日常自己写可以随便取名，只要括号里的东西跟库的一样就行
#方法二：把查询出来的结果按照gpa降序排，限制到第一个
select gpa from user_profile where university = '复旦大学' order by gpa desc limit 1;

#----sql20:运营想要看一下男性用户有多少人以及他们的平均gpa是多少，果使用round保留到小数点后面1位
select
count(gender) as male_num # 此处as列名为题目要求，可自定义,count表示数一数gender这列里面有几行
round(avg(gpa),1) from user_profile # round表示四舍五入，保留几位小数就写几
where gender = 'male'; #题目限制男性

#----sql21:运营想要对每个学校不同性别的用户活跃情况和发帖数量进行分析，请分别计算出每个学校每种性别的用户数、30天内平均活跃天数和平均发帖数量。查询返回结果需要对性别和学校分组，示例如下，结果保留1位小数，1位小数之后的四舍五入,查询出来的结果按照gender、university升序排列：
select
gender,university,
count(*) as user_num, # 填*代表数几行的时候即使是空值也纳入只要符合筛选条件，如果填的是具体列名则不会计入
round(avg(ctive_days_within_30),1) as avg_active_day,
round(avg(question_cnt),1) as avg_question_cnt
group by gender,university
order by gender asc,university asc;

#----sql22:取出平均发贴数低于5的学校或平均回帖数小于20的学校。
select
university,
round(avg(question_cnt), 3) as avg_question_cnt,
round(avg(answer_cnt), 3) as avg_answer_cnt
from user_profile
group by
university
having # 为什么不用where?因为这边的排序要求是精化过的平均数，用having，where用于原始数据，且where在分组前，having在分组后
vg_question_cnt < 5 or avg_answer_cnt <20

#----sql23:现在运营想要查看不同大学的用户平均发帖情况，并期望结果按照平均发帖情况进行升序排列，请你取出相应数据。
select
university,
round(avg(question_cnt),4) as avg_question_cnt
from user_profile  #从哪个表来的，经常容易忘记
group by
university
order by
avg_question_cnt asc

#----sql24:这题是多表关联查询，需要用inner join       on来关联两个表
select
a.device_id,a.question_id,a.result
from
question_practice_detail as a
inner join
user_profile as b
on a.device_id = b.device_id and university = '浙江大学'
order by
question_id asc

#----sql25:计算“平均答题数 = 总答题次数 ÷ 答过题的不同用户数”。也是需要连接多个表
select
a.university,
round(count(b.question_cnt) / count(distinct a.device_id),4) as avg_answer_cnt
from
user_profile as a
inner join
question_practice_detail as b
on a.device_id = b.device_id
group by university
order by university asc

#----sql26:关联三个表，就是一个接一个的inner join，inner join对于没有内容的值会直接丢弃，而left join则会给予空值null保留
select
a.university
c.difficult_level,
round(count( b.question_id) / count(distinct b.device_id),4) as avg_answer_cnt # 根据题目要求的平均判断为b表的数据来计算
from
user_profile as a
inner join  #第一个内连接
question_practice_detail as b
on a.device_id = b.device_id  #on表示根据这列把两个表连接起来
inner join  #第二个内连接
question_detail as c
on b.question_id = c.question_id
group by
a.university,
c.difficult_level

#----sql27:关联三个表，查看参加了答题的山东大学的用户在不同难度下的平均答题题目数，学了前两题做这个就简单多了
select
a.university,
c.difficult_level,
round(count(b.question_id)/count(distinct b.device_id),4) as avg_answer_cnt  #取平均时候人数记得去重
from
user_profile as a
inner join
question_practice_detail as b
on a.device_id = b.device_id
inner join
question_detail as c
on b.question_id = c.question_id and university = '山东大学'
group by  #题目说了不同难度，所以要按照难度分组
difficult_level
order by
avg_answer_cnt asc