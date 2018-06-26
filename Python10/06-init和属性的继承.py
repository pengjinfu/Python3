#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20

class Dog:
    def __init__(self,name):
        self.name = "哮天犬"


class XTQ(Dog):
    def __init__(self):
        super().__init__()  # 重写父类方法之后再手动调用父类方法
        self.color = "black"


xiaotq = XTQ()
print(xiaotq.name)