#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1
dict1 = {"name":"123","age":18}
"""增加键值"""
dict1["boy"] = True
print(dict1)

"""删除键值对"""
# del dict1["boy"]  #删除指定的键值对

age = dict1.pop("age")
print(dict1)

"""修改对应的值"""
dict1["name"] = "小明"

