numbers = list(map(int, input().split()))
index = int(input())

for i in range(index, len(numbers) - 1):
    numbers[i] = numbers[i + 1]

numbers.pop()

for i in range(0, len(numbers)):
    print(numbers[i], end=" ")
print()
