class QuickUnionUF:

    def __init__(self, n: int):
        self.id = [index for index in range(n)]

    def root(self, i: int):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p: int, q: int):
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j
