# Strings are immutable

name = "Sam"

'''
name[0] = "R"   ❌

You can't do this because Strings in Python does not support item assignment.
'''

last_letters = name[1:]
new_name = "R" + last_letters

print(new_name)

x = "Hello World"

print(x.upper())

''' 
other methods are 
.lower()
.split()
etc.
'''
