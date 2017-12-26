class QuickFindUF:

    def __init__(self, n: int):
        self.id = [index for index in range(n)]

    def connected(self, p: int, q: int):
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int):
        pid = self.id[p]
        qid = self.id[q]

        for index in range(len(self.id)):
            if self.id[index] == pid:
                self.id[index] = qid



