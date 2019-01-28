numbers = list(map(int, input().split()))

was = set()
for n in numbers:
    if n in was:
        print("YES")
    else:
        print("NO")

    was.add(n)
