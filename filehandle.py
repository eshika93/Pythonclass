#w, a, r

f = open("test.txt", "w")
f.write("Hello, I am python. \n")
f.close()

f = open("test.txt", "a")
f.write("Hello, I am python. ")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()

f = open("test.txt", "r")
print(f.readline())
f.close()

f = open("test.txt", "r")
print(f.readlines())
f.close()