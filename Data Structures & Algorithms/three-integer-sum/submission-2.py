class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -4, -1, -1, 0, 1, 2

        for i
            for j
        
        if i + j + k > 0
        since it's ascending order
        then we dont need to move j forward
        we can bring k down

        if i + j + k < 0
        then we need to move j forward
        """

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            k = len(nums) - 1
            j = i + 1
            while j < k:
                if nums[i] + nums[k] + nums[j] > 0:
                    k -= 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res


                    
