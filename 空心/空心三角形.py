#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 空心三角形

# for i in range(1, 20):
#     if i == 10:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 9:
#         print("*", end="")
#     elif i == 11:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 8:
#         print("*", end="")
#     elif i == 12:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 7:
#         print("*", end="")
#     elif i == 13:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 6:
#         print("*", end="")
#     elif i == 14:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
#
# for i in range(1, 20):
#     if i == 5:
#         print("*", end="")
#     elif i == 15:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 4:
#         print("*", end="")
#     elif i == 16:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 3 or i == 5 or i == 7 or i == 9 or i == 11 or i == 13 or i == 15 or i == 17:
#         print("*", end="")
#     else:
#         print(" ", end="")


# 打印空心等边三角形
# 分成三部分

# 当用到break的时候，就是打印了足够的*，停止循环
# 第一部分
# 当你希望三角形的底值为20时候，*要打印在中间位置
# for i in range(1, 20):
#     if i == 10:
#         print("*")
#         break
#     else:
#         print(" ", end="")
# # 第二部分
# # 根据上面的草稿，每打印一行，两边的距离都会有规律的变化
# # j循环控制行数，i循环控制每行在哪个位置打印*
# for j in range(9, 1, -1):
#     for i in range(1, 20):
#         # i控制打印的位置，当i=9时候则打印*，j就是代表*从中间10的位置开始分化，
#         # 打印*的位置分别是[9,11] [8,12] [7,13] [6,14] [5,15] [4,16].....[i,j].... i + j = 20
#         if i == j:
#             print("*", end="")
#         elif i == 20 - j:
#             print("*")
#             break
#         else:
#             print(" ", end="")
#
# # 第三部分
# # 和打印正方形的底一样，要判断每隔一个空格就要打印一个*，位置刚好是奇数：i == 1 or i == 3 or i == 5。。。。的时候，打印*
# for i in range(1, 20):
#     if i % 2 != 0:
#         print("*", end="")
#     else:
#         print(" ", end="")
# Num = int(input("请输入行数:"))

# triangle_set

num = int(input("请输入你要打印的行数："))
#
# # 直角实心三角形
# for i in range(num + 1):
#     print("*" * i)
#
# # 直角空心三角形
# for j in range(1, num + 1):
#     if j == 1:
#         print("*" * j, end="")
#     elif 1 < j < num:
#         print("*" + " " * (j - 1) + "*", end="")
#     else:
#         print("*" * (j + 1))
#     print("")
#
# # 等边实心三角形
# for i in range(num + 1):
#     for j in range(1, (num + 1) - i):
#         print(end=" ")
#     for k in range(num + 1 - i, num + 1):
#         print("$", end=" ")
#
#     print("")

# 和打印三角形是一样的
for j in range(10, 1, -1):
    for i in range(1, 20):
        if i == j:
            print("*", end="")
        elif i == 20 - j:
            print("*")
            break
        else:
            print(" ", end="")

# 第三部分
#     *         *
#      *       *
#       *     *
#        *   *
#         * *
for j in range(2, 11):
    for i in range(1, 20):
        if i == j:
            print("*", end="")
        elif i == 20 - j:
            print("*")
            break
        else:
            print(" ", end="")