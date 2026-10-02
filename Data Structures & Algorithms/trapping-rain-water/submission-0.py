class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        left_bound = 0
        right = len(height) - 1
        right_bound = 0

        while left <= right:
            if left_bound <= right_bound:
                diff = left_bound - height[left]
                res += diff if diff > 0 else 0 
                left_bound = max(left_bound, height[left])
                left += 1
            else:
                diff = right_bound - height[right]
                res += diff if diff > 0 else 0 
                right_bound = max(right_bound, height[right])
                right -= 1
        return res
        