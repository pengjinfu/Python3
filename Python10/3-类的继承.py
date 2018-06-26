#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21

"""
当两个类有相同的方法和属性时，就可以使用继承
在继承中被继承的类称为父类，要继承的的类称为子类
继承之后子类可以拥有父类中所有的方法和属性
所在的类默认都会继承object，它是所有类的基类
"""


# class Dog:  # 经典写法
class Dog(object):  # 新式写法
    def eat(self):
        print("吃骨头")

    def drink(self):
        print("喝牛奶")


class XTQ(Dog):
    def fly(self):
        print("飞一会儿！")
    # def eat(self):
    #     print("吃骨头")
    #
    # def drink(self):
    #     print("喝牛奶")


xiaotq = XTQ()
xiaotq.drink()
xiaotq.fly()