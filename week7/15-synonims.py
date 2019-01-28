n = int(input())

words = dict()
for _ in range(n):
    word1, word2 = input().split()
    words[word1] = word2
    words[word2] = word1

print(words[input()])
