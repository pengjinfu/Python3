#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20

"""
双下划线开头和双下划线结尾的方法，叫做魔法方法或运算符重载方法,这些方法有特殊的含义
"""
class Dog:
    def __init__(self,name,age):
        self.tapy = "小狗"
        self.name = name
        self.age = age
        print("My name is %s，age is %d" % (self.name, self.age))


# 如果init方法中的属性在初始值不想写死，就给init方法加上形参，但加上形参后，创建对象的类名（）中，实参要与形参一一对应。
dog1 = Dog("tom",12)
print(dog1.tapy)

dog2 = Dog("dany",2)
print(dog2.tapy)
