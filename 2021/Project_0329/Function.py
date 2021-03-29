# 斐波那契数列
a, b = 0, 1
while b < 10:
    print(b, end=',')
    # 等价 a, b = b, a + b
    n = b
    m = a + b
    a = n
    b = m
