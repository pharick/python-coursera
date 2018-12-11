numbers = list(map(int, input().split()))
k, c = list(map(int, input().split()))

numbers.append(0)

for i in range(len(numbers) - 2, k - 1, -1):
    numbers[i + 1] = numbers[i]

numbers[k] = c

for i in range(0, len(numbers)):
    print(numbers[i], end=" ")
print()
