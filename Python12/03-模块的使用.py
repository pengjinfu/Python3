#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

# 任何的.py文件都是模块或工具包，可以被其它.py文件导入使用
# 方法一：

# 格式：import 模块名    注意模块名不要以数字开头，真实开发不用中文名
# import module
# # 使用模块   模块名.xx  xx可以是模块中的变量或函数
# module.fibo(20)


# 方式二
"""
优点:可以导入模块中的局部东西，大大的节省内存
缺点：如果导入的模块有相同变量或函数/类 后导入的会覆盖前面导入

"""
# from module import fibo

# from module import *   # *为通配符，默认导入所有，等价于方式一
# # 使用模块 不用写模块名了
#
# fibo(5)

# import sys
# print(sys.path)  # 获取Python解释器查文件路径，可以手动添加

from  module import *
fibo(5)
