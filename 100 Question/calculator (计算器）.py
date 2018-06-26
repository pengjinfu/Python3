#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""

知识点：
1.函数的定义
2.if……elif……else的使用
3.print（）

"""
# 定义函数
def add(x,y):
    """相加"""
    return x + y

def subtraction(x,y):
    """相减"""
    return x - y


def multiply(x, y):
    """相乘"""

    return x * y


def divide(x, y):
    """相除"""

    return x / y

def round_numbers (x, y):
    """取整"""

    return x // y

def leave(x, y):
    """取余"""

    return x // y

def power_function (x, y):
    """取幂"""

    return x ** y


# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
print("5、取整")
print("6、取余")
print("7、幂")

choice = input("输入你的选择(1/2/3/4/5/6/7):")

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == '5':
    print(num1, "//", num2, "=", round_numbers(num1, num2))

elif choice == '6':
    print(num1, "%", num2, "=", leave(num1, num2))

elif choice == '7':
    print(num1, "**", num2, "=", power_function(num1, num2))

else:
    print("非法输入")