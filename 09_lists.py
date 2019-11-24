my_list = [1, 2, 3]
my_list = ["deba", 100, "samal", 20]
x = my_list[0]
# same as string indexing
another_list = [3, 6, 78]

new_list = my_list + another_list
print(new_list)

new_list[0] = "ONE"
print(new_list)

new_list.append("Six")
print(new_list)

poped_item = new_list.pop()
print(poped_item)
print(new_list)

poped_item = new_list.pop(0)
print(poped_item)
print(new_list)

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]

new_list.sort()
print(new_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)
