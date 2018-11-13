from math import sqrt

xn = int(input())

n = 0
summ = 0
summ_2 = 0

while xn:
    n += 1
    summ += xn
    summ_2 += xn * xn
    xn = int(input())

s = summ / n

print(sqrt((summ_2 - 2 * s * summ + n * s * s) / (n - 1)))
