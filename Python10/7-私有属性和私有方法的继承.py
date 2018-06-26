#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21


"""
普通的属性和方法是可以被继承的
私有属性和私有方法不会继承
"""


class Father(object):

    def __init__(self):
        self.__type = "人"

    def body(self):
        print("卷发")


class Son(Father):
    pass


son = Son()
son.body()
print(son.name)
