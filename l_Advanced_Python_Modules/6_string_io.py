from io import StringIO

message = "This is just a normal string."

f = StringIO(message)
print(f.read()+"\n")

f.write("\nSecond line in the normal string")

f.seek(0)

print(f.read())
