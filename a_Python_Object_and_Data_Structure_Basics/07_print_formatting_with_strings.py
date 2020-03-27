
# .format() method

print("This is a string {}".format("INSERTED"))

print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))

f = "fox"
b = "brown"
q = "quick"

print("The {} {} {}".format(q, b, f))

print("The {qu} {br} {fx}".format(qu="quick", br="brown", fx="fox"))

# float formatting
# "{value:width.precision f}"

result = 100/777

print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))

# "f" string method

name = "Jose"
age = 34

print(f"Hello, his name is {name}")
print(f"{name} is {age} years old.")
