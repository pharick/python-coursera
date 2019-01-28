fin = open("input.txt", encoding="utf-8")
fout = open("output.txt", mode="w", encoding="utf-8")

candidats = dict()
votes = 0

for candidat in fin:
    candidat = candidat.strip()
    candidats[candidat] = candidats.get(candidat, 0) + 1
    votes += 1

results = sorted(sorted(candidats), key=lambda candidat: -candidats[candidat])

if candidats[results[0]] > votes / 2:
    fout.write(results[0] + "\n")
else:
    fout.write(results[0] + "\n")
    fout.write(results[1] + "\n")

fin.close()
fout.close()
