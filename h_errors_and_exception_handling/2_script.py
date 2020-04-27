# try:
# except:
# finally:
try:
    f = open("testfile.txt", "r")
    f.write("Write a test line")
except TypeError:
    print("there was a type error")
except OSError:
    print("there was a OS error")
except:
    print("Other error")
finally:
    print("I always run")
