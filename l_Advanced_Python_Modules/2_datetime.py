import datetime

# time
t = datetime.time(5, 25, 1)

print(t)

print(t.hour)

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

# Date

today = datetime.date.today()

print(today)
print(today.month)

print(datetime.date.min)

d1 = datetime.date(2015, 3, 11)

print(d1)

d2 = d1.replace(year=1990)

print(d2)

print(d1-d2)
