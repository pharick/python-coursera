n = int(input())

fp = 0
fn = 1

if n == 0:
    print(fp)
elif n == 1:
    print(fn)
else:
    n -= 1
    while n > 0:
        tmp = fn
        fn = fp + fn
        fp = tmp
        n -= 1

    print(fn)
