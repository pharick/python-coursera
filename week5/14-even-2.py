numbers = list(map(int, input().split()))

for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=" ")
print()
