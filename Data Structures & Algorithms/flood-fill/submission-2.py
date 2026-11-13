class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        """
        get source color: 1
        target color: 2
        all adjacent ones with color 1, set to color 2.
        DFS or BFS would work I think
        """

        ROWS = len(image)
        COLS = len(image[0])
        src_color = image[sr][sc]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if src_color == color:
            return image

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                image[r][c] != src_color):
                return
            image[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return

        dfs(sr, sc)
        return image
        