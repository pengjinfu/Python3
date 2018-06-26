#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11


# def func1():
#     print("func1开始")
#     print("func1结束")
#
#
# def func2():
#     print("func2开始")
#     func1()
#     print("func2结束")
#
#
# def func3():
#     print("func3开始")
#     func2()
#     print("func3结束")
#
#
# func3()


# 定义一个函数打印一行*

def print_line(length,char):
    print(char * length)


def print_lines(count,length,char):

    i = 1
    while i <= count:
        print_line(length,char)  # 定义函数时叫形参，调用函数时叫实参
        i += 1


print_lines(5,10,"*")