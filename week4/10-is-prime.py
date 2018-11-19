from math import sqrt


def isPrime(n):
    divider = 2
    while divider <= sqrt(n):
        if n % divider == 0:
            return False
        divider += 1
    return True


n = int(input())

if isPrime(n):
    print("YES")
else:
    print("NO")
