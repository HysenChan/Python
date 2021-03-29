class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 3:
            var = self.a
            self.a += 1
            return var
        else:
            raise StopIteration


myClass = MyNumbers()
myIter = iter(myClass)
for x in myIter:
    print(x)
