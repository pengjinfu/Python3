#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.17

import os

# 1.文件生命名
# os.rename("[复件]123.txt","258.txt")

# 2.删除文件
os.remove("258.txt")

# 3.创建文件夹
os.mkdir("demo")

# 4.获取当前文件夹中的所有内容
print(os.listdir("demo"))

# 5.修改当前目录
os.chdir("demo")

# 6.获取当前目录路径
print(os.getcwd())

# 7.删除目录
os.rmdir("demo")  # 只能删除空件


