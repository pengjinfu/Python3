#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16
# 文件读取
# with open("123.txt", "r",encoding="utf-8") as f:  # 读取大文件时不能用read因为它是直接读取文件中的全部内容,可能会导致内存紧张
#     count = f.read()
#     print(count)


# 如果是读取大文件 用readline()每次读取一行 减少内存占用
# with open("123.txt","r",encoding="utf-8") as f:
#     while True:
#         count = f.readline()
#         if len(count) == 0:
#             break
#         print(count,end="")

with open("123.txt","r",encoding="utf-8") as f:
    count = f.readlines()  # 返回一个列表,列表中装的是每一行的内容,每一行的内容作为列表的一个内容
    print(count)
