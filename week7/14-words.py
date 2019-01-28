fin = open("input.txt")
words = fin.read().split()
occasions = dict()

for word in words:
    current = occasions.get(word, 0)
    occasions[word] = current + 1
    print(current, end=" ")
print()
