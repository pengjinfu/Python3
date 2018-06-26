#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16


# def square(n):  # n = 5 时的分析
#     if n == 1:
#         print("*")
#     else:   # 可以for 代替，简单一一点
#         i = 1
#         while i <= n:
#             if i == 1 or i == n:  # 打印第一行和最后一行
#                 print("*  " * 5)  # 一个星，两个空格
#             else:
#                 a = len("*  " * 5)  # 2 <= i <= 4 时，a = 15
#                 print("*" + " " * 11 + "*")  # 中间打印11个空格
#             i += 1
#
#
# def triangle(n): # n = 3 时的分析
#     i = 1
#     while i <= n:
#         if i == 1:
#             print(" " * +(2 * n - 2) + "*")  # 控制第一行打印，两个空格，第三个为星
#         elif i < n:
#             # print((2 * (n + 1 - i) - 2))
#             print(" " * +(2 * (n + 1 - i) - 2) + "*" + " " * (4 * (i - 1) - 1) + "*")  #
#         else:
#             print("*   " * n)
#         i += 1
# while True:
#     cmd_num = input("请输入要打印的图形：1.长方形 /2.三角形/0.退出:")
#     if cmd_num == "1":
#         width = int(input("请输入边长:"))
#         square(width)
#     elif cmd_num == "2":
#         width = int(input("请输入边长:"))
#         triangle(width)
#     elif cmd_num == "0":
#         print("欢迎再次使用")
#         break
#     else:
#         print("你的输入有误，请重新输入！")

import pyttsx3
import time

engine = pyttsx3.init()
with open("name.txt", "r",encoding="utf-8") as f:
    fnamelist = f.read()

engine.say('二零一八枪毙名单点名开始')
engine.runAndWait()
time.sleep(1)

for S in fnamelist:
    engine.say(S)
    engine.runAndWait()
    time.sleep(1)

engine.say('点名完毕')
engine.runAndWait()