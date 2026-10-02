class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        nums = set(nums)

        for num in nums: 
            if (num - 1) in nums:
                continue
            count = 1
            while (num + 1) in nums:
                count += 1
                num += 1
            max_seq = max(count, max_seq)
        return max_seq

