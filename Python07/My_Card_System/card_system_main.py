#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.15
"""名片系统主业务逻辑"""
"""
1~3一直在循环：
1.系统界面要一直显示
2.一直在请求用户输入
3.根据用户输入做相应的操作

"""
import card_system_tool

while True:

    # 1.系统界面
    card_system_tool.sys_menu()
    # 2.用户输入
    usr_cmd = input("请输入你要执行的功能：")
    print("你输入的功能是:%s" % usr_cmd)
    # 3.根据输入做相应的功能
    if usr_cmd == "1":
        card_system_tool.new_card()
    elif usr_cmd == "2":
        card_system_tool.show_all()
    elif usr_cmd == "3":
        card_system_tool.view_card()
    elif usr_cmd == "0":
        print("功能：退出系统")
        print("欢迎再次使用此系统")
        break
    else:
        print("你输入有误，请重新输入")
