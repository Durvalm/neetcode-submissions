class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [4, 1, 1, 4] -> 0 -> 0
         8   5  4  4 


        """
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n-1,-1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]