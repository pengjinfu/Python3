#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

# 当try进而的代码出现异常后，它会自动创建一个指定类型的异常对象
# try:
#     # print(a)
#     raise NameError("name is not define")  # 手动创建异常对象并抛出
# except NameError as error:  # error =   NameError("name is not define") 抛出异常后会自动把异常对象赋值给as后面的对象
#     print("提示：%s" % error)
# 自定义异常类：自定义的异常类，必须要继承Exception
# class CustomExcepteion(Exception):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "%s" % self.name
#
#
# while True:
#     try:
#         phone_num = input("请输入电话号码：")
#         if len(phone_num) != 11:
#             # print("你输入的号码位数不对！")
#             raise CustomExcepteion("你输入的号码位数不对！")
#         elif phone_num.isdecimal() is False:
#             # print("您输入的手机号码不合法！")
#             raise CustomExcepteion("您输入的手机号码不合法！")
#
#     except CustomExcepteion as error:
#         print(error)
#         # 创建一个小窗口
#         # 窗口上显示提示信息
#     else:
#         print("输入正确")




