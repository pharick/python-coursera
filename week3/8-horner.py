from math import floor

n = int(input())
x = float(input())

if n == 0:
    print(float(input()))
else:
    result = float(input()) * x + float(input())
    n -= 1

    while n:
        n -= 1
        result = result * x + float(input())

    print(result)
