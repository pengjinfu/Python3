#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20

"""
类是用来描述对象的：定义对象的属性和方法
对象的组成：属性-->记录对象的数据   方法-->完成对象的功能或操作

定义的格式：
class 类名：
    定义属性

    定义方法
类名：要用大驼峰
"""


class Dog:
    """定义狗类"""
    def drink(self):  # 方法第一个参数默认为self
         print(self)
         print("喝可乐")

# 通过类创建对象
# 创建对象格式： 变量 = 类名()
dog1 = Dog()  # 创建对象
# 调用方法格式：对象.方法名（）
dog1.drink()
print(dog1)