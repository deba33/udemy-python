# strings are immutable

name = "sam"
print(name)
# name[0] = p | this is wrong

last_letters = name[1:]
print(last_letters)

name = "P" + last_letters
print(name)

print("2" + "3")

x = "Hello World"
y = x.upper()
print(y)
y = x.lower()
print(y)
y = x.split()
print(y)
y = x.split("l")
print(y)
