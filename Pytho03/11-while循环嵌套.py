#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.10

i = 1
while i <= 5:
    print("*" * i)
    i += 1


# 在while循环嵌套中，外层循环执行一次，内层循环执行若干次
# 外部的row一般控制行数，外部的line控制列数

row = 1
while row <= 5:

    line = 1
    while line <= row:
        print("*",end="")
        line += 1
    print()
    row += 1
print("完成")

row = 5
while row >= 1:

    line = 1
    while line <= row:
        print("*",end="")
        line += 1
    print()
    row -= 1
print("完成")

row = 1
while row <= 9:

    line = 1
    while line <= row:
        product = line * row
        print("%d*%d=%d" % (line, row, product),end="\t")
        line += 1
    print()
    row += 1
print("完成")

row = 9
while row >= 1:

    line = 1
    while line <= row:
        product = line * row
        print("%d*%d=%d" % (line, row, product),end="\t")
        line += 1
    print()
    row -= 1
print("完成")


row = 1
while row <= 9:
    k = 9
    while k > row :
        print("        ",end="")
        k -= 1
    line = 1
    while line <= row:
        product = line * row
        print("%d*%d=%2d" % (line, row, product),end="\t")
        line += 1
    print()
    row += 1
print("完成")

row = 9
while row >= 1:
    k = 9
    while k > row :
        print("        ",end="")
        k -= 1
    line = 1
    while line <= row:
        product = line * row
        print("%d*%d=%2d" % (line, row, product),end="\t")
        line += 1
    print()
    row -= 1
print("完成")
