p = int(input())
x = int(input())
y = int(input())

sum = x * 100 + y
sum += sum * p / 100

roubles = int(sum // 100)
kopeks = int(sum % 100)

print(roubles, kopeks)
