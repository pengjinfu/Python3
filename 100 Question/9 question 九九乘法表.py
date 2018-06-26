# usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

# 方法一：
i = 1
while i <= 9:
    j= 1
    while j <= i:
        sum = i * j
        print("%d*%d=%2d\t"%(i,j,sum),end="  ")
        j += 1
    print("  ")
    i += 1


# 方法二
for line in range(1,10):
    for row in range(1,line+1):
        Sum = row * line
        print("%d*%d=%2d\t" % (row, line, Sum), end="  ")
        row += 1
    print("  ")
    line += 1



