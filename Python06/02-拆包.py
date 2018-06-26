#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12
"""拆包/解包和组包/包装"""
tuple1 = (1, 2, 3)
list1 = [1, 2, 3]
str1 = "byte"
dict1 = {"a":10,"b":20,"c":30}
# x =1 , 2 , 3  组包一般都是组成元组
a ,b ,c  = tuple1 # 拆包
a ,b ,c = list1 # 拆包
a, b, c ,d = str1  # 拆包
a, b = dict1  # 拆包默认是key
print(a, b)






