n = int(input())
zeros = 0

for i in range(n):
    number = int(input())
    if number == 0:
        zeros += 1

print(zeros)
