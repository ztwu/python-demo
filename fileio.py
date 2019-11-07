import os

#os.mkdir("test_dir")

fo = open("test.txt")
print(fo.name)



a = fo.read(2)
print(a)

fo.close()

fo = open("test.txt")

b = fo.readline()
print(b)

c = os.path.exists("test_dir")
print(c)