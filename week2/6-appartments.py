x = int(input())
y = int(input())

kvInPod = y - x + 1
kvDoPod = x - 1

if x > 0 and y > 0 and (x - 1) % (y - x + 1) == 0:
    print("YES")
else:
    print("NO")
