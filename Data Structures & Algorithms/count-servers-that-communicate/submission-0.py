class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        """
        How can we determine if there's no other number 1s in that row or col?

        create hashmap of column index and row index (first pass):
            3c: (3, 3), 3r: (3, 3), 1r: ((0, 0), (0, 1))
        then on the second pass, if len > 1 for col or row, then yes.
        if there's only 1, then it must be self, and it's false
        """
        hashmap = {}
        res = 0

        # prefill hashmap
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if f"r{r}" not in hashmap:
                        hashmap[f"r{r}"] = []
                    hashmap[f"r{r}"].append((r, c))
                    if f"c{c}" not in hashmap:
                        hashmap[f"c{c}"] = []
                    hashmap[f"c{c}"].append((r, c))

        # pass 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if max(len(hashmap[f"r{r}"]), len(hashmap[f"c{c}"])) > 1:
                        res += 1
        return res


