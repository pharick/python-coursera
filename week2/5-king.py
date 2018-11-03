x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x_diff = x1 - x2
y_diff = y1 - y2

x_diff_ok = x_diff == 1 or x_diff == -1 or x_diff == 0
y_diff_ok = y_diff == 1 or y_diff == -1 or y_diff == 0

if x_diff_ok and y_diff_ok:
    print("YES")
else:
    print("NO")
