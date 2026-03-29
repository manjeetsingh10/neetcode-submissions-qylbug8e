class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.sizes = [1]* n
        
    def findSP(self, x):
        if self.parent[x] == x:
            return self.parent[x]
        
        self.parent[x] = self.findSP(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        superParentA = self.findSP(a)
        superParentB = self.findSP(b)

        if superParentA == superParentB:
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

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if len(edges) >= n:
            return False
        # if not edges:
        #     return False
        dsu = DSU(n)
        for a,b in edges:
            if not dsu.union(a,b):
                return False
        
        print("N ", dsu.n)
        if dsu.components() == 1:
            return True
        return False
        