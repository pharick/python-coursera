size = int(input())
shoes = list(map(int, input().split()))

shoes.sort()

n = 0
lastShoeIndex = 0
while lastShoeIndex < len(shoes):
    if shoes[lastShoeIndex] >= size:
        n += 1
        break
    lastShoeIndex += 1

i = lastShoeIndex + 1
while i < len(shoes):
    if (shoes[i] - shoes[lastShoeIndex] >= 3):
        n += 1
        lastShoeIndex = i
    i += 1

print(n)
