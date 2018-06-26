#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22
# Animal相对于Python来说是：类对象
class Animal:

    animal_type = "狗" # 创建在类内，且独立在方法外的变量是：类属性
    print(id(animal_type))
    __color = "black" # 私有类属性

    def __init__(self, name, age): # 方法
        self.name = name
        self.age = age
        print("这只动物的名字是：%s，年龄是%d" % (self.name, self.age))


# dog为通过Animal类创建的对象叫做：实例对象
dog = Animal("tom", 12)

# 通过实例对象定义的属性叫做：实例属性
dog.color = "yello"
# 类属性是类对象和实例对象所共有的属性，都可以访问
print(dog.animal_type)
print(Animal.animal_type)
print("-----1")
print(id(dog.animal_type))
print(id(Animal.animal_type))
print("-----2")
Animal.animal_type = "Cat" # 修改类对象：类对象.类属性 = 值

# 在这里我到底是定义了一个实例属性，还是修改了类属性
dog.animal_type = "Dog" # 实例对象修改类属性

print(id(dog.animal_type))
print("-----3")
print(id(Animal.animal_type))
print("-----4")