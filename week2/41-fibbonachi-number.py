fk = int(input())

fp = 0
fn = 1

if fk == 0:
    print(fp)
elif fk == 1:
    print(fn)
else:
    count = 1
    while fn < fk:
        tmp = fn
        fn = fp + fn
        fp = tmp
        count += 1

if fn == fk:
    print(count)
else:
    print(-1)
