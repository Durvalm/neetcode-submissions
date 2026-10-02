class Solution:
    def climbStairs(self, n: int) -> int:
        ## RECURSIVE SOLUTION (DFS)
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)

        ## DP TOP-DOWN SOLUTION
        memo = {}
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        # return dfs(0)

        # ## DP - BOTTOM-UP
        # if n <= 2:
        #     return n
        # dp = [0] * (n)
        # dp[0], dp[1] = 1, 2
        # for i in range(2, n):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n-1]

        ## DP - BOTTOM-UP - SPACE-OPTIMIZED
        one, two = 1, 1
        for i in range(n - 1):
            tmp = two
            two = one + two
            one = tmp
        return two


    

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