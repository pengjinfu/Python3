#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12
# 实现功能

# 定义保存所有学生信息的列表
card_list = []
target_info = {}

# 1.显示菜单界面


def func_show_menu():
    print("*" * 30)
    print("欢迎使用[名片管理系统]V1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 30)


def add_card():
    """新建名片"""
    # 1.提示用户选择功能
    print("功能：新建名片")
    # 2.接收用户的输入
    # str_name = input("请输入你的名字：")
    # str_phone = input("请输入你的电话：")
    # str_qq = input("请输入你的qq：")
    # # str_mail = input("请输入你的邮箱：")
    # 2.1定义一个字典用来保存当前添加的信息
    card_info = {"name": input("请输入姓名："),
                 "phone": input("请输入电话："),
                 "qq": input("请输入qq："),
                 "mail": input("请输入邮箱：")}

    # 3.把学生信息字典添加到列表
    card_list.append(card_info)
    # print(card_list)
    # 提示用户名片添加成为
    print("添加%s的成功" % card_info["name"])


def show_all():
    """显示全部"""
    # 1.提示用户选择的功能
    print("功能：显示全部")
    # 2.判断是否有名片信息如果没有给，则后面的代码不执行，并给用户提示
    if len(card_list) == 0:
        print("提示：没有任何名片记录")
        return
    # 2.显示表头
    print("姓名\t\t电话\t\tqq\t\t邮箱")  # TODO 写到这了
    print("-" * 30)
    # 3.把列表中所有的学生信息格式展现出来
    for card_info in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %
              (card_info["name"],
               card_info["phone"],
               card_info["qq"],
               card_info["mail"]))
    # for i in card_list:
    #     print("%s\t\t%s\t\t%s\t\t%s" %
    #           (i["name"],
    #            i["phone"],
    #            i["qq"],
    #            i["mail"]))
    print("-" * 30)


def search_card():
    """查询名片"""
    # 1.提示用户选择的功能
    print("功能: 查询名片")
    # 2.安全性判断,如果没有名片信息,提示用户,并让函数中的后续代码不执行
    if len(card_list) == 0:
        print("没有任何名片信息!")
        return
    # 3.让用户输入要查询姓名
    target_name = input("请输入查询的姓名: ")

    # 4.遍历名片列表,取出每一个名片字典
    for card_info in card_list:
        # 5.拿要查询的姓名和名片字典中name这个key对应的value比较
        if target_name == card_info["name"]:
            # 5.1 输出表头
            show_table_head()

            print("%s\t\t%s\t\t%s\t\t%s" % (card_info["name"], card_info["phone"], card_info["qq"], card_info["mail"]))
            print("-" * 30)
            # 6.TODO 对查询到的名片进行高级处理
            deal_card(card_info)

            break  # 结束循环并且不让for后面的else执行
    else:
        print("没有找到%s" % target_name)


def show_table_head():
    """显示表头"""
    print("姓名\t\t电话\t\tqq\t\t邮箱")
    print("-" * 30)


def deal_card(target_info):
    """处理名片"""
    while True:  # 无限循环
        # 1.让用户输入对查询到的名片要做什么 处理
        cmd_num = input("请输入对名片的操作: 1.修改/ 2.删除/ 0.返回上一级: ")
        # 2.判断指令做相应操作
        if cmd_num == "1":  # 修改名片
            update_card(target_info)
            break
        elif cmd_num == "2":  # 删除名片
            card_list.remove(target_info)
            print("名片删除成功")
            break
        elif cmd_num == "0":  # 返回上一级
            break
        else:  # 输入有误,请重新输入
            print("输入有误,请重新输入")


def update_card(target_info):
    """修改名片"""
    target_info["name"] = input("请输入姓名:")
    target_info["phone"] = input("请输入电话:")
    target_info["qq"] = input("请输入qq:")
    target_info["mail"] = input("请输入邮箱:")
    print("%s 的名片修改成功" % target_info["name"])
