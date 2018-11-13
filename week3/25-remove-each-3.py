string = input()

for i in range(0, len(string)):
    if i % 3 != 0:
        print(string[i], end="")
print()
