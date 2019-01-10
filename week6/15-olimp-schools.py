fin = open("input.txt", "r", encoding="utf-8")

participants = []
for i in range(100):
    participants.append([0, i])

for line in fin:
    participants[int(line.split()[-2])][0] += 1

participants.sort(key=lambda school: -school[0])

i = 0
count = participants[i][0]
while participants[i][0] > 0 and participants[i][0] == count:
    print(participants[i][1])
    i += 1

fin.close()
