age = int(input("请输入狗的年龄："))
print("")
if age <= 0:
    print("无效年龄!")
elif age == 1:
    print("相当于14岁的人!")
elif age == 2:
    print("相当于22岁的人!")
else:
    human = 22 + (age - 2) * 5
    print("相当于{}岁的人!".format(human))

input("点击enter退出!")
