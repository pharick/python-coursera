fin = open("input.txt")

candidats = dict()
for line in fin:
    candidat, votes = line.split()
    candidats[candidat] = candidats.get(candidat, 0) + int(votes)

for candidate in sorted(candidats):
    print(candidate, candidats[candidate])
