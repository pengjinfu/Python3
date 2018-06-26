#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.9

"""
练习1: 定义⼀个整数变量  age  ，编写代码判断年龄是否正确
要求⼈的年龄在 0-120 之间
2. 练习2: 定义两个整数变量  python_score  、 c_score  ，编写代码判断成绩
要求只要有⼀⻔成绩 > 60 分就算合格
3. 练习3: 定义⼀个布尔型变量  is_employee  ，编写代码判断是否是本公司员⼯
如果不是提示不允许⼊内
"""

age = int(input("请输入你的年龄："))

if (age >= 0) and (age <= 120):
    print("正常人")
else:
    print("非正常人")


print("")


python_score = int(input("请输入你的Python成绩"))

c_score = int(input("请输入你的C成绩"))

if python_score >= 60 or c_score >= 60:
    print("你过了")
else:
    print("加油，继续努力！")

print("")


is_employee = True

if is_employee:
    print("允许入内")
else:
    print("请出去")