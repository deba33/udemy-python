my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)
print(my_dict["key1"])

d = {"k1": 123, "k2": [1, 2, 3], "k3": {"k3a": 89}}
print(d["k3"]["k3a"])
print(d["k2"][1])

d["k4"] = 67
print(d)

d["k1"] = 321
print(d)

print(d.keys())
print(d.values())
print(d.items())
