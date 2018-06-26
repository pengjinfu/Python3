#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

import itchat
itchat.login()
# 抓取自己好友的信息，并返回json文件
friends = itchat.get_friends(update=True)[:0]

# 初始化计数器
male = female = other =0
for i in friends[1:]:
    sex = i["sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 计算自己朋友总数
total = len(friends[1:])

print("男性好友：%.2f%%" % (float(male)/total*100)+"\n"
      +"女性好友：%.2f%%" % (float(female)/total*100)+"\n"
      +"不明性别好友：%.2f%%" % (float(male)/total*100)+"\n")

