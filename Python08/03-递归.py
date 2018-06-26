#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16


# 递归就是 函数内部调用函数本身 小心使用，不然就死循环了

# 1-4  4 + 3 + 2 + 1  num += i
# 1-4 4 * 3 * 2 * 1  num *= i   num * (num -1)


# def func_num(num1):
#     result = 1
#     i = 1
#     while i <= num1:
#         result =result * i
#         i += 1
#     print(result)
#
# result = 1
# for i in range(1,5):
#     result *= i
# print(result)
# func_num(4)
#
# def func_num(num1):
#     if num1 == 1:
#         return 1   # 递归时，必须要在某种条件成立是，返回明确数据，不然就会死循环
#     return num1 * func_num(num1 - 1)
#
#
# print(func_num(4))

def func_num(num1):
    if num1 == 1:
        return 1   # 递归时，必须要在某种条件成立是，返回明确数据，不然就会死循环
    return num1 + func_num(num1 - 1)


print(func_num(100))

# Python它的递归最大深度
# def func(num1):
#     print(num1)
#     func(num1+1)


# func(1)
