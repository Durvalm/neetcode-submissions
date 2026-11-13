class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        memo = {}

        def recurse(i):
            nonlocal count
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            if i == n:
                count += 1
                return 1
            
            memo[i] = recurse(i + 1) + recurse(i + 2)
            return memo[i]
        
        return recurse(0)
        
