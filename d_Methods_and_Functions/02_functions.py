def say_hello(name="Deba"):
    return "Hello "+name


print(say_hello("exf"))
print(say_hello())


def add(a, b):
    return a+b


result = add(3, 5)

print(result)


def dog_check(mystring):
    return "dog" in mystring.lower()


print(dog_check("dog ran away"))
print(dog_check("Dog ran away"))
print(dog_check("cat ran away"))

# PIG LATIN


def pig_latin(word):
    '''
    PIG LATIN
    > If word starts with a vowel add "ay" to end.
    > If word does not start with a vowel, put first letter at the end, then add "ay"
    EX:
        word > ordway
        apple > appleay
    '''
    first_letter = word[0]

    # check if vowel

    if first_letter in "aeiou":
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"

    return pig_word


print(pig_latin("apple"))
print(pig_latin("Deba"))
