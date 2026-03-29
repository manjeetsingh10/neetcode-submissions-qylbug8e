class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = 0
        if not grid or len(grid) == 0:
            return land
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    #call bfs
                    self.bfs(grid, row, col)
                    land += 1
                
        return land
    
    def bfs(self, grid, row, col):
        # mark r,c as visited
        grid[row][col] = "0"
        dir = [(0,1), (1,0), (0,-1), (-1,0)]
         
        for dr, dc in dir:
            nr = row + dr
            nc = col + dc

            if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == "1"):
                # call bfs
                self.bfs(grid, nr, nc)
        return
                


        