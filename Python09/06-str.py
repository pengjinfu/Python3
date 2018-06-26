#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20
"""
用print输出对象时，它内部自动调用了_str_方法

"""

class Dog:

    def __init__(self,name):
        self.name = name

    def __str__(self):  # 此方法只能返回字符串
        return "小狗的名字叫%s" % self.name

dog1 = Dog("小龙")
print(dog1)