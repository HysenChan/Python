import random

randStr = random.choice(['apple', 'pear', 'bannana'])
print(randStr)

randTenNum = random.sample(range(100),10)
print(randTenNum)

print(random.random())

print(random.randrange(6))