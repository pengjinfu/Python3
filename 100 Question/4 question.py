# usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

'''

题目4：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：
1.输入年、月、日：Year、Month、Day
2.定义一个人元组：且逐次计算天数之和
3.若输入的月在：1-12，则最后总天数=元组[下标所对应的数]
4.判断输入的年（闰年&非闰年）：闰年则总天数+1，非闰年则不加


'''

Year = int(input("Please input you want know year:\n"))
Month = int(input("Please input you want know Month:\n"))
Day = int(input("Please input you want know Day:\n"))

DayNum = (0,31,59,90,121,151,181,213,243,273,303,335)
for i in range(5):
    if 0 <= Month <= 12:
        sum = DayNum[Month - 1]
    else:
        print("date error,try again")
        break
# 如何在这设置一个断点，若Month>12，则退出
sum += Day

leap = 0
if (Year % 400 == 0) or (Year % 4 == 0) and (Year % 100 != 0):
    leap = 1
if (leap == 1) and (Month == 2):
    sum += 1
print ('It is the %dth day.' % sum)