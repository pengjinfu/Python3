#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16

# w 写入模式 只能写入 文件不存在,创建文件,文件若存在,写入时会覆盖原来内容

# with open("123.txt","w") as  f:
#     f.write("hello python")

# r 只读模式 只能读取,不能写入 文件不存在会报错

# with open("123.txt","r") as  f:
#     count = f.read()
#     print(count)

# a 追加模式 只能写入,不能读取,如果文件不存在,创建文件,文件若存在,则会在后面文件内光标处添加内容

# with open("123.txt", "a") as  f:
#     # f.write("hello python")
#     count = f.read()
#     print(count)

# 编码

with open("123.txt","w",encoding="utf-8") as  f:
    f.write("hello python,你好世界!")   # 简体中文用的是GBK   繁体BIG
