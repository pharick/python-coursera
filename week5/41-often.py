numbers = list(map(int, input().split()))

max_number = number = 0
max_frequency = frequency = 0

for i in range(len(numbers)):
    number = numbers[i]
    frequency = 1
    for j in range(i + 1, len(numbers)):
        if numbers[j] == number:
            frequency += 1

    if frequency > max_frequency:
        max_number = number
        max_frequency = frequency

print(max_number)
