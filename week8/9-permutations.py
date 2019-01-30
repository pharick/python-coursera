from itertools import permutations
print(*map(lambda variant: "".join(map(lambda n: str(n), variant)), permutations(range(1, int(input()) + 1))), sep="\n")
