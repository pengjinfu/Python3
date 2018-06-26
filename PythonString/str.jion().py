#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""

函数：string.join()

Python中有join()和os.path.join()两个函数，具体作用如下：
1.join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
2.os.path.join()：  将多个路径组合后返回

一、函数说明
1、join()函数
语法：  'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素字符串、列表、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串

2、os.path.join()函数
语法：  os.path.join(path1[,path2[,......]])
返回值：将多个路径组合后返回
注：第一个绝对路径之前的参数将被忽略

"""

# 实例如下:

# 对字符串进行操作
seq = "hello good boy doiido"
print(':'.join(seq))


# 对序列进行操作（分别使用' '与':'作为分隔符）
seq = ['hello', 'good', 'boy', 'doiido']
print(' '.join(seq))
print(':'.join(seq))


# 对元组进行操作
seq3 = ('hello', 'good', 'boy', 'doiido')
print(':'.join(seq3))

# 对字典进行操作
seq4 = {'hello': 1, 'good': 2, 'boy': 3, 'doiido': 4}
print(':'.join(seq4))


# 对集合进行操作
seq = {'hello', 'good', 'boy', 'doiido'}
print(':'.join(seq))


# 合并目录
import os
os.path.join('/hello/', 'good/boy/', 'doiido')


# 注意：str.join(sequence) 函数中的 sequence 中的元素必须的字符串，否则会报错，例如：
"""

seq = ['a','b',1,2]
jn = '-'
jn.join(seq)

TypeError: sequence item 2: expected str instance, int found
"""
