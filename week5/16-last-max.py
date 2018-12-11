numbers = list(map(int, input().split()))

max_index = 0
max = numbers[max_index]

for i in range(1, len(numbers)):
    if numbers[i] >= max:
        max_index = i
        max = numbers[max_index]

print(max, max_index)
