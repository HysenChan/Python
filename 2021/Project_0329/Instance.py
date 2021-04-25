# 传不可变对象实例
def change(para):
    print(id(para))
    para = 10
    print(id(para))


a = 1
print(id(a))
change(a)


# 传可变对象实例
def changeMe(myList):
    myList.append([1, 2, 3, 4])
    print("函数内取值：", myList)
    return


list = [10, 20, 30]
changeMe(list)
print("函数外取值：", list)
