k = int(input())

count = 0
i = 1
while i <= k:
    n = i
    np = 0
    while n:
        np = np * 10 + (n % 10)
        n //= 10

    if i == np:
        count += 1

    i += 1

print(count)
