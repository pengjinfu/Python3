#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""
推导式：快捷生成列表数据的表达式
格式：[计算公式 for循环]

"""

# list1 = []
# for i in range(1,101):
#     list1.append(i)
# print(list1)


"""列表推导式："""
# list1 = [i for i in range(1,101)]
# print(list1)
# list1 = [i+1 for i in range(100)]
# print(list1)


"""生成一个1-10中的偶数平方列表"""
# list1 = []
# for i in range(1,11):
#     if i % 2 ==0:
#         list1.append(i**2)
# print(list1)

# list1 = [i**2 for i in range(1,11) if i % 2 == 0]
# print(list1)
# list1 = [i**2 for i in range(2,11,2)]
# print(list1)

"""10个666"""
# list1 = ["666" for _ in range(10)]
# print(list1)

"""数据过滤"""
list1 = ["zhangsan","lisi","wangwu"]
list2 = {name for name in list1 if len(name) > 4}
print(list2)