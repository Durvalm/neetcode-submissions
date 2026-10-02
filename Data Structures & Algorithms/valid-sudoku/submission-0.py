class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ 
        {r, 1, 0}, {c, 1, 0}, {g, 1, 0, 0}
       (row, num, row_pos), (col, num, col_pos), (grid, num, grid_pos)
        for each cell we go, check if this number is already in the set
        """
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    continue
                grid = ("g", num, r // 3, c // 3)
                if (
                    ('r', num, r) in seen
                    or ('c', num, c) in seen
                    or grid in seen
                ):
                    return False
                seen.add(('r', num, r))
                seen.add(('c', num, c))
                seen.add(grid)
        return True



