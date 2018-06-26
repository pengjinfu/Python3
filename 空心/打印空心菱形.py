# 打印空心菱形
# for i in range(1, 20):
#     if i == 9:
#         print("*", end="")
#     elif i == 11:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 8:
#         print("*", end="")
#     elif i == 12:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 7:
#         print("*", end="")
#     elif i == 13:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 6:
#         print("*", end="")
#     elif i == 14:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
#
# for i in range(1, 20):
#     if i == 5:
#         print("*", end="")
#     elif i == 15:
#         print("*")
#         break
#     else:
#         print(" ", end="")
#
# for i in range(1, 20):
#     if i == 4:
#         print("*", end="")
#     elif i == 16:
#         print("*")
#         break
#     else:
#         print(" ", end="")

# 分四个部分
# 第一部分
# 这里要找到中间的位置，只需要打印一个*就好
for i in range(1, 20):
    if i == 10:
        print("*")
        break
    else:
        print(" ", end="")

# 第二部分
#         * *
#        *   *
#       *     *
#      *       *
#     *         *
#    *           *
# 和打印三角形是一样的
for j in range(9, 1, -1):
    for i in range(1, 20):
        if i == j:
            print("*", end="")
        elif i == 20 - j:
            print("*")
            break
        else:
            print(" ", end="")

# 第三部分
#     *         *
#      *       *
#       *     *
#        *   *
#         * *
for j in range(2, 11):
    for i in range(1, 20):
        if i == j:
            print("*", end="")
        elif i == 20 - j:
            print("*")
            break
        else:
            print(" ", end="")
