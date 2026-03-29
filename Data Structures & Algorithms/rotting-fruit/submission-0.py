class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        
        if not grid or len(grid) == 0:
            return time
        

        # init
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append([row, col])
        
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        while fresh > 0 and len(q) > 0:
            l = len(q)

            for orange in range(l):
                r,c = q.popleft()

                for dr, dc in dir:
                    newrow = r + dr
                    newcol = c + dc

                    if (newrow in range(len(grid)) and newcol in range(len(grid[0])) and grid[newrow][newcol] == 1):
                        grid[newrow][newcol] = 2
                        q.append([newrow, newcol])
                        fresh -= 1
            time += 1
        

        return time if fresh == 0 else -1