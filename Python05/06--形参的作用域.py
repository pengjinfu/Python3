#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11

a = 100   # 全局变量


# 全局变量最好不要和形参同名
def func_sum(a):  # 定义函数，a是形参
    # 形参的作用域（可使用的范围），只能在自己的函数内部使用
    print(a)


# 不同函数的形参名可以是同名的，其相互不影响，各用各的
def func1(a):
    print(a)


func_sum(5)
func1(10)
print(a)