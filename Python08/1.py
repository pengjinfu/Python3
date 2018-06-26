#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1
def square(n):
    if n == 1:
        print("*")
    else:
        i = 1
        while i <= n:
            if i==1 or i==n: # 打印第一行和最后一行
                print("*  "*5)
            else:
                a=len("*  "* 5)  #  2 <= i <= 4时，a = 10
                print((a - 2 * len("*  ") + 2) )
                print("*"+" "*(a-2*len("*  ")+2)+"*")
            i += 1


print(square(5))