# 位运算
# 0b 二进制
# 0o 八进制
# 0x 十六进制
a = 0b0111100
b = 0b0001101
print(a, b)  # 60 13
print(a << 2)  # 240 左移2位
print(a >> 3)  # 7 右移2位


# 成员运算符
def judgeValueInList(value):
    if value in list:
        print("{} is in list!".format(value))
    else:
        print("{} isn't in list!".format(value))


a = 10
b = 1
list = {1, 2, 3, 4, 5}

judgeValueInList(a)
judgeValueInList(b)
