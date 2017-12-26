class QuickUnionWeightedUF:

    def __init__(self, n: int):
        self.id = [index for index in range(n)]
        self.size = [0 for _ in range(n)]

    def root(self, i: int):
        while i != self.id[i]:
            # path compression: half the lookup to grandparent
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p: int, q: int):
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)

        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

        self.id[i] = j
