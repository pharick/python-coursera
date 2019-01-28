n, k = map(int, input().split())
days = [False] * n

for party in range(k):
    a, b = map(int, input().split())
    for day in range(a - 1, n, b):
        days[day] = True

strikes = 0
for day in range(n):
    if (day + 1) % 7 != 0 and (day + 2) % 7 != 0 and days[day]:
        strikes += 1

print(strikes)
