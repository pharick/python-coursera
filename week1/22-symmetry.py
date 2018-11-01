n = int(input())

d1 = n // 10**3
d2 = n // 10**2 % 10
d3 = n // 10 % 10
d4 = n % 10

diff1 = d1 - d4
diff2 = d2 - d3

print((diff1 + 1) * (diff2 + 1))
