#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.10

row = 1
while row <= 5:

    line = 1
    while line <= row:
        line += 1
        if line == 2:
            print("*",end="")

    print()
    row += 1
print("完成")