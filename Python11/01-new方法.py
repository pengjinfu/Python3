#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21
"""
# 1.new方法也是一种魔法方法，创建对象时，系统会自动调用new方法。
# 2.开发者可以实现new方法来自定义对象的创建过程。
# """
# class Dog:
#     """狗类"""
#     pass
#
#
# dog1 = Dog()
# print(dog1)
#
# # 模拟对象创建的过程
# def Dog_():
#     # 1.创建对象，给创建出来的对象在内存空间分配内存空间
#     new_obj = Dog.__new__(Dog)   # new方法是object中的方法，因为它是静态方法，不会再自动传递类对象，需要手动传递，传递时，一定要注意，应该传你要创建的那个对象。
#     # new_obj = object.__new__(Dog)
#
#     # 2.对象的初始化，定义属性
#     new_obj.__init__()
#
#     # 3.把创建好的对象返回
#     return new_obj
#
#
# dog2 = Dog_()
# print(dog2)

"""
创建实例对象时：类名（） 1.调用__new__方法创建对象，开辟一个空间  2.调用__init__方法对象初始化

"""
class Dog:
    pass


dog1 = Dog()
print(dog1)


def Dog_instance():
    """模拟实例对象创建过程"""
    # 1.调用new方法
    # dog_instance = object.__new__(Dog)
    dog_instance = Dog.__new__(Dog)  # nwe方法中传递什么类对象就会创建什么类对象
     # 2.调用init方法
    dog_instance.__init__()
    # 3.把创建的实例对象返回
    return dog_instance

dog2 = Dog_instance()
print(dog2)
