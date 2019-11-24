myfile = open("0.txt")
var = myfile.read()
print(var)
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines(0))
myfile.close()

with open('0.txt') as fileio:
    contents = fileio.read()

print(contents)

with open('00.txt', mode='a') as dfile:
    dfile.write('End Line')

with open('00.txt', mode='r') as dfile:
    print(dfile.read())
