#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11


# 参数的作用：给函数内部使用 优点：增加函数的通用性或灵活性
# 参数就是给将来调用函数的真实数据占位置
# 定义函数时写的参数叫形参
def func_sum(num1, num2):  # 在定义函数后面的小括号中写的东西叫参数
    sum = num1 + num2
    print(sum)


# 调用函数时写的参数叫实参
func_sum(2, 6)  # 函数调用时，里面的数据叫真实数据 叫实参
# func_sum()  # 如果函数设置了参数，在调用时必须传入对应的真实参数
