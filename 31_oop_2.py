class Dog():
    # class obj attr
    # sme fr any instance of a cls

    species = "mammal"

    def __init__(self, breed, name):
        # Attributes
        # We take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions ---->Methods

    def bark(self, num):
        return ("WOOF ! My name is {} and the number is {}".format(self.name, num))


my_dog = Dog("Lab", "Tom")

print(my_dog.breed, my_dog.name, my_dog.species+"\n" + my_dog.bark(5))
