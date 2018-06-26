#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21
"""
确保某⼀个类只会创建出⼀个实例， 这个类称为单例类， 单例模式是⼀种对象创建类型模式。
"""

# 实例化⼀个单例

# class SingLeton:
#     __name = None # 首次创建的类属性
#
#     def __new__(cls):
#         if cls.__name is None:
#             print("创建对象")
#             cls.__name = super().__new__(cls)
#         return cls.__name
#
#
# num1 = SingLeton()
# print(num1)
# num2 = SingLeton()
# print(num2)


# class SingLeton:
#     __name = None  # 首次创建的类属性
#     __has_init = False  # 记录是否已经初始化
#
#     def __new__(cls):
#         if cls.__name is None:
#             print("创建对象")
#             cls.__name = super().__new__(cls)
#         return cls.__name
#
#     def __init__(self):
#         if not self.__has_init:
#             print("对象初始化")
#             self.type = "猫"
#             self.__has_init = True
#
#
# num1 = SingLeton()
# num1.type = "动漫⼈物"
# print(num1)
# num2 = SingLeton()
# print(num2)


"""
让对象只分配一次内存，只让它执行一次new方法就可以
重写的父类方法，让__new__方法和__init__方法只调用一次
"""


# class ShoppingCar:  # 执行第1步
#     """购物车类"""
#     __instance = None  # 记录创建出来的对象
#     __has_init = False
#
#     def __new__(cls, *args, **kwargs):  # 执行第2步
#         """重写创建对象的方法"""
#         # print("------")    # 执行第4步
#         # 1.调用父类的new方法创建对象
#         if cls.__instance == None:  # 如果对象没有创建过，再去执行创建代码
#             cls.__instance = object.__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self):
#         if ShoppingCar.__has_init is False:
#             self.total_price = 0
#             ShoppingCar.__has_init = True
#
#
# car1 = ShoppingCar()  # 执行第3步
# car1.total_price = 200
# print(car1.total_price)
# print(car1)
#
# car2 = ShoppingCar()
#
# print(car2.total_price)
# print(car2)

class ShoppingCar:
    __instance = None  # 用来记录new方法是否创建了对象
    __has_init = False  # 用来记录init方法是否被操作

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # 若把object改成ShoppingCar,类对象就会一直调用自己的new，成了死循环

        return cls.__instance

    def __init__(self):
        if ShoppingCar.__has_init == False:
            self.price = 200
            ShoppingCar.__has_init = True

gwc1 = ShoppingCar()
gwc1.price = 400
gwc2 = ShoppingCar()

print(gwc1)
print(gwc2)
print(gwc1.price)
print(gwc2.price)
