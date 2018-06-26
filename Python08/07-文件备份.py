#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.16
# 需求 123.txt [复件]123.txt
# 1.接收用户输入的文件名
file_name = input("请输入要复制的文件名:")
# 2.拼接新的文件名字
new_file_name ="[复件]" + file_name

index = file_name.rindex(".")
new_file_name = file_name[:index] + "[复件]" + file_name[index:]
# 3.读取原谅伯,写入到复件中
with open(file_name,"r") as old_f:
    with open(new_file_name,"w") as new_f:
        count = old_f.read()  # 读取旧文件
        new_f.write(count)
