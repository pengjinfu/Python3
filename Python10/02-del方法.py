#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20

class Dog:
    def __init__(self,name):
        self.name = name

    def __del__(self):
        print("%s要被删除了，销毁了！" % self.name)


dog1 = Dog("tom")
print("******")