def sign(n):
    if (n > 0):
        return 1
    elif (n < 0):
        return -1
    else:
        return 0

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if sign(x1) == sign(x2) and sign(y1) == sign(y2):
    print("YES")
else:
    print("NO")
