file = open("lorum.txt", "r+")
file.write("Test\n")
print(file.read(5))
print(file.seek(0))
print(file.read(5))
#print(file.seek(0))
file.write("Test\n")
print()
file.close()


with open("lorum.txt", "a+") as f:
    f.write("qwerty")