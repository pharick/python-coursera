from math import sqrt

a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c

if a == b == c == 0:
    print(3)
elif a == b == 0:
    print(0)
elif a == 0:
    print(1, -c / b)
elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    print(2, x1, x2)
elif d == 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    print(1, x1)
else:
    print(0)
