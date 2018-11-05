n = int(input())

last = 0
if n != 0:
    count = 1
else:
    count = 0
max_count = count

while n != 0:
    last = n
    n = int(input())

    if n == last:
        count += 1
    else:
        count = 1

    if count > max_count:
        max_count = count

print(max_count)
