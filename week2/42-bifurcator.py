start = int(input())
end = int(input())

while start != end:
    if start % 2 == 0 and start / 2 >= end:
        print(":2")
        start /= 2
    else:
        print("-1")
        start -= 1
