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

#----sql21:
