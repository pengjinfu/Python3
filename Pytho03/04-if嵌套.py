#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.9

"""
⽕⻋站安检
需求:
1. 定义布尔型变量  has_ticket  表示是否有⻋票
2. 定义整型变量  knife_length  表示⼑的⻓度，单位：厘⽶
3. ⾸先检查是否有⻋票，如果有，才允许进⾏ 安检
4. 安检时，需要检查⼑的⻓度，判断是否超过 20 厘⽶
如果超过 20 厘⽶，提示⼑的⻓度，不允许上⻋
如果不超过 20 厘⽶，安检通过
5. 如果没有⻋票，不允许进⻔
"""
has_ticket = input("有没有票：")


if has_ticket == "有":
    print("准备安检")
    knife_length = int(input("刀的长度："))
    if knife_length >= 20:
        print("请跟我走一趟")
    else:
        print("请上车")
else:
    print("请买票")
    ticket = input("火车票，动车，高铁（1/2/3）：")
    if ticket == "1":
        print("请安检过后，走火车通道")
    elif ticket == "2":
        print("请安检过后，走动车通道")
    elif ticket == "3":
        print("请安检过后，走高铁通道")
    else:
        print("请买票")
print("一路顺风")
