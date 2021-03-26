# 身份运算符
# is 用于判断两个变量引用对象是否为同一个
# == 用于判断引用变量的值是否相等
a = 20
b = 30
if a is b:
    print("a and b is same!")
else:
    print("a and b isn't same!")

if id(a) == id(b):
    print('a and b have same identification!')
else:
    print('a and b not have same identification!')

list1 = [1, 2, 3]
list2 = list1
print(list2 is list1)  # True
print(list2 == list1)  # True
list2 = list1[:]
print('list1:{},list2:{}'.format(list1, list2))
print(list2 is list1)  # False
print(list2 == list1)  # True
