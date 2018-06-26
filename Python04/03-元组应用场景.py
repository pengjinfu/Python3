#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1
"""
一、元组是自动组包的默认类型
"""
a = 10, 20, 30  # v如果多个数据赋值给一个变量时，它会自动组包成元组类型
print(type(a))
print(a)

# 解包：列表、元组、字典
tuple1 = (1, 2)
a, b = tuple1
print(a, b)

x, y = 20, 10

# x = x + y
# y = x - y
# x = x - y
# print(x,y)

x, y = y, x
print(x, y)

# 类型转换
list1 = [1, 2, 3, 4]
tuple2 = tuple(list1)
print(tuple2)
list2 = list(tuple2)
print(list2)
str1 = str(list2)
print(str1)
