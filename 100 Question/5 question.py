# usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

"""
题目5：输入三个整数x,y,z，请把这三个数由小到大输出。

1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

------------------------------
1.输入三个整数：i，j，k
2.把i默认为最小数
3.若i<j,则最大数为就j，j<k，则k为最大数.....

"""

# 定义一个空列表，用于存储三个3位数

Num = []

# 用迭代输出3个3位数
for i in range(3):
    x = int(input("Please input you number:\n"))

    Num.append(x)  # 把每一个输入的数插入到列表里最后位置

"""

list.sort ()
对列表中的元素就地进行排序。

"""

Num.sort()
print(Num)