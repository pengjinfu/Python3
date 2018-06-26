#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

list1 = [1,2,3]
list2 = [1,2,3]

# # == 判断两侧的数据值是否相等
# if list1 == list2:
#     print("Ture")


# is 判断的是两侧变量的内存地址是否相同
if list1 is list2:
    print("Ture")
else:
    print("False")

print(id(list1))
print(id(list2))

# is 在判断是None 或 False 或 Ture 时用，其它一般用 ==
# 值相同内存地址不定相同，但内存地址相同值一定相同