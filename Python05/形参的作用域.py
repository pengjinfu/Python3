#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12


# 形参它只能在定义函数内部使用，其它地方都无法使用
# 变量尽量不和形参同名，但是两个不同的函数可以有同名的形参互不影响
# 当形参和变量同名时，定义函数优先使用形参，在函数外部只会用到变量
def sum_num(a,b):
    print(a)
    print(b)
