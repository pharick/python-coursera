a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b == 0:
    print("INF")
elif a == 0 or b*c - a*d == 0 or -b % a != 0:
    print("NO")
else:
    print(-b // a)
