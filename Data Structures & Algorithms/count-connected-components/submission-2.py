class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
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

    def getDifferentComponents(self):
        unique = set()
        for p in range(1, len(self.parent)-1):
            unique.add(self.parent[p])

        print(unique)
        
        return len(unique)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res