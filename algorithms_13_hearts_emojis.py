import unicodedata

for i in range(230000):
    char = chr(i)
    charName = unicodedata.name(char, "")
    if "HEART" in charName:
        print(char, end="")    