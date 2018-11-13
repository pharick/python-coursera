string = input()

o1 = string.find("h")
o2 = len(string) - string[::-1].find("h") - 1

print(string[:o1], end="")
print(string[o2 + 1:])
