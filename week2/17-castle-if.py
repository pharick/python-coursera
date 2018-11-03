a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

case1 = (a <= d and b <= e) or (b <= d and a <= e)
case2 = (b <= d and c <= e) or (c <= d and b <= e)
case3 = (a <= d and c <= e) or (c <= d and a <= e)

if case1 or case2 or case3:
    print("YES")
else:
    print("NO")
