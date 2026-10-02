class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
[3,4,5,6,1,2] if it was rotated 4 times.

[1,2,3,4,5,6] if it was rotated 6 times.


1. [3,4,5,6  ----  1,2]
2. There's a certain point in the list where [n] > [n+1] -> 6 -> 1. Means we found it
3. There's 2 different parts of the list:
   - for the first list example, if we end on 6. nums[0] == 3 and nums[-1] == 2. 6 is greater   than both, which means the answer is to the right.
   - for the second list example, if we land on 1. nums[0] == 4 and nums[-1] == 3. 1 is smaller than both, which means it should keep going left if it's not the min already

        """
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
                
        return nums[l]

