def myfunc(a, b):
    '''Returns 5% of the sum a and b'''
    return sum((a, b))*(5/100)


print(myfunc(40, 60))


# *args

def args_myfunc(*args):
    return sum(args)*(5/100)


print(args_myfunc(1.5, 90, 30))
print(args_myfunc(1.5, 90, 30, 8, 34))


# **kwargs

def kwargs_myfunc(**kwargs):
    if "fruit" in kwargs:
        return "My fruit of choice is {}".format(kwargs["fruit"])
    else:
        return "I did not find any fruit here"


print(kwargs_myfunc(fruit="apple", veggie="lettuce"))


# both *args and **kwargs

def both_myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    return "I would like {} {}.".format(args[0], kwargs["food"])


print(both_myfunc(10, 20, 30, fruit="orange", food="eggs", animal="dog"))
