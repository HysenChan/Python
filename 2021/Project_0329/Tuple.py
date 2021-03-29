# 元组和列表的区别在于元组的元素不能修改
# 元组使用小括号()
# 列表使用方括号[]
tuple1 = (50)  # == tuple1=50
print(type(tuple1))  # int
tuple2 = (10,)
print(type(tuple2))  # tuple

tuple3 = ['A', 'C', 'B', 'D', 'Z', 'X', 'E']
print(max(tuple3))
print(min(tuple3))
