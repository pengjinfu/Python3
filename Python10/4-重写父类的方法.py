#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.21

class Dog():
    def eat(self):
        print("bone")

    def drink(self):
        print("pear")

class XTQ(Dog):

    def  eat(self):
        print("peak")

xiaotq = XTQ()
xiaotq.drink()
xiaotq.eat()