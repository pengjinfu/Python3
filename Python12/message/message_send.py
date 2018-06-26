#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22

message_send = 20

# 使用递归的方法打印出前n个斐波那契数列
def fibo(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 加上此判断后，如果此文件是主动执行就走if里面的代码，如果是被当成模块导入后的被动执行就不走if里面的代码
if __name__ == '__main__':
    print(__name__)  # __main__表示当前.py是主动 当文件如果被执行name中会 模块名
    fibo(20)
