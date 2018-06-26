#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12


"""
函数定义和调用不是指书写顺序，是指它的执行顺序
"""
print("开始")


def fun():

    print("fun开始")
    print("-fun--")


def fun1():
    print("fun开始")
    fun()
    print("-fun1--")


fun1()