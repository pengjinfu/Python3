#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""
元组：存储多个数据 ，每个数据叫元素
格式：（元素1，元素2，...）,元素最好相同
获取元组：索引 --元组[索引]
元组不可变
"""
tuple1 = ("123", "456", "abc", "678")
print(type(tuple1))
print(tuple1)

# 获取元素
print(tuple1[3])
print(tuple1[0])
# 当元组只有一个元素时,会自动根据元素的类型而推导，必须要元素后加一个","
tuple2 = (1)
print(type(tuple2))
print(tuple2)
tuple3 = (1,)
print(type(tuple3))
print(tuple3)