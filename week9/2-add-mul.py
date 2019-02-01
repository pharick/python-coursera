from sys import stdin


class Matrix:
    def __init__(self, m):
        self.m = []
        for i in range(len(m)):
            self.m.append([])
            for j in range(len(m[i])):
                self.m[i].append(m[i][j])

    def __add__(self, other):
        res = []
        for i in range(len(self.m)):
            res.append([])
            for j in range(len(self.m[i])):
                res[i].append(self.m[i][j] + other.m[i][j])

        return Matrix(res)

    def __mul__(self, n):
        return Matrix(list(map(
            lambda l: list(map(lambda i: i * n, l)),
            self.m
        )))

    __rmul__ = __mul__

    def __str__(self):
        return "\n".join(map(lambda i: "\t".join(map(str, i)), self.m))

    def size(self):
        return len(self.m), len(self.m[0])


exec(stdin.read())
