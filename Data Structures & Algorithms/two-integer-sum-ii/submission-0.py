class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            n1 = numbers[start]
            n2 = numbers[end]
            sum_ = (n1 + n2) 

            if sum_ == target:
                return [start+1, end+1]
            if sum_ < target:
                start += 1
            elif sum_ > target:
                end -= 1
