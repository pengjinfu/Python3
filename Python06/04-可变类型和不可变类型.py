#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12
"""可变类型和不可变类型"""
# 可变类型就是存储空间中的数据可以改变，地址不变
# 不可变类型就是存储空间中的数据不可以改变

list1 = [1, 2, 3, 4]
print(list1)
print(id(list1))
list1.append(5)
print(id(list1))
print(list1)


"""默认参数最好不要用可变类型"""