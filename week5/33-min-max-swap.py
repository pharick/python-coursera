numbers = list(map(int, input().split()))

min_index = 0
max_index = 0
min = numbers[min_index]
max = numbers[max_index]

for i in range(len(numbers)):
    if numbers[i] < min:
        min_index = i
        min = numbers[min_index]
    if numbers[i] > max:
        max_index = i
        max = numbers[max_index]

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)
