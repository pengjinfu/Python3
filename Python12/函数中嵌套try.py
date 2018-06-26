#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

def test1():
    print("----test1----")
    print(num)
    print("----test2----")


def test2():
    try:
        print("----test1-1----")
        test1()
        print("----test2-2----")
    except:
        print("----test2异常----")

    print("----test3----")


test2()
print("_……_")