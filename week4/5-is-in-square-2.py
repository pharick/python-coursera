def isPointInSquare(x, y):
    return y >= x - 1 and y <= x + 1 and y >= -x - 1 and y <= -x + 1


x = float(input())
y = float(input())

if isPointInSquare(x, y):
    print("YES")
else:
    print("NO")
