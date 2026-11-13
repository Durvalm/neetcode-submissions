class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_val = 0

        l = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue
            max_val = max(max_val, prices[r] - prices[l])
        return max_val
            
