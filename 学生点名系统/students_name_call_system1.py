#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

#点名程序

import random,os,sys

# 点名程序
import random
import os,sys

called = set()   # 指定一个空集合，用来剔除已经遍历的名称
f = open('name.txt','r',encoding="utf-8")  # 打开文件读取姓名
data = f.read()   # 读取的数据，默认读取所有，括号里加数字制定只读取多少字符
data1 = data.split('、')  # 分割字符串生成列表
f.close()     #关闭打开文件
#循环遍历
while True:
    try:
        rdata = random.sample(data1, 1) # 这是一个只有一个元素的列表
        strdata = ''.join(rdata) # 将列表转化为字符串
        c = '\033[32mEnter Press\033[0m'
        if c != 'q':
            data1.remove(strdata)
            if strdata not in called:
                print(strdata)
                called.add(strdata)
        else:
            break
    except ValueError as e:
        print('\033[31m姓名已遍历所有，将推出程序！\033[0m')
        break