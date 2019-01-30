print(
    *filter(
        lambda n: all(map(
            lambda i: n % i != 0,
            range(2, n // 2 + 1)
        )),
        range(2, int(input()) + 1)
    )
)
