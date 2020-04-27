# try:
# except:
# else:


def add(n1, n2):
    sum = n1 + n2
    return sum


number1 = 10
number2 = 10

try:
    result = add(number1, number2)
except:
    print("Error in your code, RECHECK")
else:
    print(f"{number1} + {number2} = {result}")
