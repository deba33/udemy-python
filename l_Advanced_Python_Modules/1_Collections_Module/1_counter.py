# Counter

from collections import Counter

l = [1, 1, 2, 1, 2, 3, 4, 4, 4, 3, 3, 4, 5, 5, 5]

print(Counter(l))

s = "asasasasasassasasasafdfdfdrdfrdfrdf"

print(Counter(s))

r_st = "Nory was a Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been."

words = r_st.split()
print(Counter(words))

# print(Counter(r_st.split()))

c = Counter(words)

print(c.most_common(3))

print(sum(c.values()))
