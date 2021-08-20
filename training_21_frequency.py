f = open("words.txt", "r")

NEW = []
for n in f.read():
    if n.islower():
        NEW.append(n)

letters = {}

for i in NEW:  
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1
    #print(i)
print(letters)

for char in letters:
    print(f"{char}: {format(letters[char] / len(NEW), '.2f')}")

f.close()