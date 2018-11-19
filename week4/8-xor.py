def xor(x, y):
    return (x or y) and x != y


x = bool(int(input()))
y = bool(int(input()))

print(int(xor(x, y)))
