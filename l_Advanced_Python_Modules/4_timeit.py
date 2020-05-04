import timeit

# print("0-1-2-3-............-99")

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=100))

print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=100))

print(timeit.timeit('"-".join(map(str,range(100)))', number=100))
