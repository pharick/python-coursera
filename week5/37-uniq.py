numbers = list(map(int, input().split()))
uniq = []

for i in range(len(numbers)):
    if not (numbers[i] in numbers[:i] or numbers[i] in numbers[i + 1:]):
        uniq.append(numbers[i])

print(*uniq)
