def power(a, n):
    if n < 0:
        return 1 / power(a, n * -1)
    else:
        res = 1
        while n > 0:
            res *= a
            n -= 1
        return res


a = float(input())
n = int(input())

print(power(a, n))
