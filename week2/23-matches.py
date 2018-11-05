l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

s1, s2, s3 = 1, 2, 3

# Разложим по порядку

if (l2 >= l3):
    l2, l3 = l3, l2
    r2, r3 = r3, r2
    s2, s3 = s3, s2
if (l1 >= l2):
    l1, l2 = l2, l1
    r1, r2 = r2, r1
    s1, s2 = s2, s1
if (l2 >= l3):
    l2, l3 = l3, l2
    r2, r3 = r3, r2
    s2, s3 = s3, s2

# Посчитаем расстояние

dist1 = l2 - r1
dist2 = l3 - r2

v1 = v2 = v3 = v3 = v4 = v5 = 4

if (dist1 <= 0 and dist2 <= 0) or (r2 <= r1 and r3 <= r1):
    print(0)
else:
    if dist1 <= 0:
        v1 = s3
    if dist2 <= 0:
        v2 = s1

    if r1 - l1 >= dist2:
        v3 = s1
    if r2 - l2 >= l3 - r1:
        v4 = s2
    if r3 - l3 >= dist1:
        v5 = s3

    if v1 < 4 or v2 < 4 or v3 < 4 or v3 < 4 or v5 < 4:
        print(min(v1, v2, v3, v4, v5))
    else:
        print(-1)
