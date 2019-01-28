start1, end1, start2, end2 = map(int, input().split())

if start1 > end1:
    start1, end1 = end1, start1
if start2 > end2:
    start2, end2 = end2, start2

if start1 > start2:
    start1, end1, start2, end2 = start2, end2, start1, end1

if end1 < start2:
    print(0)
elif start1 == start2 or end1 == end2:
    print(min(end1 - start1 + 1, end2 - start2 + 1))
else:
    print(abs(end1 - start2) + 1)
