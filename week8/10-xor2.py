from functools import reduce

print(
    *map(
        lambda l: reduce(lambda a, b: a + b, l) % 2,
        zip(
            *map(
                lambda i: map(int, input().split()),
                range(int(input()))
            )
        )
    )
)
