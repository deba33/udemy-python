# add() method
s = set()

s.add(1)
s.add(2)

print(s)

# clear() method
s.clear()

s = {1, 2, 3}

# copy() method
sc = s.copy()
print(sc)

s.add(4)
print(s)

# difference() and difference_update() method
print(s.difference(sc))

s1 = {1, 2, 3}
s2 = {1, 4, 5}

s1.difference_update(s2)

print(s1)
print(s2)

# discard(method)
s = {1, 2, 3, 4}

s.discard(2)
s.discard(7)

print(s)

# intersection() and intersection_update() method
s1 = {1, 2, 3}
s2 = {1, 2, 4}

print(s1.intersection(s2))

print(s1, s2)

s1.intersection_update(s2)

print(s1, s2)

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

# isdisjoint() method
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# issubset() method
print(s1.issubset(s2))
print(s2.issuperset(s1))

# symmetric_difference() method
print(s1.symmetric_difference(s2))

# union() method
print(s1.union(s2))
