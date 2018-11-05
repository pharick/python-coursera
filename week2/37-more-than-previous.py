p = int(input())
n = int(input())
count = 0

while n != 0:
    if n > p:
        count += 1
    p = n
    n = int(input())

print(count)
