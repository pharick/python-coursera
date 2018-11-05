n = int(input())

if n == 1:
    print(0)
else:
    power = 2
    k = 1

    while power < n:
        power *= 2
        k += 1

    print(k)
