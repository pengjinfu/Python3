#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.9

"""
⼥友的节⽇
需求:
1. 定义  holiday_name  字符串变量记录节⽇名称
2. 如果是 情⼈节 应该 买玫瑰／看电影
3. 如果是 平安夜 应该 买苹果／吃⼤餐
4. 如果是 ⽣⽇ 应该 买蛋糕
5. 其他的⽇⼦每天都是节⽇啊…
"""
# elif 它主要强调两种以上额的执行结果
# 逻辑运算符强调一种执行结果

holiday_name = input("请输入节日：")

if holiday_name == "情人节":
    print("买玫瑰")
elif holiday_name == "平安夜":
    print("买苹果")
elif holiday_name == "生日":
    print("买蛋糕")
elif holiday_name == "新年":
    print("发红包")
else:
    print("在家吃狗粮")