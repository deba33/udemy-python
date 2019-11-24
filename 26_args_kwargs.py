# args & kwargs function


# normal Function
def sum_myfunc(a, b):
    return sum((a, b)) * 0.05


print(sum_myfunc(5, 9))


def adv_myfunc(a, b, c=0, d=0, e=0):
    return sum((a, b, c, d, e)) * 0.05


print(adv_myfunc(3, 8, 90))


# *args
def arg_myfunc(*args):
    return sum(args) * 0.05


print(arg_myfunc(56, 44))


# **kwargs
def kwargs_myfunc(**kwargs):
    if "fruit" in kwargs:
        return ("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        return kwargs


print(kwargs_myfunc(fruit="APPLE", veg="xyz"))


#args and kwargs

def both_func(*args, **kwargs):
    return ("I would like {} {}.".format(args[0], kwargs["food"]))


var = both_func(1, 2, 3, food="Rice", fruit="apple")
print(var)
