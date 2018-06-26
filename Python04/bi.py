#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1


# def money(apple, weight):
#     if apple == 1:
#         price = 10
#     elif apple == 2:
#         price = 8
#     else:
#         price = 12
#     return price * weight
#
#
# pingou = money(1, 100)
# print(pingou)
# print(money(3, 5))
#
# a = [1, 2, 3]
# b = "24568"


name = "⼩明"
# 解释器知道这⾥定义了⼀个函数


def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)
# 只有在调⽤函数时，之前定义的函数才会被执⾏
# 函数执⾏完成之后，会重新回到之前的程序中，继续执⾏后续的代码
say_hello()
print(name)