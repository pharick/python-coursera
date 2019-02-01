from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, m):
        self.m = []
        for i in range(len(m)):
            self.m.append([])
            for j in range(len(m[i])):
                self.m[i].append(m[i][j])

    def __add__(self, other):
        if len(self.m) != len(other.m) or \
           len(self.m[0]) != len(other.m[0]):
            raise MatrixError(self, other)

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

    def transpose(self):
        transposed = []
        for i in range(len(self.m[0])):
            transposed.append([])
            for j in range(len(self.m)):
                transposed[i].append(self.m[j][i])
        self.m = transposed
        return Matrix(transposed)

    @staticmethod
    def transposed(matrix):
        transposed = []
        for i in range(len(matrix.m[0])):
            transposed.append([])
            for j in range(len(matrix.m)):
                transposed[i].append(matrix.m[j][i])
        return Matrix(transposed)


exec(stdin.read())
