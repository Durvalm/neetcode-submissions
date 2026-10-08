class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        target=12
        coins = [1, 5, 10]

        greedy approach:
        - start at 10, then go to 5 (doesnt fit), then 1 and 1 again        
        
        coins=[1,3,4]
        amount=6

        greedy approach doesnt work.
        - 4 - 1 - 1 = 6 (3 turns)
        - 3 - 3 = 6 (2 turns)

        this is a non contiguous substring, which brings me to recursive/brute-force solution
        - try all possibilities until sum is (amount)


        DP:
        coins: [1, 5, 10]    amount: 12
        dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for a in list:
            for c in coins:
        
        1 -> 1,5,10. We choose 1 and dp[a-c] == 0 (+ 1)
        5 -> 1 (3 attempts)


        



        """ 
        # turns = 0
        # for i in range(len(coins)-1, -1, -1):
        #     print(coins[i], amount)
        #     while coins[i] <= amount:
        #         amount -= coins[i]
        #         turns +=1
        # return turns if amount==0 else -1



        # memo = {}

        # def dfs(i):
        #     if i == 0:
        #         return 0
        #     if i in memo:
        #         return memo[i]

        #     res = float('inf')
        #     for c in coins:
        #         if (i - c) >= 0:
        #             res = min(res, 1 + dfs(i - c))
        #     memo[i] = res
        #     return res
        
        # res = dfs(amount)
        # return res if res <= amount else -1

        dp = [amount+1] * (amount+1)
        dp[0] = 0
        min_use = float('inf')

        for i in range(1, amount + 1):

            for c in coins:
                if (i - c) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1











        # dp = [amount + 1] * (amount + 1)
        # # 0, 1, 2, 3, 4, 5, 6
        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a - c])
        # print(dp)
        # return dp[amount] if dp[amount] != amount + 1 else -1
