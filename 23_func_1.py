
def name_function():
    '''
    DOCSTRING:  Info about function
    Input:      No Input
    Output:     Hello      
    '''
    print("Hello")


name_function()
print(help(name_function))


def say_hello(name='NAME'):
    return ("Hello " + name)


result = say_hello("ZACH")
print(result)
