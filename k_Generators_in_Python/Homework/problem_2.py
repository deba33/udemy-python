# Create a generator that yields "n" random numbers between a low and high number(that are inputs).
# Use the random library.

import random as rnd


def rand_num(low, high, n):
    for i in range(n):
        yield rnd.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)
