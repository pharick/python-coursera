def C(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if n == k:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)


n = int(input())
k = int(input())
print(C(n, k))
