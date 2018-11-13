from math import sqrt

a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c

if d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    print(x1, x2)
elif d == 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    print(x1)
