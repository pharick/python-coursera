from math import sqrt


def minDivisor(n):
    divisor = 2
    while divisor <= sqrt(n):
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n


n = int(input())
print(minDivisor(n))
