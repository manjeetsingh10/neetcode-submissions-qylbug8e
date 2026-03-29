class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return

        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()

        # push all treasures
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                    grid[nr][nc] != 2147483647):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))