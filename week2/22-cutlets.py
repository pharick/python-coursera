k = int(input())
m = int(input())
n = int(input())

if n <= k:
    print(m * 2)
else:
    print(((n * 2 - 1) // k + 1) * m)
