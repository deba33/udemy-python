try:
    result = 10 + 10
except:
    print("Hey it looks like you are not adding correctly!")
else:
    print("Add went well")
    print(result)

try:
    f=open("testfile","r")
    f.write("Write a test line")
except TypeError:
    print("There was a Name error")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")
