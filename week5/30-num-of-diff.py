numbers = list(map(int, input().split()))

count = 0

for i in range(len(numbers)):
    if i == 0 or numbers[i] != numbers[i - 1]:
        count += 1

print(count)
