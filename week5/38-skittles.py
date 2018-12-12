n, k = list(map(int, input().split()))

skittles = list("I" * n)

for i in range(k):
    l, r = list(map(int, input().split()))
    for j in range(l, r + 1):
        skittles[j - 1] = "."

print("".join(skittles))
