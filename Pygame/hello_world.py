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

# 导入pygame，sys
# 从pygame.locals导入*

# 导入pygame，sys包
import pygame,sys

# 从pygame.locals中导入所有东西
from pygame.locals import *

# pygame初始化
pygame.init()

# 设置窗口的大小
DisplaySurf = pygame.display.set_mode((500,400))

# 设置窗口的标题
pygame.display.set_caption('Hello World！')

while True:  # 主游戏循环
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
