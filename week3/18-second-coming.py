string = input()

o1 = string.find("f")
o2 = string.find("f", o1 + 1)

if o1 == -1:
    print(-2)
else:
    print(o2)
