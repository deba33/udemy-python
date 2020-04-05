mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print("jelly")

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")

list_sum = 0

for num in mylist:
    list_sum = list_sum+num

print(list_sum)

mystring = "Hello World"

for letter in mystring:
    print(letter)

# tuple unpacking

mylist_ = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in mylist_:
    print(a)
    print(b)

d = {"k1": 1, "k2": 2, "k3": 3}

for (key, value) in d.items():
    print(value)
