
"""
需求
1. 定义字符串变量  name  ，输出 我的名字叫 ⼩明，请多多关照！
2. 定义整数变量  student_no  ，输出 我的学号是 000001
3. 定义⼩数  price  、 weight  、 money  ，输出 苹果单价 9.00 元／⽄，购买了 5.00
⽄，需要⽀付 45.00 元
4. 定义⼀个⼩数  scale  ，输出 数据⽐例是 10.00%
"""

name = "小米"
print("我的名字叫 %s，请多多关照！" % name)
print("你的大名是：%s" % name)

student_no = 1
print("我的学号是 %06d" % student_no)

price = 9.0
weight = 5.0
money = price * weight
print("苹果单价 %.02f 元／⽄，购买 %.02f ⽄，需要⽀付 %.02f 元" % (price, weight, money))
print("单价：%.2f,重量：%.2f,金额：%.2f" % (price,weight,money))

scale = 0.1
print("数据⽐例是 %.02f%%" % (scale * 100))

dog = 0.25
print("这只狗是%.2f%%" % (dog * 100))