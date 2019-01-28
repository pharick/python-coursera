n = int(input())

cities = dict()
for _ in range(n):
    line = input().split()
    for i in range(1, len(line)):
        cities[line[i]] = line[0]

m = int(input())

for _ in range(m):
    print(cities[input()])
