#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22
# 在项目中创建子文件的作用是把.py分类，方便查找
# 导入包中的模块方式一：import 包名.模块名
import message.message_send

# 使用模块： 包名.模块名.xx    xx可以是模块中的变量或函数/类
print(message.message_send.message_send)

# 导入包中的模块方式二：
from message.message_send import message_send
print(message_send)


