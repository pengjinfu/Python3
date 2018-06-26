#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.9
"""
break和continue作用：

break：某一条件满足时，
continue:

"""
# # break例子
# i = 0
# while i <= 5:
#     print(i)
#     if i == 2:
#         break
#     print("这是第%d次输出打印"%i)
#     i += 1
# print("完成")

i = 0
while i <= 99:
 i += 1
 if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
     continue
 else:
     print(i)

# continue例子
i = 0
while i <= 5:
    print(i)
    if i == 2:
        i += 1
        continue
    print("这是第%d次输出打印"%i)
    i += 1
print("完成")

