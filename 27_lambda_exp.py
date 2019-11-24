# map function
def square(num):
    return num**2


my_nums = [1, 2, 3, 4]

for item in map(square, my_nums):
    print(item)

my_nums_list = list(map(square, my_nums))
print(my_nums_list)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


names = ['andy', 'Eve', 'Sally']
print(list(map(splicer, names)))


# filter function
def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, my_nums)))


# lambda function
# square = lambda num: num ** 2
def square(num): return num ** 2


print(square(5))
# or
print(list(map(lambda num: num**2, my_nums)))

print(list(filter(lambda num: num % 2 == 0, my_nums)))

print(list(map(lambda x: x[0], names)))

print(list(map(lambda x: x[::-1], names)))
