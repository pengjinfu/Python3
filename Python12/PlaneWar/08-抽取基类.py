#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

# 1.创建窗口
# 2.加载背景图片
# 3.背景图片贴到窗口
# 4.刷新窗口

import pygame  # 模块分两种 静态模块.py  动态模块.py (windows  .dll  .pyd) linux  .os
import sys
from pygame.locals import *
import time
import random

# 模拟常量：用大写定义后不要再改了
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 760


class BasePlane:

    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)  # 英雄图片路径
        # 英雄飞机第一次出现在窗口的位置
        self.x = x
        self.y = y
        # 窗口
        self.window = window

    def display(self):
        """显示英雄飞机图片"""
        self.window.blit(self.img, (self.x, self.y))


class Bullet:
    """子弹"""

    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)  # 子弹图片路径
        # 子弹出现在窗口的位置
        self.x = x
        self.y = y
        # 子弹所在的窗口
        self.window = window

    def display(self):
        """显示子弹图片"""
        self.window.blit(self.img, (self.x, self.y))

    def bullet_move(self):
        """子弹移动"""
        self.y -= 10

    def __del__(self):
        """对象释放时自动调用"""
        print("子弹销毁了！")


class HeroPlane(BasePlane):
    """英雄飞机"""

    def __init__(self, img_path, x, y, window):
        super().__init__(img_path, x, y, window)

        self.bullets = []  # 保存所有发射的子弹

    def display(self):
        """显示英雄飞机图片"""
        self.window.blit(self.img, (self.x, self.y))

    def move_left(self):
        """飞机向左移"""
        if (self.x - 8) >= 0:
            self.x -= 8

    def move_right(self):
        """飞机向右移"""
        if (self.x + 8) <= 395:
            self.x += 8

    def move_down(self):
        """飞机向下移"""
        if (self.y + 8) <= 700:
            self.y += 8

    def move_up(self):
        """飞机向上移"""
        if 0 < (self.y - 8):
            self.y -= 8

    def fire(self):
        """发射子弹"""
        # 创建子弹对象
        # 子弹的x = 飞机的x + 飞机的宽度 * 0.5 - 子弹宽度 * 0.5
        # 子弹的y = 飞机的y - 子弹的高
        bullet = Bullet("res/bullet_9.png", self.x + 50, self.y - 31, self.window)
        # bullet.display()
        # 把发射过的子弹添加到列表中保存起来
        self.bullets.append(bullet)

    def display_bullet(self):
        """处理子弹图"""
        del_bullet = []
        for bullet in self.bullets:  # 取出一个个子弹
            if bullet.y >= 31:
                bullet.display()  # 每一个子弹重复贴图
                bullet.bullet_move()  # 让子弹飞
            else:
                # self.bullets.remove(bullet)  # 让超出边界的子弹销毁
                del_bullet.append(bullet)
        for bullet1 in del_bullet:
            self.bullets.remove(bullet1)


class EnemyPlane(BasePlane):
    """敌机"""

    def enemy_move(self):
        """敌机移动"""
        self.y += 5
        if self.y >= WINDOW_HEIGHT:
            self.y = random.randint(-300, -68)
            self.x = random.randint(0, WINDOW_WIDTH - 100)
            self.img = pygame.image.load("res/img-plane_%d.png" % random.randint(1, 7))


# 程序的主入口
def main():
    # 1.初始化pygam库。让计算机硬件做装备，如果想要音效或文字
    pygame.init()

    # 2.创建窗口
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # 3.加载图片文件，返回图片对象
    # 加载背景图片
    bg_img = pygame.image.load("res/img_bg_level_1.jpg")

    # 创建英雄飞机对象
    hero_plane = HeroPlane("res/hero2.png", 196, 500, window)

    # 创建敌机
    enemy_list = []
    for _ in range(105):
        enemy_plane = EnemyPlane("res/img-plane_%d.png" % random.randint(1, 7), random.randint(0, WINDOW_WIDTH - 100),
                                 random.randint(-300, -68), window)
        enemy_list.append(enemy_plane)
    while True:
        # 4.贴图（指定坐标，将图片绘制到窗口）
        window.blit(bg_img, (0, 0))

        # 添加飞机到窗口上
        hero_plane.display()

        # 添加敌机到窗口上
        for enemy_plane in enemy_list:
            enemy_plane.display()
            enemy_plane.enemy_move()
        # 把子弹对象重新贴图
        # for bullet in hero_plane.bullets:  # 取出一个个子弹
        #     bullet.display()  # 每一个子弹重复贴图
        #     bullet.bullet_move()  # 让子弹飞
        hero_plane.display_bullet()
        # 5.刷新界面，不刷新不会更新内容
        pygame.display.update()

        # 检测事件
        for event in pygame.event.get():
            # 1.鼠标点击关闭窗口事件
            if event.type == QUIT:
                print("点击关闭窗口按钮")
                sys.exit()  # 关闭程序
            # 2.键盘按下事件
            if event.type == KEYDOWN:
                # # 判断用户按键操作
                # if event.key == K_LEFT or event.key == K_a:
                #     x -= 5
                #     print("left")
                # if event.key == K_RIGHT or event.key == K_d:
                #     x += 5
                #     print("right")
                # if event.key == K_DOWN or event.key == K_w:
                #     y += 5
                #     print("down")
                # if event.key == K_UP or event.key == K_s:
                #     y -= 5
                #     print("up")
                if event.key == K_SPACE:
                    print("space")
                    hero_plane.fire()
            # 3.键盘获取长按事件
            # 获取当前键盘所有按键的状态（按下、没有按下），返回bool元组（0，0，0，1，0，0，0）
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            hero_plane.move_left()
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            hero_plane.move_right()
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            hero_plane.move_down()
        elif pressed_keys[K_UP] or pressed_keys[K_w]:
            hero_plane.move_up()

        # 让每一次的循环停0.01，降低循环的执行速度
        time.sleep(0.01)  # 降低CPU的消耗
        print(len(hero_plane.bullets))


if __name__ == '__main__':
    main()
