#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21

class Dog:

    def __init__(self):
        self.name = "小花"

    def __del__(self):  # 当对象要释放时，从内存删除时就会调用此方法
        # 在此方法可以做对象的临终遗言，来验证对象是否被删除
        print("%s走了" % self.name)


dog1 = Dog()
print("------")
