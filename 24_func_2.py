def dog_check(mystring):
    if "dog" in mystring.lower():
        return True
    else:
        return False


print(dog_check("My dog barks"))
print(dog_check("Dog ran away"))
print(dog_check("cat run away"))


def pro_dog_check(mystring):
    return "dog" in mystring.lower()


print(pro_dog_check("My dog barks"))
print(pro_dog_check("Dog ran away"))
print(pro_dog_check("my cat is black"))
