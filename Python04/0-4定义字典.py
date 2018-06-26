#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""
字典作用：存储多个数据，描述一个物体的信息
格式：{key1：value1，key2：value2，key3：value3，...}
查询：字典[key]
"""
dic1t = {"name": "小明", "age": 18, "boy": True}
print(dic1t)
print(type(dic1t))

# 获取字典中指定的key对应数据
name1 = dic1t["name"]
print(name1)

# 修改：若存在键值对，则修改，若不存在则在末尾创建
dic1t["name"] = "小绁"
dic1t["name2"] = "lishi"
print(dic1t)

"""
可变类型：列表，字典
不可变类型：元组，字符串，整形，浮点型，布尔型  
什么是不可变：如元组，如果一但被定义，
"""

