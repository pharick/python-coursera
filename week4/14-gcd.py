def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b

    return gcd(b, a % b)


a = int(input())
b = int(input())

print(gcd(a, b))
