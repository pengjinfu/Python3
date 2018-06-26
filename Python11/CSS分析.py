#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22
"""
class Gun 枪类

属性
model 型号
damage  伤害
bullet_count 子弹当量

方法
add_bullet_count（self,count)  添加子弹
shoot(self) 射击
重写str方法


class Player 玩家类

属性
name 角色
gun 玩家拥有的枪保存
hp 血量 默认100
state  玩家状态
方法
fire(self) 开枪     判断是否有枪，查看是否有子弹，有则射击
hurt(self) 受伤     提示玩家受伤，血量过少则死亡

"""