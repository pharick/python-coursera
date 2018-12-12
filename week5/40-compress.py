numbers = list(map(int, input().split()))
compressed = []

for n in numbers:
    if n != 0:
        compressed.append(n)

for _ in range(len(numbers) - len(compressed)):
    compressed.append(0)

print(*compressed)
