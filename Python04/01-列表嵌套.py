#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""
⼀个学校，有3个办公室，现在有8位⽼师等待⼯位的分配，请编写程序:
1> 完成随机的分配
2> 获取办公室信息 (每个办公室中的⼈数，及分别是谁)
"""

import  random

# 1.定义列表表示8位老师
teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]

# 定义一个大列表，用于表示所有办公室
office = [[],[],[]]

# 遍历老师列表的每个老师
for name in teachers:
    # offices = office[random.randint(0,2)]  # 随机选择大列表中小办公室
    # offices.append(name) # 把老师插到小办公室里
    offices = office[random.randint(0,2)].append(name)
print(office)

i = 1
for offices in office:
    print("第%d个办公室有%d个老师"%(i,(len(offices))))
    i += 1
    for name in offices:
        print(name)
