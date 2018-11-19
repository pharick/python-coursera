def isPointInArea(x, y):
    frag1 = (x + 1)**2 + (y - 1)**2 <= 2**2 and y >= -x and y >= 2*x + 2
    frag2 = (x + 1)**2 + (y - 1)**2 >= 2**2 and y <= -x and y <= 2*x + 2
    return frag1 or frag2


x = float(input())
y = float(input())

if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
