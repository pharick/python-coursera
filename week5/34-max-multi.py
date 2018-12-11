numbers = list(map(int, input().split()))

max1_pos = numbers[0]
max2_pos = numbers[1]

if max1_pos < max2_pos:
    max1_pos, max2_pos = max2_pos, max1_pos

max1_neg = 0
max2_neg = 0

for i in range(0, len(numbers)):
    if numbers[i] > 0:
        if numbers[i] > max1_pos:
            max2_pos = max1_pos
            max1_pos = numbers[i]
        elif numbers[i] > max2_pos:
            max2_pos = numbers[i]
    else:
        if numbers[i] < max1_neg:
            max2_neg = max1_neg
            max1_neg = numbers[i]
        elif numbers[i] < max2_neg:
            max2_neg = numbers[i]

if (max1_pos * max2_pos > max1_neg * max2_neg):
    print(max2_pos, max1_pos)
else:
    print(max1_neg, max2_neg)
