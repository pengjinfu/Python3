#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21

"""鸭子类型：不强求数据/对象的类型，只要数据能完成相应的操作，不会报错就行。"""
class Meat(object):
    """肉"""

    def __init__(self, name):
        self.name = name


class Ham(Meat):
    """火腿"""
    pass


class Person(object):

    def eat(self, meat):
        print("小哥哥要吃%s" % meat.name)


man1 = Meat("肉")
man2 = Ham("火腿")

cg = Person()
cg.eat(man2)
