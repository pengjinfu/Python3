#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.23

class Dog:

    __type = "狗"

    @classmethod   # 修饰符 语法糖  作用:让下面定义的第一个方法变成类方法
    def get_type(cls):   # 调用类方法时Python解释器会自动传递类对象
        return cls.__type

    @staticmethod  # 修饰符 它的作用是让下面的第一个方法成静态,静态方法不会传递self和cls
    def info():
        print("haha")

print(Dog.get_type())

"""
类属性和类方法   用类对象
其它所有尽量用实例对象操作
"""
dog1 = Dog()
dog1.info()
print(dog1.get_type())