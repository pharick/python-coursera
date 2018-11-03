x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x_diff = x1 - x2
if x_diff < 0:
    x_diff = x2 - x1

y_diff = y1 - y2
if y_diff < 0:
    y_diff = y2 - y1

if x_diff % 2 == 0:
    if y_diff % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if y_diff % 2 == 0:
        print("NO")
    else:
        print("YES")
