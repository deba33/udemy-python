class Dog():

    def __init__(self, breed, name, spots):
        """ Attributes
        We take in the argument
        Assign it using self.attribute_name """
        self.breed = breed
        self.name = name

        # expect boolean True/False
        self.spots = spots


my_dog = Dog(breed="Lab", name="Sammy", spots=False)

print(type(my_dog))
print(my_dog.breed, my_dog.name, my_dog.spots)
