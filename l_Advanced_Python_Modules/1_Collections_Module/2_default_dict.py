from collections import defaultdict

d = defaultdict(object)

d["one"]

for item in d:
    print(item)

new_dict = defaultdict(lambda: 0)

new_dict["one"]
new_dict["two"] = 2

print(new_dict)
