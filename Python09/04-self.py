#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20
"""
self:只代表类创建的对象
当调用对象的属性时，最好用self 去访问
调用方法时，不用给slef传参数，python3解释器，默认把类创建的对象作为self实参传递
"""
class Dog:

    def drink(self):
        print("%s喝青岛" % self.name)


dog1 = Dog()
dog1.name = "旺财"
dog1.drink()

dog2 = Dog()
dog2.name = "来福"
dog2.drink()
print(dog1.name)
print(dog2.name)




