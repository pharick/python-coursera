def countSort(lst):
    counts = [0] * 101

    for n in lst:
        counts[n] += 1

    sortedStr = ""
    for i in range(len(counts)):
        sortedStr += (str(i) + " ") * counts[i]

    sortedLst = sortedStr.split()

    for i in range(len(lst)):
        lst[i] = sortedLst[i]


lst = list(map(int, input().split()))
countSort(lst)
print(*lst)
