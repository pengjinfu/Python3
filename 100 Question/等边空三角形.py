#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

# rows = input("请输入列数：")
# print("")
# for i in range(0,rows+1):
#     for j in range(0,rows - i):
#         print(" ",end="")
#         j += 1
#     for k in range(0,2 * i - 1):
#         for k == 0 or k == 2 *i - 2 or rows == 1:
#             if


for j in range(9, 3, -1):
    for i in range(1, 20):
        if i == j:
            print("*", end="")
        elif i == 20 - j:
            print("*")
            break
        else:
            print(" ", end="")
print("  ")
for j in range(4, 10):
    for i in range(1, 20):
        if i == j:
            print("*", end="")
        elif i == 20 - j:
            print("*")
            break
        else:
            print(" ", end="")
