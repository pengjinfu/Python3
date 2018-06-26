#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20
"""
属性私有化：就是不让属性在类的外部使用，只能在类的内部使用。
在属性名字的前面加上双下下划线,此属性就变成了私有属性
"""
class Dog:
    def __init__(self):
        # self._age = None
        self.__age = None  # 在属性的前面加 双下划线就是把属性私有化，一般需要提供set或get方法进行间接设置和访问私有属性

    def eat(self):
        print("吃凤翔")
    # 定义一对set和get方法，在set方法中对数据进行安全判断后再使用

    def set_age(self,age):
        if age > 0: # 判断数据满足要求后再使用
            self.__age = age
        else:
            self.__info("age")
    def get_age(self):
        return self.__age

    def __info(self,property_name): # 私有方法也是只能在类的内部使用
        print("%s属性赋值不成功！" % property_name)


dog1 = Dog()
# dog1.age = -10   # 脏数据 垃圾数据
dog1.set_age(-10)
print(dog1.get_age())

# print(dog1.age)