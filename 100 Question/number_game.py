# usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""

计算机想到一个 1 到 20 之间的随机数，让你来猜它是几。计算机会告诉你每次猜的数太大还是太小。如果能够在 6 次之内猜到正确的数字，就赢得游戏。

"""

# 导入随机函数的包
import random

# 设置猜的次数初始值为0,创建了一个名为 guessesTaken 的新变量。我们将把玩家猜过的次数保存到这个变量中。因为此时玩家还没有做过任何猜测，所以这里保存的是整数 0
guessesTaken = 0

# 提示：要求用户输入姓名，并且将输入存储到 myName 变量中（记住，这个字符串可能并不是玩家的真实姓名。它可能只是玩家输入的任意字符串。计算机则只会无条件地执行指令）
print("Hello! What is your name?")
MyName = input()

# 调用随机函数的功能，电脑随机出一个数：randon.randint(a,b),(a,b)为区间，可取到a,b的值
# 调用了一个名为 randint()的新函数，并且把返回值存储到了变量 number 中
number = random.randint(1, 20)

# 提示电脑将会在1到20出一个数
print('Well, ' + MyName + ', I am thinking of a number between 1 and 20.')

# 猜的次数总共为6次
while guessesTaken < 6:

    print('Take a guess.') # There are four spaces in front of print.
    guess = int(input())  #输入你猜的数
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in frontof print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + MyName + '! You guessed my number in ' +
              guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The numMber I was thinking of was ' + number)