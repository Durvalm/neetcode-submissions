class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                if grid[r][c] == FRESH:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nr >= ROWS 
                        or nc < 0 or nc >= COLS
                        or grid[nr][nc] != FRESH
                        ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = ROTTEN
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1

