class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        main thing:
            for every cell that can be traversed, update it the distance to    
            nearest treasure chest
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        steps = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != INF):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = steps
                
            steps += 1

        

