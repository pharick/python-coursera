fin = open("input.txt")
occassions = dict()
words = fin.read().split()

for word in words:
    occassions[word] = occassions.get(word, 0) + 1

print(sorted(sorted(occassions), key=lambda word: -occassions[word])[0])
