#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12

"""注意点1：return后面不再写其它代码，当函数中执行了return，函数内部后面的代码将不会再执行"""


def func1():
    a = 10
    return a
    print("""11111""")  # 此语句将不被执行


print(func1())

"""注意点2：return返回值有多个时，调用函数时会自动组包，以元组形式输出"""


def func2():
    return 10, 20, 30  # 当return返回多个值时，会自动组包返回元组


print(func2())

"""注意点3：可以有多个return，但只会返回一个return"""


def func3(num):
    if num % 2 == 0:
        return "这是一个偶数"
    else:
        return "这是一个奇数"



print(func3(2))
