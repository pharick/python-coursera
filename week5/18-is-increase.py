numbers = list(map(int, input().split()))

is_increase = True

for i in range(1, len(numbers)):
    if numbers[i] <= numbers[i - 1]:
        is_increase = False
        break

if is_increase:
    print("YES")
else:
    print("NO")
