#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11

# 函数的作用提升代码的可读性，（减少代码冗余，重复代码只用写一遍就可以），而且代码可以重复使用
# 乘法口诀表

def func_multi_table():  # 定义函数
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            product = j * i
            print("%d*%d=%2d"%(j,i,product),end="\t")
            j += 1
        print("")
        i += 1
    print("打印完成")


func_multi_table()