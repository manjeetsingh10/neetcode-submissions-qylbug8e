class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        if n == 0:
            return []

        # init adjacency map
        adj = {i:[] for i in range(n)}

        # iterate through all the courses and populate adj
        for i in range(len(pre)):
            a, b = pre[i]
            adj.get(a).append(b)
        
        visited = set()
        finalList = []

        def dfs(courseNumber = 0):
            if courseNumber < 0:
                print("returning 1")
                return False

            dependent = adj.get(courseNumber)
            if dependent == []:
                if courseNumber not in finalList:
                    finalList.append(courseNumber)
                return True
            for d in dependent:
                if d in visited:
                    print("returning 2")
                    return False
                # mark visited
                visited.add(d)
                if not dfs(d):
                    print("returning 3")
                    return False
                visited.remove(d)

            adj[courseNumber] = []
            print(adj)
            # finalCourses.add(courseNumber)
            finalList.append(courseNumber)
            return True
        
        print(adj)
        for i in range(n):
            if not dfs(i):
                print("returning 4")
                return []
        return finalList