#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12


# def sum_num():
#     """只能做2+3"""
#     result = 2 + 3
#     print(result)
#
#
# sum_num()

# 定义函数时定的参数 叫形参
# 参数的作用：它可以将外部的数据传递到函数内部使用，为将来真实的数据进行占位
# 优点：增加函数灵活性，通用
def sum_num(a,b):   # 的函数名后面括号中写的变量叫做形参
    """此函数用于两个数求和"""
    result = a + b
    print(result)


# 如果函数定义了形参，则在传递真实数据时，实参的个数要与形参 一一对应，否则会报错
sum_num(10,20)   # 调用函数时，传递的真实数据叫实参

