#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16

# 推导式：列表、字典、无序集合
# 语法格式：[计算格式 for循环 if判断]
# 语法格式：{key: value for循环 if判断}


# 1 ~10 "1":1  "2":4
# dict1 = {str(i):i**2 for i in range(1,11)}
# print(dict1)

"""字典中的key和value互换"""
# dict1 = {"name":"zhangsan","age":18}
# dict2 = {dict2[key]:key for key in dict2}
# dict2 = {item[1]:item[0] for item in  dict1.items()}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict2)

"""无序集合推导式"""
list1 =["beijing","beihai","shanghai","wuhan","sz""beihai"]
list2 = {city for city in list1 if city.startswith("b")}
print(list2)