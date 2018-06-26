#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.9

"""
⽯头剪⼑布
⽬标:
1. 强化 多个条件 的 逻辑运算
2. 体会  import  导⼊模块（“⼯具包”）的使⽤
需求
1. 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
2. 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
3. ⽐较胜负

序号          规则
1         ⽯头 胜 剪⼑
2         剪⼑ 胜 布
3         布 胜 ⽯头
"""

import random

computer = random.randint(1,3)

for i in range(1,7):
    guess = int(input("你有六次机会，请输入⽯头（1）／剪⼑（2）／布（3）:"))
    if guess < 4:
        if ((guess == 1 and computer == 2) or
            (guess == 2 and computer == 3) or
            (guess == 3 and computer == 1)):
            print("第%d次猜,电脑出的数是%d.噢耶！！！电脑弱爆了！！！"%(i,computer))
        elif guess == computer:
            print("第%d次猜,电脑出的数是%d.⼼有灵犀，再来⼀盘！"%(i,computer))
        else:
            print("第%d次猜,电脑出的数是%d.不⾏，我要和你决战到天亮！"%(i,computer))
    else:
        print("第%d次猜,电脑出的数是%d.输入无效，请重新输入"%(i,computer))
    i += 1
    if i == 7:
        print("你的次数用完了")