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

# 模拟常量：用大写定义后不要再改了
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


# 程序的主入口
def main():
    # 1.初始化pygam库。让计算机硬件做装备，如果想要音效或文字
    pygame.init()

    # 2.创建窗口
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # 3.加载图片文件，返回图片对象
    # 加载背景图片
    bg_img = pygame.image.load("res/img_bg_level_1.jpg")
    # 加载英雄飞机图片
    hero_plane_img = pygame.image.load("res/hero2.png")

    # 定义一个 x,y 用来记录飞机的位置
    x = 196
    y = 500

    while True:
        # 4.贴图（指定坐标，将图片绘制到窗口）
        window.blit(bg_img, (0, 0))

        # 添加飞机到窗口上
        window.blit(hero_plane_img, (x, y))

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

            # 3.键盘获取长按事件
            # 获取当前键盘所有按键的状态（按下、没有按下），返回bool元组（0，0，0，1，0，0，0）
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            x -=3
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            x +=3
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            y +=3
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            y -=3

if __name__ == '__main__':
    main()
