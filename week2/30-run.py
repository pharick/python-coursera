x = int(input())
y = int(input())

d = 1
while x < y:
    x += x * 0.1
    d += 1

print(d)
