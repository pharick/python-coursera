n = int(input())

numbers = set(range(1, n + 1))

line = input()

while line != "HELP":
    question = set(map(int, line.split()))
    answer = input()

    if answer == "YES":
        numbers &= question
    else:
        numbers -= question

    line = input()

print(*sorted(numbers))
