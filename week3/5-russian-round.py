from math import floor, ceil

x = float(input())
fraction = floor((x % 1) * 10)

if fraction < 5:
    print(floor(x))
else:
    print(ceil(x))
