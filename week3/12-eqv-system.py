a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if (a == d == 0):
    x = f / c
    y = e / b
else:
    y = (a*f - c*e) / (a*d - c*b)
    x = (e - b*y) / a

print(x, y)
