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

# 基本运算
print(1 + 1)  # 2
print(2.5 - 2)  # 0.5
print(3 * 2)  # 6
print(3 / 2)  # 1.5 浮点数
print(3 // 2)  # 1  整数
print(3 % 2)  # 1
print(2 ** 3)  # 8  乘方

# 字符串
string = 'HelloWorld'
print(string)  # HelloWorld
print(string[0:-1])  # HelloWorl
print(string[0])  # H
print(string[2:5])  # llo
print(string[0:])  # HelloWorld
print(string * 2)  # HelloWorldHelloWorld
print(string + "Test")  # HelloWorldTest
print(len(string))  # 10

List = ['a', 'b', 'c', 'd', 'e']
print(List[0:])

ListMixture1 = ['abc', 123, 3.14, 'hello', 3 * 2]
ListMixture2 = ['xzy', 456, "JQK"]
print(ListMixture2 * 2)
print(ListMixture1 + ListMixture2)
ListMixture = ListMixture1 + ListMixture2
print(ListMixture[1:3:-1])

ListMixture2[0:] = [1, 2, 3]
print(ListMixture2)
ListMixture2[0:] = []
print(ListMixture2)


# 翻转字符串
def reverseWord(input):
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    inputStr = 'A B C D E F G'
    rw = reverseWord(inputStr)
    print(rw)  # G F E D C B A
