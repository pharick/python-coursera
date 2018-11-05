n = int(input())

max_1 = max_2 = 0

while n != 0:
    if n >= max_1:
        max_2 = max_1
        max_1 = n
    elif n > max_2:
        max_2 = n

    n = int(input())

print(max_2)
