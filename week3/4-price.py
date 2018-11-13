from math import floor

price = float(input())

roubles = int(price // 1)
kopeks = round((price - roubles) * 100)

print(roubles, kopeks)
