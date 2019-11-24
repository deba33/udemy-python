from random import shuffle, randint

mylist = [1, 2, 3]

for num in range(10):
    print(num)

for num in range(2, 11):
    print(num)

for num in range(2, 20, 3):
    print(num)

print(list(range(2, 20, 3)))

index_count = 0

for letter in "abcde":
    print("at index {} the letter is {}".format(index_count, letter))
    index_count += 1

var = "Debabrata"

for index, letter in enumerate(var):
    print(index)
    print(letter)
    print("\n")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list2):
    print(item)

list3 = list(zip(list1, list2))

print(list3)

print("x" in [1, 2, 3])

print(min(list1))
print(max(list1))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]

shuffle(mylist)

print(mylist)

print(randint(0, 5000))

x = int(input("Enter a number: "))
print(type(x))
