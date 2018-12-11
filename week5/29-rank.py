rank = list(map(int, input().split()))
height = int(input())

is_fit = False
for i in range(len(rank)):
    if (height > rank[i]):
        print(i + 1)
        is_fit = True
        break

if (not is_fit):
    print(len(rank) + 1)
