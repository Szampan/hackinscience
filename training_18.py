f = open("words.txt", "r")
num = 0

for i in f.read():
    if i == "e":
        num += 1
print(num)