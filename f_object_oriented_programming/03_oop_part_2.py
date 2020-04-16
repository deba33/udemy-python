class Dog():

    # class object attribute
    # Same for any instance of a class
    species = "mammal"

    def __init__(self, breed, name):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # Operations/Actions ---> Methods
    def bark(self, number):
        return "WOOF ! My name is {} and the number is {}".format(self.name, number)


my_dog = Dog("Lab", "Sammy")

print(type(my_dog))
print(my_dog.breed, my_dog.name, my_dog.species)
print(my_dog.bark(5))
