class Solution:
    def climbStairs(self, n: int) -> int:
        """
        0 -> 1 -> 2 -> 3
        1 + 1 + 1
        2 + 1
        1 + 2
        """       
        if n <= 2:
            return n

        dp = [1, 2]
        for i in range(2, n):
            cur = dp[0] + dp[1]
            tmp = dp[1]
            dp[1] = cur
            dp[0] = tmp
        return dp[1]
