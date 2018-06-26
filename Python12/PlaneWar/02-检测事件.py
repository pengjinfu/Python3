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

    while True:
    # for i in range(100):
        # 4.贴图（指定坐标，将图片绘制到窗口）
        window.blit(bg_img, (0, 0))

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
                # 判断用户按键操作
                if event.key == K_LEFT or event.key == K_a:
                    print("left")
                if event.key == K_RIGHT or event.key == K_d:
                    print("right")
                if event.key == K_DOWN or event.key == K_w:
                    print("down")
                if event.key == K_UP or event.key == K_s:
                    print("up")
                if event.key == K_SPACE:
                    print("space")


if __name__ == '__main__':
    main()
