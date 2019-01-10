n = int(input())
places = []
i = 1
for place in map(int, input().split()):
    places.append((place, i))
    i += 1
places.sort()

m = int(input())
shelters = []
i = 1
for shelter in map(int, input().split()):
    shelters.append((shelter, i))
    i += 1
shelters.sort()

res = []
last_j = 0
for i in range(n):
    for j in range(last_j, m):
        if j != m - 1:
            razn1 = abs(places[i][0] - shelters[j][0])
            razn2 = abs(places[i][0] - shelters[j + 1][0])
        if j == m - 1 or razn1 < razn2:
            res.append((places[i][1], shelters[j][1]))
            last_j = j
            break

res.sort()

for item in res:
    print(item[1], end=" ")
print()
