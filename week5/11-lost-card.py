n = int(input())

sum = 0

for i in range(1, n + 1):
    sum += i

for i in range(n - 1):
    card = int(input())
    sum -= card

print(sum)
