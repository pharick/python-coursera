def merge(a, b):
    res = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    res += a[i:] + b[j:]

    return res

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
