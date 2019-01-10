fin = open("input.txt", "r", encoding="utf-8")

scores9 = []
scores10 = []
scores11 = []

for line in fin:
    lst = line.split()
    if int(lst[-2]) == 9:
        scores9.append(int(lst[-1]))
    elif int(lst[-2]) == 10:
        scores10.append(int(lst[-1]))
    elif int(lst[-2]) == 11:
        scores11.append(int(lst[-1]))

max9 = scores9[0]
max9_2 = scores9[1]
if max9_2 > max9:
    max9, max9_2 = max9_2, max9
for score in scores9:
    if score > max9:
        max9_2 = max9
        max9 = score
    elif score > max9_2 and score != max9:
        max9_2 = score

max10 = scores10[0]
max10_2 = scores10[1]
if max10_2 > max10:
    max10, max10_2 = max10_2, max10
for score in scores9:
    if score > max10:
        max10_2 = max10
        max10 = score
    elif score > max10_2 and score != max10:
        max10_2 = score

max11 = scores11[0]
max11_2 = scores11[1]
if max11_2 > max11:
    max11, max11_2 = max11_2, max11
for score in scores11:
    if score > max11:
        max11_2 = max11
        max11 = score
    elif score > max11_2 and score != max11:
        max11_2 = score

print(max9_2, max10_2, max11_2)
