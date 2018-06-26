#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.22



# __all__ = []  # 当外面用from  模块名 import * 的方式导入此模块时，可以用此变量来控制导入的具体东西
__all__ = ["fibo"]
# 使用递归的方法打印出前n个斐波那契数列
def fibo(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

if __name__ == '__main__':
    fibo(5)
