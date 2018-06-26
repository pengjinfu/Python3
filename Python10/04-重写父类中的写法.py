#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20

# class Dog:  # 经典的写法
class Dog(object):  # 新式写法 所有的类最终都会继承到object
    def eat(self):
        print("吃骨头")


# 继承的作用：减少代码的冗余，提升代码的可读性和开发效率
# 继承：想拥有某个类的方法或属性时  子类继承父类后，就可以拥有父类中所有的方法和属性
class XTQ(Dog):  # 语法格式：类名（要继承的类/父类）
    # 如果子类有和父类同名的方法，将来执行时，优先调用自己里面的方法
    def eat(self):  # 在子类中定义了一个和父类同名的方法，就叫重写父类的方法
        print("吃仙桃")  # 继承链：当前类----> 直接父类--->……--->object所有的基类



xiaotq = XTQ()
xiaotq.eat()
print()
