dists = list(map(int, input().split()))
tariffs = list(map(int, input().split()))

dists.sort()
tariffs.sort(reverse=True)

res = 0
for i in range(len(dists)):
    res += dists[i] * tariffs[i]

print(res)
