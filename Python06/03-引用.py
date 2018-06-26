#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12

"""普通变量的引用"""
# c = 10
# a = 10
# b = a
#
#
# print(id(a))
# print(id(b))
# print(id(c))


"""列表引用"""
# a = [1,2,3]
# b = a
# a.append(4)
# c = [1,2,3,4]
# print(id(a))
# print(id(a))
# print(id(c))
# print(a)
# print(b)


"""小数字缓存池： -5 ~256 python解析一运行就全部分配好内存"""
# a = -6
# b = -6
#
# c = 256
# d = int(25.6 * 10)
#
# e = 100000  # 在交互模式中 不会对大数据进行缓存
# f = 100000
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

"""字符串也有缓存 最大缓存位数是20位"""
str1 = "hello"
str2 = "hello"

print(id(str1))
print(id(str2))
