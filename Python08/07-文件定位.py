#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.17

"""对文件的读写操作都会影响"""

with open("123.txt","a+",encoding="utf-8") as f:
    # 查询当前 文件定位
    print(f.tell())
    f.write("hello")
    print(f.tell())

    # 修改文件的定位
    # offset  偏移多少字节
    # whence： 0 移动定位到开头 1.移动定位不变  2.移动文件到最后
    f.seek(0,0)
    print(f.tell())
    content = f.read()
    print(f.tell())
    print(content)


