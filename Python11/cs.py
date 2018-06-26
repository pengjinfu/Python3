#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.23

"""
定义类：
class Gun:

属性：
model =  # 枪的型号
damage = # 枪的伤害
bullet_count = 20 # 子弹的数量

方法：
add_bullet_count  # 添加子弹
shoot  # 射击
"""

class Gun:
    """枪类"""

    def __init__(self,model,damage):
        self.model = model  # 枪的型号
        self.damage = damage  # 枪的伤害
        self.bullet_count = 20  # 子弹数量

    def add_bullet_count(self,count):
        self.bullet_count += count

    def shoot(self,enemy):
        if self.bullet_count == 0:
            print("没在子弹了，请及时装弹！")
        else:
            self.bullet_count -= 1
    # TODO 敌人受伤
            enemy.hurt(self)
    def __str__(self):
        return "枪的型号是：%s,枪的伤害是：%d，子弹的数量是：%d" % (self.model,self.damage,self.bullet_count)

"""
定义类型：
class Player:

属性：
name = # 角色
hp = 100 # 血量
gun =  # 玩家拥有枪
state =  # 玩家的状态

方法：
fire (self,enemy)  # 开火
hurt(self,enemy_gun) # 伤害，敌人枪的伤害

"""

class Player:
    """玩家"""
    def __init__(self,name):
        self.name = name  # 玩家
        self.hp = 100  # 血量
        self.gun = None # 玩家的枪
        self.state = "Live"  # 玩家的状态

    def fire(self,enemy):
        """开火"""
        if self.gun is None:
            print("不用怕，上！")
        else:
            self.gun.shoot(enemy)  # 用枪对象调用自己的射击方法

    def hurt(self,enemy_gun):
        """受伤"""
        self.hp = self.hp - enemy_gun.damage    # enemy_gun.damage自己受伤是敌人枪的伤害
        if self.hp > 0:
            print("%s玩家的血量是%d" % (self.name, self.hp))
        else:
            print("%s玩家倒下了！" % self.name)
            self.state = "Over"

    def __str__(self):
        return "[%s]玩家的状态是[%s],血量是[%d],拿的神枪是[%s]" % (self.name,self.state,self.hp,self.gun)


ak47 = Gun("ak47",50)
k98 = Gun("k98",60)

poliice = Player("警察")
poliice.gun = ak47
print(poliice)

badman = Player("Super")
badman.gun = k98
print(badman)

poliice.fire(badman)
badman.fire(poliice)
badman.fire(poliice)
print(poliice)
print(badman)
