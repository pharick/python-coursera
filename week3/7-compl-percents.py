p = int(input())
x = int(input())
y = int(input())
k = int(input())

sum = x * 100 + y

for i in range(1, k + 1):
    sum += int(sum * p / 100)

roubles = int(sum // 100)
kopeks = int(sum % 100)

print(roubles, kopeks)
