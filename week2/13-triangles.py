a = int(input())
b = int(input())
c = int(input())

if (b > a):
    a, b = b, a
if (c > a):
    a, c = c, a

if a >= b + c:
    print("impossible")
else:
    if (a*a == b*b + c*c):
        print("rectangular")
    elif (a*a < b*b + c*c):
        print("acute")
    elif (a*a > b*b + c*c):
        print("obtuse")
