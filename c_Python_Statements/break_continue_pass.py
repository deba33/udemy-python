# Pass

x = [1, 2, 3]

for item in x:
    pass

# continue

mystring = "Sammy"

for letter in mystring:
    if letter == "a":
        continue
    print(letter)

# Break

mystring = "Sammy"

for letter in mystring:
    if letter == "a":
        break
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
