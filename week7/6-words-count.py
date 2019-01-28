fin = open("input.txt", "r", encoding="utf-8")

unique_words = set()
for line in fin:
    words_in_line = line.split()
    for word in words_in_line:
        unique_words.add(word)

print(len(unique_words))
