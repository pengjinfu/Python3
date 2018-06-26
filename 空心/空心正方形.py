#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 打印正方形
# 分为三个部分
# 第一部分 ：打印上边，占位20个*
for i in range(20):
    # 加入判断，是为了在每隔一个空格打印一个*，刚好是偶数的位置：例如 i == 2 or i == 4 or i == 6.........的时候，打印*
    # end = "" ，意思是不换行，直接到下一个
    if i % 2 == 0:
        print("*", end="")
    else:
        print(" ", end="")
print() #这里要记得必须换行，因为第一部分完毕后没有换行，可以试试

# 第二部分
# 相对简单，第0个位置和最后一个位置打印*就可以了
# 外面的j循环是控制行数，里面的i循环控制每一行哪个位置打印*
for j in range(8):
    for i in range(20):
        # 判断i的数值就是判断在哪里打印*
        # i = 0 和 i = 18的位置
        if i == 0:
            print("*", end="")
        elif i == 20 - 2:
            print("*")
            break
        else:
            print(" ", end="")
# 第三部分
# 和第一部分一样
for i in range(20):
    if i % 2 == 0:
        print("*", end="")
    else:
        print(" ", end="")