#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11

"""位置参数：普通参数，形参的个数和实参个数一一对应"""


def func_sum(num1,num2):
    sum_num = num1 + num2

    print(sum_num)

func_sum(1,2)


"""默认参数：给形参设置默认值，如果将设置过默认值的形参没有给它设置对应的实参，它会用默认，如果没有设置实参就没有调用时的实参。设置了默认参数的形参应该在没设置默认参数的后面"""


def func1(num1, num2=2):
    sum_num1 = num1 + num2

    print(sum_num1)


func1(5)


"""关键字参数:给形参指定的实参  如果要设置给形参指定实参 要指定就全指定"""


def func2(num1,num2):
    sum_num2 = num1 + num2
    print(sum_num2)
    print(num1)
    print(num2)


func2(num2=2,num1=1)


"""可变参数"""


def func3(*args):  #定义可变参数时 参数前面加* 它是告诉Python解释器，它是一个可变参数，可接收任意个参数

    sum_num = 0
    for var in args:
        sum_num += var
    print(args)


func3(5, 6, 8)  # 用可变参数时，它会把多个实参 自动组包成元组
