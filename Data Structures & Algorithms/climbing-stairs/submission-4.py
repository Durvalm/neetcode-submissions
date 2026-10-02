class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
        #     return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)

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
        return dfs(0)

        # if n <= 2:
        #     return n
        # dp = [0] * (n)
        # dp[0], dp[1] = 1, 2
        # print(dp)
        # print("---")
        # for i in range(2, n):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        #     print(dp)
        # return dp[n-1]
    

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