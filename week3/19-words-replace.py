string = input()

space = string.find(" ")

print(string[space+1:], string[:space])
