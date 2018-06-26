#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.1

# print('\n'.join([''.join([(u'ILoveChina爱'[(x-y)%11]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
#
# print('\n'.join([''.join([('ILoveChinaHelloWordHelloChina'[(x-y)%29]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


# students = [
# {"name": "阿⼟",
# "age": 20,
# "gender": True,
# "height": 1.7,
# "weight": 75.0},
# {"name": "⼩美",
# "age": 19,
# "gender": False,
# "height": 1.6,
# "weight": 45.0},
# ]
# find_name = "阿⼟"
# for stu_dict in students:
#     print(stu_dict)
# # 判断当前遍历的字典中姓名是否为find_name
#     if stu_dict["name"] == find_name:
#         print("找到了")
# # 如果已经找到，直接退出循环，就不需要再对后续的数据进⾏⽐较
#         break
#     else:
#         print("没有找到")
# print("循环结束")



# L = [
# ['Apple', 'Google', 'Microsoft'],
# ['Java', 'Python', 'Ruby', 'PHP'],
# ['Adam', 'Bart', 'Lisa']
# ]
#
# t = ('a', 'b', ['A', 'B'])



def money(apple,weight):
    if apple == 1:
        price = 10
    elif apple == 2:
        price = 8
    else:
        price = 12
    return price * weight

a = 2
w = 10
print("apple=",a,"weight=",w,"money=",money(a,w))

