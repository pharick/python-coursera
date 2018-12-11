from math import ceil

numbers = list(map(int, input().split()))

for i in range(0, ceil(len(numbers) / 2)):
    rev_i = len(numbers) - i - 1
    numbers[i], numbers[rev_i] = numbers[rev_i], numbers[i]

for i in range(0, len(numbers)):
    print(numbers[i], end=" ")
print()
