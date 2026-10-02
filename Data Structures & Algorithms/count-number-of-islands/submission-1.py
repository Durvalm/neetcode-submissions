class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        num_of_islands = 0

        def dfs(r, c):
            
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == "0" or
                (r, c) in visited):
                return
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    num_of_islands += 1
        return num_of_islands