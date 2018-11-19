def sum_seq():
    n = int(input())
    if n == 0:
        return 0
    return n + sum_seq()


print(sum_seq())
