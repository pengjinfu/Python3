# usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""

题目3：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？

程序分析：
1.先给定这个数的范围：10万以内
2.sqrt(i+100)= x  --->x*x = （i+100）
3.sqrt(i+268)= y  --->x*x = （i+268）
4.判断：x*x = （i+100）and x*x = （i+268）是否同时满足
5.打印输出：print（i）

"""

# 导入math包

import math

for i in range(10000):

    # 要转换成整形
    x = int (math.sqrt(i + 100))  # 利用数学平方函数
    y = int (math.sqrt(i + 268))

    if(x * x == i + 100) and (y * y == i + 268):
        print("这个数就是:%d"%i)

