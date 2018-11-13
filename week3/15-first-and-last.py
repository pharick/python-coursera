string = input()

o1 = string.find("f")
o2 = string[::-1].find("f")

if o2 != -1:
    o2 = len(string) - o2 - 1
    if o2 == o1:
        print(o1)
    else:
        print(o1, o2)
