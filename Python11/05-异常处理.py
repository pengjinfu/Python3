#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22
# 发行量避免程序出错
# 异常处理的目的就 代码可能出错，让程序出错后不要直接崩溃退出，而是提示错误信息，继续后续执行
# 如果用了try语法，后面必须跟except或finally，else可以不写。
try:  # 如果代码很可能出错，就把此代码放在try里面
    path = input("请输入文件路径：")
    with open(path, "r") as f:
        content = f.read
        print(content)
    # print(a)
# except FileNotFoundError:  # 只拦截文件未找到的错误，别的什么也不管
#     print("文件未找到！")
# except NameError as error:
#     print("%s名字出错" % error)
except Exception as  error:   # 可以拦截到所有用户类型，as可以获取到错误的详细信息
    print("%s出错了！" % error)
else:
    print("如果try里面的代码正常执行，没有出错就会走else")
print("后续处理！")
