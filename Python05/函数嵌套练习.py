#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.12


def line(char,length):

    print(char * length)


def lines(char1, len):
    i = 1
    while i <= 5:
        line(char1,len)
        i += 1


lines("*",5)