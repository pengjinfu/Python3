#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12
"""
可变参数与混合参数混合使用:
l.默认参数和可变参数混合使用时，默认参数放在可变参数的后面
2.默认参数和可变参数混合使用时，想要设置默认参数的值，必须以关键字参数的形式来设置
3.可变参数不能用关键字参数形式来设置


位置参数---->可变参数------>默认值参数
"""


# def fun_sum(*args):
#     sum_num = 0
#     for num in args:
#         sum_num += num
#     print(sum_num)
#
#
# fun_sum(1,2,3)

#
# def fun_sum(*args, is_print=False):
#     print(is_print)
#     print(args)
#
#     sum_num = 0
#     for num in args:
#         sum_num += num
#     if is_print:
#         print(sum_num)
#
#
# fun_sum(True, 1, 2, 3, is_print=True)
#
# """字典形式可变参数 关键字参数的形态"""
#
#
# def func1(a, **kwargs):  # 形参前加**就是告诉Python解释器，此参数是一个字典形的可变参数 要接收 多余的关键字参数
#     # 字典形式的可变参数 把多余的 关键字参数给kwargs 包装成一个字典传给形参
#     print(a)
#     print(kwargs)
#
#
# func1(1, n=2, m=3)
#
# """在实参前加 * """
#
#
# # 在容器前面加变量 前面加* 除了字典 可以进行格式转换
# def func2(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# tuple1 = (1, 2, 3)
# # a.b,c =tuple1
# func2(*tuple1)  # (1,2,3)--->1,2,3
#
# list1 = [1, 2, 3]
# func2(*list1)  # [1,2,3]--->1,2,3
#
# dict1 = {"a":10,"b":20,"c":20}
# func2(**dict1)


# 如果遇到可变参数 里面嵌套调用有可变参数的函数时，要注意它会自动组包成元组或字典，再次传给可变参数时，注意手动解包

def func_sum1(*args, **kwargs):
    print("------------")
    print(args)
    print(kwargs)


def func_sum2(*args, **kwargs):
    print(args)
    print(kwargs)
    # func_sum1((1,2,3),{"m":10,"n":20})
    func_sum1(*args, **kwargs)
    # func_sum1(1,2,3,m = 10 , n = 20)


func_sum2(1, 2, 3, n=10, m=20)
