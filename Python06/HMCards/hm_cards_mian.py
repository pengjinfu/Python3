#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

# 名片管理系统主要业务逻辑

# 导入模块
import hm_cards_tool
"""
重复执行1~3
1.显示菜单界面
2.接收用户输入，相应的命令
3.根据用户输入不同命令做不同的功能

无限循环：程序设计需要，出口
死循环：是程序Bug
"""

while True:
    # 1.显示菜单界面
    hm_cards_tool.func_show_menu()
    # 2.接收用户输入，相应的命令
    cmd_num = input("请选择执行的操作：")
    print("你选择的功能是:%s"%cmd_num)
    # 3.根据用户输入不同命令做不同的功能
    if cmd_num == "1":      # 新建名片
        hm_cards_tool.add_card()
    elif cmd_num == "2":   # 显示全部
        hm_cards_tool.show_all()
    elif cmd_num == "3":   # 查询名片
        hm_cards_tool.search_card()
    elif cmd_num == "0":
        print("退出系统,欢迎再次使用此系统！")
        break
    else:
        print("输入有误，请重新输入")
