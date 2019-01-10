fin = open("input.txt", "r", encoding="utf-8")

k = int(fin.readline())

scores = []
while True:
    line = fin.readline()
    if len(line) == 0:
        break

    lst = line.split()
    if int(lst[-3]) >= 40 and int(lst[-2]) >= 40 and int(lst[-1]) >= 40:
        scores.append(int(lst[-3]) + int(lst[-2]) + int(lst[-1]))

fin.close()

scores.sort()

if len(scores) <= k:
    print(0)
elif len(scores) == 1:
    print(scores[0])
elif scores[-k] == scores[-k - 1]:
    if scores[-k] == scores[-1]:
        print(1)
    else:
        for i in range(-k, -1):
            if scores[i] != scores[-k]:
                print(scores[i])
                break
else:
    print(scores[-k])
