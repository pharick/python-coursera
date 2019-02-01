from sys import stdin


class Matrix:
    def __init__(self, m):
        self.m = []
        for i in range(len(m)):
            self.m.append([])
            for j in range(len(m[i])):
                self.m[i].append(m[i][j])

    def __str__(self):
        return "\n".join(map(lambda i: "\t".join(map(str, i)), self.m))

    def size(self):
        return len(self.m), len(self.m[0])


exec(stdin.read())
