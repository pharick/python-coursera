numbers = list(map(int, input().split()))

start = 0
while numbers[start] <= 0:
    start += 1

min = numbers[start]

for i in range(start, len(numbers)):
    if numbers[i] > 0 and numbers[i] < min:
        min = numbers[i]

print(min)
