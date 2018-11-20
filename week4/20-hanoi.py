def move(n, x=1, y=3, b=2):
    if n > 0:
        move(n - 1, x, b, y)
        print(n, x, y)
        move(n - 1, b, y, x)


n = int(input())
move(n)
