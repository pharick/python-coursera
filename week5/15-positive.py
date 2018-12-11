numbers = list(map(int, input().split()))

positives = 0
for i in range(0, len(numbers)):
    if numbers[i] > 0:
        positives += 1

print(positives)
