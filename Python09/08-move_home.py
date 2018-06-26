

"""
class JiaJu:
self.type
self.area
__init__
__str__

class Home:
self.address
self.area
self.free_area
__init__
__str__

free.area =home.area -jiaju.area

"""


class Funiture:
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return "%s家具，占用面积是%d" % (self.type, self.area)


class Home:
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.item = []

    def __str__(self):
        return "房⼦在:%s, ⾯积为%d, 剩余⾯积为%d" % (self.address, self.area, self.free_area)

    def add_funiture(self,funiture):
        if self.free_area >= funiture.area:
            print("%s添加成功" % funiture.type)
            self.free_area -= funiture.area
        else:
            print("%s家具添加失败" % funiture.type)


bed = Funiture("双⼈床", 4)
print(bed)
# 创建房⼦
fangzi1 = Home("北京盘古⼤观", 200)
print(fangzi1)
# 添加家具
fangzi1.add_funiture(bed)
print(fangzi1)
# 再添加⼀个家具
bed2 = Funiture("冰箱", 1)
print(bed2)
fangzi1.add_funiture(bed2)
print(fangzi1)
bed3 = Funiture("篮球场", 420)
print(bed3)
fangzi1.add_funiture(bed3)
print(fangzi1)

