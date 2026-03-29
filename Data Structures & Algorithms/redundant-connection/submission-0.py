class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.sizes = [1]* n
        self.remove = set()
        
    def findSP(self, x):
        if self.parent[x] == x:
            return self.parent[x]
        
        self.parent[x] = self.findSP(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        superParentA = self.findSP(a)
        superParentB = self.findSP(b)

        if superParentA == superParentB:
            self.remove.add((a,b))
            return False

        sizeA = self.sizes[superParentA]
        sizeB = self.sizes[superParentB]

        self.n-=1
        if sizeA >= sizeB:
            self.sizes[superParentA] += self.sizes[superParentB]
            self.parent[superParentB] = superParentA
        elif sizeB > sizeA:
            self.sizes[superParentB] += self.sizes[superParentA]
            self.parent[superParentA] = superParentB
        return True
    
    def components(self):
        return self.n
    def removable(self):
        return self.remove.pop()

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            dsu.union(u, v)
        
        a,b = dsu.removable()

        return [a,b]

        