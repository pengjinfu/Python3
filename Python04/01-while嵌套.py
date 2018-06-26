#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""
九九乘法表：
要求：
一、用while循环嵌套
1.输出一个左下角九九乘法表
2.输出一个左上角九九乘法表
3.输出一个右下角九九乘法表
4.输出一个右上角九九乘法表

二、用for循环嵌套
1.输出一个左下角九九乘法表
2.输出一个左上角九九乘法表
3.输出一个右下角九九乘法表
4.输出一个右上角九九乘法表

"""

# 一、用while循环嵌套

# 1.输出一个左下角九九乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        product = j * i
        print("%d*%d=%2d\t" % (j,i,product),end="")
        j += 1
    print("")
    i += 1
print("打印完成")

"""
程序分析：
1.当i = 1时，满足while i <= 9:
2.执行循环体j = 1,满足while j <= i:
3.product = j * i，i = 1,j = 1,product =1
4.按格式输出：1*1=空格1空格空格
5.执行j +=1,j=2
6.跳回while j <= i:，此时2 <= 1,不满足，退出循环
7.执行print("")打印空行
8.执行i +=1，i = 2
--->
9.i = 2满足while i <= 9:
10.执行循环体j = 1,满足while j <= i:
11.product = j * i，i = 2,j = 1,product =2
12.按格式输出：1*2=空格2空格空格
13.执行j +=1,j=2，跳回while j <= i:，条件满足
14.按格式输出：2*2=空格1空格空格，且与1*2=空格2空格空格同一行
15.执行j +=1,j=3
16.跳回while j <= i:，此时3 <= 2,不满足，退出循环
17.执行print("")打印空行
18.执行i +=1，i = 3
.........
"""
# 2.输出一个左上角九九乘法表
i = 9
while i >= 1:
    j = 1
    while j <= i:
        product = j * i
        print("%d*%d=%2d" % (j,i,product),end="   ")
        j += 1
    print("")
    i -= 1
print("打印完成")

"""
程序分析：
1.当i = 9时，满足while i >= 1:
2.执行循环体j = 1,满足while j <= i:
3.product = j * i，i = 9,j = 1,product =9
4.按格式输出：1*9=空格9空格空格
5.执行j +=1,j=2
6.跳回while j <= i:，条件满足
7.product = j * i，i = 9,j = 2,product =18
8.按格式输出：1*9=18空格空格
9.执行j +=1,j=3
........
10.当执行j +=1,j=10时，跳回while j <= i:，条件不满足
11.执行print("")打印空行
12.执行i -=1，i = 8
.........

"""
# 3.输出一个右下角九九乘法表
i = 1
while i <= 9:
    k = 9
    while k>i:
        k -= 1
        print(end="        ")
    j = 1
    while j <= i:
        product = j * i
        print("%d*%d=%2d\t" % (j, i, product), end="")
        j += 1
    print("")
    i += 1
print("打印完成")

"""
程序分析：
1.当i = 1时，满足while i <= 9:
2.执行循环体k = 9,满足while k > i:
3.执行k -= 1,k = 8 ,print(end="        ")，输出8个空
4.执行循环体j = 1,满足while j <= i:
4.按格式输出：1*1=空格1空格空格
5.执行j +=1,j=2
6.跳回while j <= i:，此时2 <= 1,不满足，退出循环
7.执行print("")打印空行
8.执行i +=1，i = 2
--->
9.i = 2满足while i <= 9:
10.执行循环体k = 9,满足while k > i:
11.执行k -= 1,k = 7 ,print(end="        ")，输出8个空
12.执行循环体j = 1,满足while j <= i:
13.product = j * i，i = 2,j = 1,product =2
14.按格式输出：1*2=空格2空格空格
15.执行j +=1,j=2，跳回while j <= i:，条件满足
16.按格式输出：2*2=空格1空格空格，且与1*2=空格2空格空格同一行
17.执行j +=1,j=3
16.跳回while j <= i:，此时3 <= 2,不满足，退出循环
17.执行print("")打印空行
18.执行i +=1，i = 3
.........

"""
# 4.输出一个右上角九九乘法表
i = 9
while i >= 1:
    k = 9
    while k>i:
        k -= 1
        print(end="        ")
    j = 1
    while j <= i:
        product = j * i
        print("%d*%d=%2d\t" % (j, i, product), end="")
        j += 1
    print("")
    i -= 1
print("打印完成")


# 二、用for循环嵌套
# 1.输出一个左下角九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        product = j * i
        print("%d*%d=%2d\t" % (j, i, product), end="")
    print("")
print("打印完成")

"""
1.for i in range(1,10):i产生1~9
2.for j in range(1,i+1):j产生1~10
3.当i = 1时， j = 1,d故product = j * i，product = 1
4.按格式输出：1*1=空格1
5.当i = 2时， j = 1,d故product = j * i，product = 2
6.按格式输出：1*2=空格1
7.当i = 2时，再次执行for j in range(1,i+1): j = 2,d故product = j * i，product = 4
.......

这条语句for j in range(1, i+1):中为什么i要+1？
答：for i in range(1,10):i产生1~9，所以最后j = 10，而不是j = 11

"""

# 2.输出一个左上角九九乘法表
for i in range(9, 0, -1):
    for j in range(1, i+1):
        product = j * i
        print("%d*%d=%2d\t" % (j, i, product), end="")
    print("")
print("打印完成")

"""
1.for i in range(9, 0, -1):产生一个序列i：9，8，6……1
2.for j in range(1, i+1):产生一个序列j：1-9

"""
# 3.输出一个右下角九九乘法表

for i in range(1, 10):
    for k in range(i+1, 10):
        print(end="        ")
    for j in range(1,i+1):
        product = j * i
        print("%d*%d=%2d\t" % (j, i, product), end="")
    print("")
print("打印完成")

# 4.输出一个右上角九九乘法表
for i in range(1, 10):
    for k in range(1,i):
        print(end="        ")
    for j in range(9,i-1,-1):
        print("%d*%d=%2d\t" % (i, j, i * j), end='')
    print("")


# 一条语句输出九九乘法表
print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


