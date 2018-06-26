#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20


class Dog:

    def eat(self):
        print("吃东西")


dog1 = Dog()
dog1.eat()

# 定义属性格式:对象.变量 = 值
dog1.name = "小花"  # 第一次给属性赋值是定义一个属性

print(dog1.name)

dog1.name = "旺财"  # 再次给属性赋值是修改属性
print(dog1.name)


class Cat:
    def eat(self, name, age):
        self.name = name
        self.age = age
        print("我叫%s，我的年龄是%d" % (self.name, self.age))


cat = Cat()
cat.eat("tom", 18)
