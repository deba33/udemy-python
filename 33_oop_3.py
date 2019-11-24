# inheritance


class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        return ("I am an Animal")

    def eat(self):
        return ("I am eating")


anm = Animal()

print(anm.eat()+"  "+anm.who_am_i())


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        return ("I am a Dog")

    def bark(self):
        return ("WOOF")


dog = Dog()

print(dog.eat()+"  "+dog.who_am_i())

# polymorphism


class Dog2():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+" Says woof !"


class Cat2():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+" Says meow !"


niko = Dog2("niko")
felix = Cat2("felix")

print(niko.speak()+"\n"+felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    return pet.speak()


print(pet_speak(niko)+"\n"+pet_speak(felix))


class Animal3():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Sub class must implement this abstract method")


class Dog3(Animal3):
    def speak(self):
        return self.name+" Says woof !"


class Cat3(Animal3):
    def speak(self):
        return self.name+" Says meow !"


fido = Dog3('fido')
isis = Cat3('Isis')

print(fido.speak()+"\n"+isis.speak())
