# LEGB rule
# L local
# E Enclosing functions
# G Global(module)
# B built in

# local
lambda num: num**2

# Enclosing
name = "This is a global string"


def greet():
    name = "sammy"

    def hello():
        print("Hello "+name)

    hello()


greet() 
