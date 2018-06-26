#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1


import itchat, time
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' %
                    (msg['ActualNickName'],
                     msg['Content']), msg['FromUserName'])


itchat.auto_login(True)  # 登陆的时候使用命令行显示二维码
itchat.run()
# 获取自己的用户信息，返回自己的属性字典
itchat.get_friends()
# 获取特定 UserName 的用户信息
itchat.get_friends(userName='@abcdefg1234567')
# 获取任何一项等于 name 键值的用户
itchat.get_friends(name='littlecodersh')
# 获取分别对应相应键值的用户
itchat.get_friends(wechatAccount='littlecodersh')
# 三、四项功能可以一同使用
itchat.get_friends(name='LittleCoder 机器人', wechatAccount = 'littlecodersh')