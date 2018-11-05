n = int(input())

maximum = n
count = 1

while n != 0:
    if n > maximum:
        maximum = n
        count = 1

    n = int(input())

    if n == maximum:
        count += 1

print(count)
