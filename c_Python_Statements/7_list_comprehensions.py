mystring = "hello"
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)


mylist_ = [letter for letter in mystring]
print(mylist_)

mylist_ = [letter for letter in "mystring"]
print(mylist_)

mylist = [num for num in range(5, 64, 6)]
print(mylist)

mylist = [num**2 for num in range(5, 64, 6)]
print(mylist)

mylist = [x for x in range(0, 15) if x % 2 == 0]
print(mylist)


celcius = [0, 10, 8, 25, 90.8]
fahrenheit = [((9/5)*temp+32) for temp in celcius]

print(fahrenheit)


mylist = []

for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x*y)

print(mylist)


mylist = [x*y for x in [2, 4, 6] for y in [100, 200, 300]]
print(mylist)
