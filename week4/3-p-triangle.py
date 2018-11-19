from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def p_triangle(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)
    return(d1 + d2 + d3)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print(p_triangle(x1, y1, x2, y2, x3, y3))
