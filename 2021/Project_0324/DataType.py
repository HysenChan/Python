counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "DataType"  # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值--相同的值
a = b = c = 1
print('a,b,c:', a, b, c)
# 多个变量赋值--不同的值
x, y, z = 1, 2.0, "DataType"
print('x,y,z:', x, y, z)

b = True
print(type(x), type(y), type(z), type(b))


# type主要用于获取未知变量的类型
# isinstance主要用于判断A类是否继承于B类
class A:
    pass


class B(A):
    pass


print(type(A), type(B), type(A()), type(B()), A, B)  # type type __main__.A __main__.B __main__.A __main__.B
print(type(type(A())), type(A))  # type type
print(type(A()) == A)  # True
print(type(B()) == A)  # False
print(isinstance(A(), A))  # True
print(isinstance(A(), B))  # False
print(isinstance(B(), A))  # True
