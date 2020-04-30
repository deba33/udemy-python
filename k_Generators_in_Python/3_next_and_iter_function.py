def simple_gen():

    for x in range(3):
        yield x

for num in simple_gen():
    print(num)

g = simple_gen()

next(g)

next(g)

next(g)

# next(g)

s = "hello"

for letter in s:
    print(letter)

s_iter = iter(s)

next(s_iter)

next(s_iter)

next(s_iter)