n = int(input())

numbers = set(range(1, n + 1))

line = input()

while line != "HELP":
    question = set(map(int, line.split()))

    if len(numbers & question) > len(numbers) / 2:
        print("YES")
        numbers &= question
    else:
        print("NO")
        numbers -= question

    line = input()

print(*sorted(numbers))
