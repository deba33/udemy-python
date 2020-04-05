# range

for num in range(10):
    print(num)

for num in range(0, 11, 2):
    print(num)

mylist = list(range(0, 22, 3))
print(mylist)

# enumerate

index_count = 0

for letter in "abcde":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

index_count = 0
word = "debabrata"

for letter in word:
    print(word[index_count])
    index_count += 1

word = "something"

for item in enumerate(word):
    print(item)

# zip

mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]

for item in zip(mylist1, mylist2):
    print(item)

# in

print(2 in mylist1)
