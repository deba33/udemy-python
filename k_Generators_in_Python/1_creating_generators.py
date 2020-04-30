def create_cubes(n):

    for x in range(n):
        yield x**3


print(create_cubes(10))

print(list(create_cubes(10)))

for x in create_cubes(10):
    print(x)
