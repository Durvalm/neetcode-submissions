class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i >= n:
        #         print(i == n)
        #         return i == n
        #     return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)

        memo = {}
        def dfs(i):
            if i >= n:
                return i == n
            if i in memo:
                return memo[i]
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)
    

    """
    (2)

1               2

1
    """     


    """
            (3)
        1     |      2
    1       2 | 1           
    1         |
    """