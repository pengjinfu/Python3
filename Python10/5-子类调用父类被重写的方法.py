#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21

"""
如果子类重写了父类中的方法后还想调用父类中被重写的方法，诮两种方法。
通过类名创建出来的对象：实例对象
"""
class Dog(object):

    def eat(self):
        print("吃骨头")

    def drink(self):
        print("mile")


class XTQ(Dog):

    def eat(self):
        # 调用父类被重写的方法有两种
        # 第一种方法
        # Dog.eat(self)  # 如果用类名直接调用方法时需要手动传递self
        
        # 第二种方式：
        # super(类对象，实例对象）.方法（）
        # 如果super中指定的类对象，就是super所在的类，那么这个类对象可省略不用写
        # 如果super中指定的实例对象，就是super所在方法的，此实例对象可省略不用写
        # super(XTQ, self).eat()  # 如果是单继承尽量用super
        super().eat()
        print("吃蟠桃")
        

xiaotq = XTQ()
xiaotq.eat()