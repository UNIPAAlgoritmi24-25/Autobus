class UnionFind:
    def __init__(self, nodi):
        self.parent = {nodo: nodo for nodo in nodi}
        self.rank = {nodo: 0 for nodo in nodi}

    def find(self, nodo):
        if self.parent[nodo] != nodo:
            self.parent[nodo] = self.find(self.parent[nodo])
        return self.parent[nodo]

    def union(self, nodo1, nodo2):
        root1 = self.find(nodo1)
        root2 = self.find(nodo2)

        if root1 == root2:
            return False  # già connessi → creerebbe un ciclo

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True
