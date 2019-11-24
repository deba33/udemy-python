print("This is a string {}".format("INSERTED"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# float formatting

result = 100 / 777
print("The result was {r:1.3f}".format(r=result))

name = "deba"
# print(f"hello, his name is {name}") | not wrong in python3
