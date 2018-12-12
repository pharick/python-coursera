queens = []

for i in range(8):
    queens.append(list(map(int, input().split())))

is_beating = False

for i in range(len(queens)):
    for j in range(i + 1, len(queens)):
        same_line = (queens[i][0] == queens[j][0] or
                     queens[i][1] == queens[j][1])
        same_diag = (abs(queens[i][0] - queens[j][0]) ==
                     abs(queens[i][1] - queens[j][1]))
        if same_line or same_diag:
            is_beating = True
            break

if is_beating:
    print("YES")
else:
    print("NO")
