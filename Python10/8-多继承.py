#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21


"""
Python中支持多继承 格式：class 类名（父类1，父类2）
如果继承的多个父类方法，然后手动去调用指定的父类方法，应用类对象去调用，但不要忘记
"""
class Dog(object):

    def eat(self):
        print("eat bone")


class God(object):

    def fly(self):
        print("fly")

    def eat(self):
        print("eat peak")

# 继承链：Xiaohuang--->Dog---->God---->object 只是表示Xiaohuang继承的顺序，并不表示Dog---->God之间有关系

class Xiaohuang(Dog, God):
    def eat(self):
        God.eat(self)


dog = Xiaohuang()
dog.eat()
dog.fly()
