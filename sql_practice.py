# day1 牛客网sql记录
#----sql1:查询所有列，*代表所有列
select * from user_profile;

#----sql2:查询多列，各个列名之间用英文逗号隔开
select device_id,gender,age,university from user_profile;

#----sql3:查询结果去重，用distinct
select distint university from user_profile;

#或者先查询然后用group by分组结果一样
select university from user_profile group by university;

#----sql4:查询结果限制返回行数  最后边加个limit 数字就行，中间要有空格
select device_id from user_prodile limit 2;

#----sql5:把查询后的列重新命名，加上限制行数 用as就行
select device_id as user_infos_example from user_profile limit 2;

#----sql6:查找完然后排序  用select查询，order by后边跟排序条件，asc升序 desc降序
select device_id,age from user_profile order by age asc;

#----sql7:查找后多个排序，查询时把先按照什么排序的先查，order by 写一次就行
select device_id,gpa,age from user_profile order by gpa asc,age asc;

#----sql8:查找后多列降序排序,就是改成desc
select device_id,gpa,age from user_profile order by gpa desc,age desc;
