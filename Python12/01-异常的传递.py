#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

# 当try嵌套时，如果内层的try后面的except不能正常捕获异常，它会把异常抛出，传过外层的except，
# try:
#     f = open("123.txt","r")   # 如果try里面的代码出现异常后，当前try内部的后续代码不会再执行，而是执行except中的代码，及外边的代码
#     try:
#         conten = f.read()
#         print(conten)
#         print(a)
#         # 因为上一名异常，则try后续代码不会执行了，即下面一句不会被打印
#         print("88888")
#     except FileNotFoundError:
#         print("文件不存在！")
# except Exception:  # 可以拦截所有的异常
#     print("出现异常")
# print("haha")


"""
当try后面的代码出错时，会立即执行相对应的except代码，且程序不会终止，except后续代码继续执行
如果try里面的代码没有出错，相对应的except代码不会被执行
如果使用了try，就必须用except或finally，否则会报错，else可有可不有,而且finally和else只能使用一次
"""

try:
    f = open("12311.txt","r")
    content = f.read()
    print(content)
    f.close()
except Exception as error:
    print(error)

