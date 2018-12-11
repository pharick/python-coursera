n = int(input())
numbers = list(map(int, input().split()))
ref = int(input())

closest = numbers[0]
diff = abs(ref - closest)
for num in numbers:
    if abs(ref - num) < diff:
        closest = num
        diff = abs(ref - num)

print(closest)
