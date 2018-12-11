a = int(input())
b = int(input())

for i in range(a, b + 1):
    n = i
    d1 = n % 10
    n //= 10
    d2 = n % 10
    n //= 10
    d3 = n % 10
    n //= 10
    d4 = n % 10

    if d1 == d4 and d2 == d3:
        print(i)
