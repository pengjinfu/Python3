#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

# 定义枪类
class Gun:
    """枪类"""

    def __init__(self, model, damage):
        self.model = model  # 枪的型号
        self.damage = damage  # 枪的伤害
        self.bullet_count = 50  # 初始化子弹数量

    def add_bullet_count(self, count):
        """添加子弹"""
        self.bullet_count += count

    def shoot(self, enemy):
        """射击方法"""
        if self.bullet_count == 0:
            print("请及时装弹！")
        else:
            self.bullet_count -= 1  # 减少子弹
            # TODO打中敌人后，敌人受伤
            enemy.hurt(self)

    def __str__(self):
        return "我有一把%s枪，枪的伤害是：%d，有%d颗子弹" % (self.model, self.damage, self.bullet_count)


# AK47 = Gun("AK47",100)
# print(AK47)
# AK47.shoot()
# print(AK47)

class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name  # 角色
        self.gun = None  # 玩家拥有的枪
        self.hp = 100  # 血量
        self.state = "live"  # 玩家状态

    def fire(self, enemy):
        """开枪"""
        if self.gun is None:
            print("%s没有枪，没事，上！" % self.name)
        else:
            if self.gun.bullet_count <= 0:  # 有枪没有子弹，就自己加子弹
                self.gun.add_bullet_count(20)
            else:
                self.gun.shoot(enemy)  # 射击敌人

    def hurt(self, enemy_gun):
        """受伤"""
        self.hp -= enemy_gun.damage  # 减血量
        if self.hp > 0:
            print("%s的血量为%d" % (self.name, self.hp))
        else:
            print("%s倒下了！" % self.name)
            self.state = "Over!"

    def __str__(self):
        return "%s玩家,当前状态[%s],当前血量[%d],拥有的神枪[%s]" % (self.name, self.state, self.hp, self.gun)


AK47 = Gun("AK47", 50)
police = Player("警察")
police.gun = AK47
print(police)
badman = Player("pig")
print(badman)
# 警察开枪了

police.fire(badman)
police.fire(badman)
print(police)
print(badman)
