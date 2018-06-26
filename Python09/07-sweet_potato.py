#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.20

"""
class SweetPotato:

state = "生的"

"""


class SweetPotato:
    """"""

    def __init__(self):
        self.state = "生的"
        self.cook_time = 0

    def cook(self,time):
        """"""
        self.cook_time = self.cook_time + time
        if self.cook_time >= 0 and self.cook_time < 3:
            self.state = "生的"
        elif self.cook_time >= 3 and self.cook_time < 6:
            self.state = "半生不熟"
        elif self.cook_time >= 6 and self.cook_time < 8:
            self.state = "可以吃了"
        else:
            print("有毒了")

    def __str__(self):
        return ("地瓜状态为%s，烧烤总时间为%d" % (self.state,self.cook_time))


digua1 = SweetPotato()
digua1.cook(1)
print(digua1) # 地瓜状态:⽣的, 烧烤总时间:1
digua1.cook(2)
print(digua1) # 地瓜状态:半⽣不熟, 烧烤总时间:3
digua1.cook(3)
print(digua1) # 地瓜状态:熟了, 烧烤总时间:6
digua1.cook(3)
print(digua1) # 地瓜状态:烤糊了, 烧烤总时间:9