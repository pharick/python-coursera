string = input()

o1 = string.find("h")
o2 = len(string) - string[::-1].find("h") - 1

print(string[:o1+1], end="")
print(string[o1+1:o2].replace("h", "H"), end="")
print(string[o2:])
