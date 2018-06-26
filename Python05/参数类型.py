#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12
"""
1.位置参数/普通参数：
2.默认参数/缺省参数：
3.可变参数/不定长参数



关键词参数：它表示的是实参的地方

"""

"""位置参数/普通参数:有几个位置参数就要有几个实参，实参和位置参数的顺序要一一对应"""


def sum_num(num1,num2):
    result = num1 + num2
    print(result)


sum_num(1,2)


"""默认参数：给形参设置 默认值，如果设置了默认值的形参没有传递实参就用它的默认值。默认参数应该放在非默认参数之后"""


def sum_num1(num1,num2=2):
    result = num1 + num2
    print(result)


sum_num1(1,2)


"""关键字参数：指的是实参的地方给指定的形参设置对应的真实数据，一般关键字实参要放在实参的后面"""


def sum_num2(num1,num2):
    result = num1 + num2
    print(result)


sum_num(1,2)


"""可变参数："""


def sum_num3(*args):  # 在形参前加*告诉Python解释器它是一个可变参数
    result = 0
    for a in args:
        result += a
    print(result)


sum_num3(1,23,4,5)


