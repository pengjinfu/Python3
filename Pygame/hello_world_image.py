#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1
"""
就像Python带有随机，数学或时间等几个模块来为您的程序提供附加功能一样，Pygame框架包括几个模块，这些模块具有绘制图形，播放声音，处理鼠标输入以及其他内容的功能。

GUI与CLI:
您可以使用Python的内置函数编写的Python程序仅通过print（） 和input（）函数处理文本。您的程序可以在屏幕上显示文本，并让用户从键盘输入文本。这种类型的程序有一个命令行界面，或者CLI（发音类似于“攀登”的第一部分，韵文与“天空”）。这些程序有些受限，因为它们无法显示图形，有颜色或使用鼠标。这些CLI程序只能通过input （）函数从键盘获得输入，即使此时用户必须在程序响应输入之前按Enter键。这意味着实时 （即不用等待用户而继续运行代码）动作游戏是不可能的。

Pygame提供了用图形用户界面或GUI （发音为“gooey”）创建程序的功能。与基于文本的CLI不同，带有基于图形的GUI的程序可以显示带有图像和颜色的窗口。

"""

# background_image = ""
# mouse_image = ""
#
# # 导入pygame,sys
# import pygame,sys
#
# # 从pygame.locals中导入所有东西
# from pygame.locals import *
#
# from sys import exit
#
# # pygame初始化
# pygame.init()
#
# # 创建一个窗口并设置窗口的大小
# screen = pygame.display.set_mode((640,480),0,32)
#
# # 设置窗口的标题
# pygame.display.set_caption('Hello World！')
#
# #加载并转换图像
# background = pygame.image.load(background_image).convert()
# mouse_cursor = pygame.image.load(mouse_image).convert_alpha()
#
# while True:  # 主游戏循环
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     # 将背景图画上去
#     screen.blit(background, (0, 0))
#
#     # 获得鼠标位置
#     x, y = pygame.mouse.get_pos()
#
#     # 计算光标的左上角位置
#     x -= mouse_cursor.get_width() / 2
#     y -= mouse_cursor.get_height() / 2
#
#     # 把光标画上
#     screen.blit(mouse_cursor, (x, y))
#
#     pygame.display.update()
# !/usr/bin/env python

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
# 指定图像文件名称

import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit

# 向sys模块借一个exit函数用来退出程序

pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((640, 480), 0, 32)
# 创建了一个窗口
pygame.display.set_caption("Hello, World!")
# 设置窗口标题

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# 加载并转换图像

while True:
    # 游戏主循环

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0, 0))
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()
    # 获得鼠标位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()
    # 刷新一下画面
