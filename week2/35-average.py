n = int(input())
count = 0
summ = 0
while n != 0:
    count += 1
    summ += n
    n = int(input())

print(summ / count)
