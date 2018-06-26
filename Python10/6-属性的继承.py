#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21

"""
当子类继承父类就可以拥有父类中的属性
当子类想要定义自独有的属性时，需要在子类中重写init方法，但是重写后父类的属性就不会被继承
如果还想拥有父类的属性，需要用super调用父类被重写的init方法，继承拥有父类中的属性。
"""


class Father(object):

    def __init__(self):
        self.type = "人"


class Son(Father):

    def __init__(self):
        # super(Son, self).__init__()
        super().__init__()
        self.color = "yello"


people = Son()
print(people.type)
print(people.color)
