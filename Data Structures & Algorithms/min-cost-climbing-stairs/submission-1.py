class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1 -> 2 -> 3 -> 0


        [1-> 2-> 1-> 2-> 1-> 1-> 1] -> 0
        [4   5   3   3   2   1   1]

        """

        n = len(cost)
        dp = [0] * (n + 2)

        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 2], dp[i + 1])
        return min(dp[0], dp[1])