#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.15
"""系统工具，用于实现各种功能"""

card_list = []


# 1.系统界面欢迎
def sys_menu():
    print("_" * 50)
    print("欢迎使用【名片管理系统】V1.2")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("_" * 50)


# 2.功能操作

# 2.1新键名片
def new_card():
    """新建名片"""
    # 提示用户操作功能
    print("功能：新建名片")
    # 请用户输入名片信息
    card_info = {}  # 用字典来存储名片信息
    card_info["name"] = input("请输入名字：")
    card_info["phone"] = input("请输入电话：")
    card_info["qq"] = input("请输入qq：")
    card_info["mail"] = input("请输入邮箱：")

    # 用列表来接收字典名片
    card_list.append(card_info)

    # 提示用户添加功能成功
    print("添加%s的姓名成功！" %  card_info["name"])


# 2.2查看全部
def show_all():
    """查看全部"""
    # 提示用户操作功能
    print("功能：查看全部")
    # 判断是否有名片信息
    if len(card_list) == 0:
        print("没有名片信息！")
        return
    # 打印表头
    print("*" * 50)
    print("姓名\t\t电话\t\tqq\t\t邮箱\t\t")
    # 遍历所有的名片信息
    for card_info in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %
              (card_info["name"],
               card_info["phone"],
               card_info["qq"],
               card_info["mail"]))
    print("*" * 50)


# 2.2查询名片
def view_card():
    """查询名片"""
    # 提示用户操作功能
    print("功能：查询名片")
    # 判断是否有名片信息，并提示
    if len(card_list) == 0:
        print("没有名片信息!")
        return
    # 提示用户输入查询的姓名
    target_name = input("请输入要查询的姓名：")
    # 遍历名片信息列表，对数据进行比较
    for card_info in card_list:
        if target_name == card_info["name"]:
            # 打印表头
            print("*" * 50)
            print("姓名\t\t电话\t\tqq\t\t邮箱\t\t")
            # 按格式输出所有的用户名片信息
            print("%s\t\t%s\t\t%s\t\t%s" %
                  (card_info["name"],
                   card_info["phone"],
                   card_info["qq"],
                   card_info["mail"]))
            print("*" * 50)
            # 高级操作 TODO
            high_op(card_info)
            break
    else:
        print("你要查询的信息没有找到！")


# 2.2.1修改名片/删除名片
def high_op(target_info):
    """名片高级操作"""
    while True:
        # 提示用户要进行的操作
        usr_cmd = input("请输入你要进行的操作：1.修改/2.删除/0.返回上一级：")
        # 根据用户命令进行不同的操作
        if usr_cmd == "1":
            # 对名片进行修改
            update_card(target_info)
            # target_info["name"] = input("请输入姓名:")
            # target_info["phone"] = input("请输入电话:")
            # target_info["qq"] = input("请输入qq:")
            # target_info["mail"] = input("请输入邮箱:")
            # print("%s 的名片修改成功" % target_info["name"])
            break
        elif usr_cmd == "2":
            card_list.remove(target_info)
            break
        elif usr_cmd == "0":
            break
        else:
            print("你的输入有误，请重新输入")


def update_card(target_info):
    """修改名片"""
    target_info["name"] = input("请输入姓名:")
    target_info["phone"] = input("请输入电话:")
    target_info["qq"] = input("请输入qq:")
    target_info["mail"] = input("请输入邮箱:")
    print("%s 的名片修改成功" % target_info["name"])