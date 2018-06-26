#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1


def func():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            product = j * i
            print("%d*%d=%d" % (j, i, product),end="\t")
            j += 1
        print("")
        i += 1
    print("打印完成")