my_list_a = [1, 2, 3]
my_list_b = ["string", 900, 89.80]

print(my_list_a[1])

print(my_list_a + my_list_b)

my_list_b[0] = "STRING"

'''
variable = ["Data","String"]
variable[0] = 50   ✔

Because, Lists in Python are not immutable
'''

print(my_list_b)

# .append and .pop

my_list_b.append("six")
print(my_list_b)

# my_list_b.pop()

popped_item = my_list_b.pop()

print(popped_item)
print(my_list_b)

# .sort() and .reverse()

new_list = ["a", "e", "x", "b", "c"]
num_list = [1, 5, 4, 8, 2]

new_list.sort()
num_list.sort()

print(new_list)
print(num_list)

new_list.reverse()
num_list.reverse()

print(new_list)
print(num_list)
