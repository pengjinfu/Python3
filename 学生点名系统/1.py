#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

def get_prime(n):
    ret = []
    if n<1:
        pass
    else:
        ret.append(2)
        for i in range(3,n):
            isPrime = True
            for j in range(2,i):
                if i%j==0:
                    isPrime = False
                    break
            if isPrime:
                ret.append(i)
    return ret


print(get_prime(10))
