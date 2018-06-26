#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21


class People:

    def __init__(self):
        self.__age = None  # 表示属性没有初始化

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            pass
            # self.__info("age")

    def get_age(self):
        return self.__age

    # def __info(self, property_age):
    #     print("%s属性赋值不成功！" % property_age)


people = People()
people.set_age(20)
print(people.get_age())
