class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        if n == 0:
            return False

        # init adjacency map
        adj = {i:[] for i in range(n)}

        # iterate through all the courses and populate adj
        for i in range(len(pre)):
            a, b = pre[i]
            adj.get(a).append(b)
        
        visited = set()
        finalCourses = set()

        def dfs(courseNumber = 0):
            if courseNumber < 0:
                print("returning here 4 ", courseNumber)
                return False

            dependent = adj.get(courseNumber)
            if dependent == []:
                return True
            for d in dependent:
                if d in visited:
                    print("returning here 1")
                    return False
                # mark visited
                visited.add(d)
                if not dfs(d):
                    print("returning here 2")
                    return False
            visited.clear()

            adj[courseNumber] = []
            print('adj after update ', courseNumber)
            print(adj)
            finalCourses.add(courseNumber)
            return True
        
        print(adj)
        for i in range(n):
            if i not in finalCourses and not dfs(i):
                print("returning here 3")
                return False
        return True