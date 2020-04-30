def gen_fibon(n):

    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


for num in gen_fibon(10):
    print(num)