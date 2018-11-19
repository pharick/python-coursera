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


def reduce_fraction(n, m):
    divider = gcd(n, m)
    if divider == 1:
        return n, m
    return reduce_fraction(n // divider, m // divider)


n = int(input())
m = int(input())

n_socr, m_socr = reduce_fraction(n, m)
print(n_socr, m_socr)
