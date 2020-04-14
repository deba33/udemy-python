def square(num):
    return num**2

# or using lambda expressions


lambda num: num ** 2

# lambda with map function

mynums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num: num**2, mynums)))

# lambda with filter function

print(list(filter(lambda num: num % 2 == 0, mynums)))
