#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16
"""
以表达式的方式来定义函数
应用场景：自定义排序规则
格式：lambda 参数 1，参数 2：内部实现
"""
# 匿名函数：就是没有名字的函数 只能做一些简单的处理，如果功能复杂就老实用回普通函数
# 匿名函数应用场景：此函数功能简单，并且只用一次，定义完了就要去执行的，可以考虑用匿名函数
# 语法格式： lambda  参数1 ,参数2 ：返回值


# def func_sum(num1,num2):
#     return num1+num2
#
#
# result = func_sum(1,2)
# print(result)

"""匿名函数的第一种使用"""
# func = lambda  num1,num2:num1 + num2   # 此写法前面的变量是在接收到函数
# result = func(1,2)
# print(result)

"""匿名函数常用的方法，定义并直接调用"""
result = (lambda num1, num2: num1 + num2)(1, 2)   # 此写法前面的变量是在接收到函数的返回值
print(result)


stu = [{"name":"zhangsan","age":18},{"name":"Lisi","age":17},{"name":"wangwu","age":19}]

stu.sort(key=lambda x: x["name"])
print(stu)

stu.sort(key=lambda x: x["age"])
print(stu)