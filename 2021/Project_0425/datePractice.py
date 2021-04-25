import datetime

print(datetime.date.today())

now = datetime.date.today()
birthday = datetime.date(2000, 1, 1)

age = now - birthday
print(age)
