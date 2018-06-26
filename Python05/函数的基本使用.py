#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12


"""
函数两步：
1.定义函数： 制造工具  编写功能代码
2.调用函数： 使用工具  执行功能代码

格式：定义函数

def 函数名():
    函数内的功能代码
    ........

调用函数：
函数名()

函数的作用：提高代码的可读性，减少代码的冗余性，提高写代码的效率
"""


def func():
    print("Hello Python")


func()


def table():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            product = j * i
            print("%d*%d=%2d"%(j,i,product),end="\t")
            j += 1
        print("")
        i +=1
    print("打印完成")



table()


