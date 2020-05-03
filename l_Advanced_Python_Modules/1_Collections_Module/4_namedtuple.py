# can be able to create new object type
from collections import namedtuple

Dog = namedtuple("Dog", "age breed name")

sam = Dog(age=2, breed="Lab", name="sammy")

print(sam)

print(sam.age)
