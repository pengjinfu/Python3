#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11

print("Hello")


def func_sum():  # 代码执行到函数定义时，它不会走函数的内部的代码，只是把函数名这个标识符，添加到内存中
    sum = 1 + 2
    print(sum)


# 想要在调试时让代码进入函数内部，要使用step into
# step over 不会进行函数内部
func_sum()  # 去内存中查看是否有此标识符，如果有就执行函数内部的代码，没须就跳出

print("Hello")