mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print("Hello")

print("-----Even Numbers-----")

for num in mylist:
    if num % 2 == 0:
        print(num)

print("-----Odd Numbers-----")

for num in mylist:
    if num % 2 != 0:
        print(num)

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print("---Total SUM----")
print(list_sum)

mystring="Hello World"

for letter in mystring:
    print(letter)

mylist = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in mylist:
    print(a)

d = {"k1":1,"k2":2,"k3":3}

for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(value)