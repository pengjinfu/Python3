#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.10

list1 = ["zhangsan","lisi","list","ww"]

"""list.append(元素)：增加元素到末尾"""
list1.append("who are you")
print(list1)


"""list.insert(索引，元素）：在指定位置增加元素"""
list1.insert(1,"ml")
print(list1)

list2 = ["123","20"]
"""list.extend(新的列表):读取新列表的元素，并依次加入原列表的末尾"""
list1.extend(list2)
print(list1)

"""list.remove(元素）：删除元素"""
list1.remove("ml")
print(list1)


"""name = list[索引]：查询元素"""
name = list1[2]
print(name)

"""list[索引] = 值：修改元素"""
list1[2] = 123
print(list1)

"""list.index(元素,位置）：当位置不填时，默认从0查找第一个"""
list1.index(123)
print(list1)