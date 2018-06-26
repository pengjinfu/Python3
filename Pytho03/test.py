#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.9


# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         sum = j*i
#         print("%d*%d=%2d"%(j,i,sum),end="\t")
#         j += 1
#     print("")
#     i += 1


# i = 0
# while i <= 99:
#  i += 1
#  if i % 7 == 0 or i % 10 == 7 or i//10 == 7:
#      continue
#  else:
#      print(i)
i = 0
while i <= 99:
 i += 1
 if i % 7 == 0 or i % 10 == 7 or i//10 == 7:
     continue
 else:
     print(i)
i=1
while i <= 9:
    if i<=5:
        print(' '*(5-i),'*'*(2*i-1))
    else:
        print(' '*(i-5), '*'*(2*(10-i)-1))
    i+=1