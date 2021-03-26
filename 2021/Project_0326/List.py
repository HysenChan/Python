list = ['A', 'B', 'C', 'D']

list.append('Z')
list.reverse()
del list[2]
print(list)
list1 = list.copy()
print('list:{},list1:{}'.format(list, list1))
print(list == list1)  # True 值是相等的
print(list is list1)  # False 引用的对象不同
print(id(list) == id(list1))  # False
