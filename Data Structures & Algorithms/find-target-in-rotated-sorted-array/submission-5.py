class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        say mid is 5:
        say target is 1:

        5 > [n-1]:2 - means we're in the greater side
        if above and nums[mid] > target : go right
        else: go left
        
        say mid is 1:
        say target is 2:

        1 < [n-1]:2 - means we're in the lower side
        if above and nums[mid] < target: go right
        else: go left
        """

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
