# Inheritance


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        return "I am an animal"

    def eat(self):
        return "I am eating"


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # def who_am_i(self):
    #     return "I am a Dog"

    def bark(self):
        return "WOOF!"


myanimal = Animal()
mydog = Dog()

print(mydog.who_am_i(), mydog.eat(), mydog.bark())


# Polymorphism

class P_dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF !"


class P_cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow !"


niko = P_dog("niko")
felix = P_cat("felix")

print(niko.speak(), felix.speak())

for pet in [niko, felix]:

    print(type(pet))
    print(type(pet.speak()))
