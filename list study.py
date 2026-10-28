#换gemini给的方向来复习列表
yigeliebiao = ["神",2778,"true"]
print(yigeliebiao)
print(type(yigeliebiao))
print(yigeliebiao[1])
print(yigeliebiao[-2])

a_new_list = [[9,1],[7,8]]
print(a_new_list[0][0])
print(a_new_list[0][1])
print(a_new_list[1][0])
print(a_new_list[1][1])

# 列表的常用操作
# 1.查询数据在列表的位置  .index

mylist =[5,1,7,8]
suoyin = mylist.index(8)
print(suoyin)

# 2.修改列表中的元素
mylist[0]=9
print(mylist)

# 3.元素的插入 .insert
mylist.insert(2,7)
print(mylist)

# 4.元素的追加(直接追加)  .append
mylist.append(886)
print(mylist)

# 把其它数据列表的内容取出，依次追加到列表尾部  .extend
mylist.extend([7,7,8])
print(mylist)

# 5.删除列表指定元素 del列表  或者列表.pop
del mylist[2]
mylist.pop(4)
print(mylist)

# 6.删除列表第一个匹配项 .remove
mylist.remove(7)
print(mylist)

# 7.清空列表 .clear
mylist.clear()
print(mylist)

# 8.统计某元素数量 .count
wlist =[1,1,1,1,2]
a=wlist.count(1)
print(a)

# 9.统计列表所有元素数量 len
b=len(wlist)
print(b)

# 10.用while循环遍历列表元素,可以制定循环条件，任何场景都能用
mlist = [1,2,3,4,5,6,7]
index = 0
while index < len(mlist):       #循环变量需要顶格写
       m = mlist[index]
       print(f"{m}")

       index +=1

# 11.用for循环遍历
klist=[1,2,3,4,5,6,7]
for k in klist:
    print(f"{k}")
