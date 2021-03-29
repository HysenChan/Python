class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        var = self.a
        self.a += 1
        return var


myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))