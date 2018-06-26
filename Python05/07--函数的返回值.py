#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11

# 函数的返回值，就是把函数的执行结束返回出来(如果需要使用执行结果，就把它给一个变量）


def func_sum(num1, num2):
    sum_num = num1 + num2
    # print(sum_num)
    return sum_num  # return它的作用返回函数的执行结果，只能在函数内部使用


# 如果函数没有写返回值，默认返回函数就是None
result = func_sum(1, 4)
print(result)
# print("*" * result)
