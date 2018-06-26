#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12


"""

函数返回值作用：就是将调用执行结果，让函数中的某个数据返回给调用的调用者
如果调用完调用需要拿到函数执行结果或函数中的某个数据时，此时就函数有返回值
想让函数有返回值时需要用return关键词，此关键字只能在函数内部使用

"""


def sum_num(num1, num2):
    result = num1 + num2

    return result


re = sum_num(12, 3)
print(re)
