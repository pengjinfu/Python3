#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.11


# return返回值注意点1：只要执行了函数中的return,return后面的代码就不执行了
def func1():
    print("hello")
    return  12

    print("python")


func1()


# return返回值注意点2：返回值可以同时返回多个值，它会自动组包为元组
def func2():
    return 1,2,3


a,b,c = func2()
print(a,b,c)


# return返回值注意点3：在函数中可以有多个return;只会执行其中的一个
def func_even_num(num1):
    """求奇偶数"""
    if num1 % 2 == 0:
        return "偶数"
    else:
        return "奇数"


print(func_even_num(11))