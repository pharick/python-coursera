s, n = map(int, input().split())
users = []

for i in range(n):
    users.append(int(input()))

users.sort()

res = 0
for i in range(n):
    s -= users[i]
    if s >= 0:
        res += 1
    else:
        break

print(res)
