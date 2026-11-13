class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, num in enumerate(nums):
            if num in cache:
                return [cache[num], i]
            complement = target - num
            cache[complement] = i
        
