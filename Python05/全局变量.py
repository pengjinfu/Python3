#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12
"""
在函数外部定义的变量叫全局变量
作用域：在定义那一行之后的整个.py文件中使用

"""

a = 20


def fun():
    global a  # 如果在函数内部想要给全局变量用=号的方式给全局变量赋值，就必须先声明全局变量
    a = 10   # 在函数内部给变量赋值,默认都是定义一个新的局部变量
    print(a)


fun(50)

print(a)