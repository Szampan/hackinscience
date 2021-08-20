import os

print(os.getcwd())
print(os.listdir())

fil = open("./words.txt", "r")
print(fil.read())