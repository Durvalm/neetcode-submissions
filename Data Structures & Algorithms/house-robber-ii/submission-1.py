class Solution:
    def rob(self, nums: List[int]) -> int:
   
        n = len(nums)

        if n == 1:
            return nums[0]


        def robber(start, end):
            dp = [0] * (n + 2)
            for i in range(end, start - 1, -1):
                dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            return dp[start]
        
        return max(
            robber(0, n - 2),
            robber(1, n - 1)
        )


